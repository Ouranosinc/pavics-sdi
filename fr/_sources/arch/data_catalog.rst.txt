Data Catalog 
============

Pavics bundles a number of cataloguing services that allow you to search 
for data and add data to the catalog. 

PAVICS Catalogue Search
-----------------------
The ``pavicssearch`` service closely mimics the API for the Earth 
System Grid Federation (ESGF) search. The search fields (or *facets*)
include author, category, cf_standard_name, experiment, frequency, 
institute, model, project, source, subject, title, units, variable and
variable_long_name. The search results are returned in a ``json`` file and
include the URL to download the file or access it through DAP. 


Examples
~~~~~~~~
The request `pavicsearch&DataInputs=constraints=model:CRCM4,experiment:rcp85 <http://132.217.140.45:8009/pywps?service=WPS&request=execute&version=1.0.0&identifier=pavicsearch&DataInputs=constraints=model:CRCM4,experiment:rcp85>`_
will search for all files that are part of the RCP8.5 experiment and based on the CRCM4 model.







 


