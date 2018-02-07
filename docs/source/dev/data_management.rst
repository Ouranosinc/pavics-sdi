===============
Data management
===============

NetCDF files specifications
===========================

NetCDF files integrated in the PAVICS platform must follow the CF Conventions
document: http://cfconventions.org/

In order to benefit from the search engine capabilities, typical global
attributes should be set. Currently the platorms searches for::

    project
    institute
    model
    experiment
    frequency

For variables, the standard_name and units should follow the CF standard name
table: http://cfconventions.org/standard-names.html

By default, the dataset_id will be made up of the relative path on the thredds
server. It is recommended to provide the dataset_id as a global attribute
in each NetCDF file that is unique for each collection of files that constitute
a timeseries.

NetCDF files with multiple variables are presently not fully supported.


Manually adding NetCDF files
============================

NetCDF files can be manually added to the THREDDS Data Server by copying
them to the directory used as a docker volume in docker-compose.yml (see
:doc:`installation`).

In order for the new files to be catalogued, the Solr and PAVICS-DataCatalog
components must be running and pavicrawler must be run::

    # replace localhost and port number with your PAVICS-DataCatalog deployment address
    http://localhost:8086/pywps?service=WPS&request=execute&version=1.0.0&identifier=pavicrawler&storeExecuteResponse=true&status=true&DataInputs=

New entries in the catalog should appear in Solr::

    http://localhost:8983/solr/#/birdhouse/query
    # must Execute Query, with relevant search criteria, or by increasing rows to get more results


THREDDS Data Server example
===========================

An example of a public THREDDS Data Server can be found here:
https://data.nodc.noaa.gov/thredds/catalog.html
