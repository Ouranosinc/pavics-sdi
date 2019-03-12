===========================
Data and service management
===========================

The PAVICS project Data Server is built around a Thematic Real-time Environmental Distributed Data Service (THREDDS). This service allows for real-time collection and presentation of archived data and metadata using remote access protocols to bridge the gap between data providers and researchers. 

The THREDDS Project is an Open Source initiative maintained by UCAR's Unidata Program. For more information on Unidata, see the `Project Home Page <https://www.unidata.ucar.edu/>`_. To learn more about THREDDS, view the `Project Description <https://github.com/Unidata/thredds/>`_ on GitHub.  

To better understand the way THREDDS integrates within PAVICS, see the System Architecture :doc:`../arch/overview`.

NetCDF file management in THREDDS
=================================


Data preparation for inclusion in the platform
----------------------------------------------

NetCDF files integrated in the PAVICS platform must follow the CF Conventions
document: http://cfconventions.org/

In order to benefit from the search engine capabilities, typical global
attributes should be set. Currently the platorms searches the following
fields::

    project
    institute
    model
    experiment
    frequency

For variables, the standard_name and units should follow the CF standard name
table: http://cfconventions.org/standard-names.html

It is recommended to provide a dataset_id as a global attribute
in each NetCDF file that is unique for each collection of files that constitute
a timeseries.

NetCDF files with multiple variables are presently not fully supported.


Adding files
------------

NetCDF files can be manually added to the THREDDS Data Server by copying them to the directory used as a docker volume in ``docker-compose.yml`` (see :doc:`installation`).

In order for new files to be catalogued, the Solr and PAVICS-DataCatalog components must be running and pavicrawler must be run::

    # replace localhost and port number with your PAVICS-DataCatalog deployment address
    http://localhost:8086/pywps?service=WPS&request=execute&version=1.0.0&identifier=pavicrawler&storeExecuteResponse=true&status=true&DataInputs=

Note that this crawls the whole THREDDS server and can take a very long time. In order to partially crawl the THREDDS server, use::

    http://localhost:8086/pywps?service=WPS&request=execute&version=1.0.0&identifier=pavicrawler&storeExecuteResponse=true&status=true&DataInputs=target_thredds=https://thredds_host.com/twitcher/ows/proxy/thredds/catalog/birdhouse/subpath/to/crawl

It is possible to restrict the crawling even more from the specified THREDDS path with the target_files argument to pavicrawler.

.. note:: 
	The pavicrawler scans for typical attributes (mostly defined by CMIP) in the NetCDF global attributes. This allows search by facets by other components of the platform. 

After running the pavicrawler, new entries in the catalog should appear in Solr::

    http://localhost:8983/solr/#/birdhouse/query
    # must Execute Query, with relevant search criteria, or by increasing rows to get more results

By default, the dataset_id will be made up of the relative path on the thredds
server.

Inspecting metadata
-------------------

An essential requirement for a functional platform is that netCDF data stored in THREDDS has complete and uniform
metadata. To do so, the :function:`pavics.catalog.thredds_crawler` function can be used to extract the metadata from the
netCDF files and see if there are missing entries::

   from pavics.catalog import thredds_crawler as crawler
   crawler('http://pavics.ouranos.ca/thredds', index_facets=['project'], exclude_files=['birdhouse/wps_outputs', 'birdhouse/workspaces'])

Note that running this command can take a long while, so the `include_files` argument can be passed to restrict the
crawler to certain directories, such as :file:`birdhouse/ouranos/climex/`.


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


Using thredds_crawler
=====================

Test code ::

  from thredds_crawler.crawl import Crawl
  Crawl('https://pavics.ouranos.ca/thredds/birdhouse/ouranos/climex/catalog.xml')
  Crawl('https://pavics.ouranos.ca/thredds/catalog/birdhouse/ouranos/climex/QC11d3_CCCma-CanESM2_rcp85/day/historical-r1-r1i1p1/tasmin/catalog.xml')