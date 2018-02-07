===============
Data management
===============

Manually adding NetCDF files
============================

NetCDF files can be manually added to the THREDDS Data Server by copying
them to the directory used as a docker volume in docker-compose.yml (see
:doc:`installation`).

In order for the new files to be catalogued, the Solr and PAVICS-DataCatalog
components must be running and pavicrawler must be run::

    # replace localhost and port number with your PAVICS-DataCatalog deployment address
    http://localhost:8086/pywps?service=WPS&request=execute&version=1.0.0&identifier=pavicrawler&storeExecuteResponse=true&status=true&DataInputs=

Note that the crawler scans for typical attributes (mostly defined by CMIP) in
the NetCDF global attributes. This allows search by facets by other components
of the platform. This list is currently not configurable and includes::

    project
    institute
    model
    experiment
    frequency

It is highly recommended that those attributes, when applicable, be properly
set in the added NetCDF files, as well as the variables standard_name,
long_name and units.

Furthermore, a dataset_id global attribute for each collection of files
that consitute a timeseries is recommended.

New entries in the catalog should appear in Solr::

    http://localhost:8983/solr/#/birdhouse/query
    # must Execute Query, with relevant search criteria, or by increasing rows to get more results


THREDDS Data Server example
===========================

An example of a public THREDDS Data Server can be found here:
https://data.nodc.noaa.gov/thredds/catalog.html
