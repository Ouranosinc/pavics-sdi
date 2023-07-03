# Working with Web Processing Service with Python and OWSLib


In this notebook, you will interact with a Web Processing Service (WPS) server using the [OWSLib](https://geopython.github.io/OWSLib/) library, a client for OGC Web Services. More specifically, you'll learn how to list available processes, get information about a process, and execute a process. If you need more information than provided here, refer to the [OWSLib documentation](https://geopython.github.io/OWSLib/#wps).


## Connect to server and list processes

Here is how to establish a connection to a WPS server and list the available processes. We first connect to the server, then send a `getCapabilities` request to the server, which answers with a list of all the processes it hosts. This allows the client to populate its `processes` attribute. 

```python

from owslib.wps import WebProcessingService

# Connect to the server
wps = WebProcessingService('https://pavics.ouranos.ca/twitcher/ows/proxy/finch')

# Send a `getCapabilities` request to populate the list of processes
wps.getcapabilities()

# Print out the identifiers of five processes
processes = [x.identifier for x in wps.processes]
print(processes[:5])
```

## Get information about a single process
 
Assume we're interested in using the `humidex` process, we first need to know which arguments this process expects. To get this information, we must first send a `describeProcess` request to the server for the process description. 

```python

process = wps.describeprocess('humidex')
print(process.title, " : ", process.abstract)
print ([x.identifier for x in process.dataInputs])
```

Each process has a list of `dataInput` objects, each with an individual title and abstract, a list of supported data types, constraints on the minimum and maximum of values it can take, and optionally a default value. For example, the `tas` argument is mandatory (`minOccurs` is set to 1).

```python 

tas = process.dataInputs[0]
print(tas.abstract)
print(tas.minOccurs)
```

Similarly, each process' has a list of `processOutput` object with descriptive fields, in addition to methods to retrieve the actual data from the server once the process has been executed. 

```python  

from owslib.wps import ComplexDataInput

url = "https://pavics.ouranos.ca/twitcher/ows/proxy/thredds/fileServer/birdhouse/testdata/xclim/cmip5/tas_Amon_CanESM2_rcp85_r1i1p1_200701-200712.nc"

exec = wps.execute("tg_mean", inputs=[
         ("tas", ComplexDataInput(url)), 
         ("data_validation", "log")], 
         mode="sync")

print(exec.status)
```

## Retrieving the execution results

In synchronous mode, once the execution has completed the client automatically fetches the response. The response is an XML document that either stores the results, or links to the results, depending on how the process and server are configured. 

```python

out = exec.processOutputs[0]

# The link to the output stored on the server 
print(out.reference)
```

You may retrieve the data directly with `out.retrieveData()`, in the case above you'll get the bytes of the netCDF result file, or save the results to a file on disk using `exec.getOutput(out.identifier, filepath="path/to/file")`. 
