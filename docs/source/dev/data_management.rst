===========================
Data and service management
===========================

The PAVICS project Data Server is built around a Thematic Real-time Environmental Distributed Data Service (THREDDS). This service allows for real-time collection and presentation of archived data and metadata using remote access protocols to bridge the gap between data providers and researchers. 

The THREDDS Project is an Open Source initiative maintained by UCAR's Unidata Program. For more information on Unidata, see the `Project Home Page <https://www.unidata.ucar.edu/>`_. To learn more about THREDDS, view the `Project Description <https://github.com/Unidata/thredds/>`_ on GitHub.  

To better understand the way THREDDS integrates within PAVICS, see the System Architecture :doc:`../arch/overview`.

NetCDF file management in THREDDS
=================================

File conventions
----------------

NetCDF files integrated in the PAVICS platform must follow the CF Conventions document: http://cfconventions.org/

In order to benefit from the search engine capabilities, typical global attributes should be set. Currently the platorms searches the following fields::

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

NetCDF files with multiple variables are presently not fully supported

Adding files
------------

NetCDF files can be manually added to the THREDDS Data Server by copying them to the directory used as a docker volume in ``docker-compose.yml`` (see :doc:`installation`).

In order for new files to be catalogued, the Solr and PAVICS-DataCatalog components must be running and pavicrawler must be run::

    # replace localhost and port number with your PAVICS-DataCatalog deployment address
    http://localhost:8086/pywps?service=WPS&request=execute&version=1.0.0&identifier=pavicrawler&storeExecuteResponse=true&status=true&DataInputs=

.. note:: 
	The pavicrawler scans for typical attributes (mostly defined by CMIP) in the NetCDF global attributes. This allows search by facets by other components of the platform. 

After running the pavicrawler, new entries in the catalog should appear in Solr::

    http://localhost:8983/solr/#/birdhouse/query
    # must Execute Query, with relevant search criteria, or by increasing rows to get more results

Birdhouse Solr
==============

The birdhouse solr uses deduplication
(http://wiki.apache.org/solr/Deduplication) on the fields "source" and "url".
Essentially the id is a hash of the combination of those fields. This is
defined in solrconfig.xml
(e.g. https://github.com/bird-house/birdhousebuilder.recipe.solr/blob/master/birdhousebuilder/recipe/solr/templates/solrconfig.xml)

THREDDS Data Server example
===========================

An example of a public THREDDS Data Server can be found here:
https://data.nodc.noaa.gov/thredds/catalog.html

Adding external services
========================

.. todo::
	How to add WPS, WMS, WFS servers to PAVICS.