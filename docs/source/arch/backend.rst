=======
Backend
=======

.. image:: images/PAVICS_architecture.png

The Backend of PAVICS-SDI is built entirely with Free and Open Source Software. All of the backend projects (source code and documentation) are open to be inspected, built upon, or contributed to. 

Birdhouse
---------

PAVICS is largely built upon the many components developed as part of the `Birdhouse Project <https://github.com/bird-house/birdhouse-docs/blob/master/slides/birdhouse-architecture/birdhouse-architecture.pdf>`_.

The goal of Birdhouse is to develop an easy-to-use Web Processing Service to support remote analyses of climate data using python. The library components of Birdhouse are called 'Birds' while each 'bird' is built to perform a specific set of functions within the Birdhouse ecosystem. PAVICS components that are borrowed from within the official Birdhouse structure are the following:

Birdhouse/Malleefowl
    Access to ESGF data nodes and THREDDS catalogs, workflow engine.
    `Malleefowl Official Documentation <https://malleefowl.readthedocs.io/en/latest/>`_

Birdhouse/Flyingpigeon
    Climate services including indices computation, spatial analogs, weather analogs, species distribution model, subsetting and averaging, climate fact sheets, etc.
    `Flyingpigeon Official Documentation <https://flyingpigeon.readthedocs.io/en/latest/>`_
    
Birdhouse/Hummingbird
    Climate Data Operators (CDO) and compliance-checker for netCDF files.
    `Hummingbird Official Documentation <https://birdhouse-hummingbird.readthedocs.io/en/latest/>`_

.. note::
	Are there any other birds worth mentioning here?

Other Projects
--------------

PAVICS-SDI relies upon several other projects specialized for spatial and climate data management and presentation.

THREDDS 
    The *Thematic Real-time Environmental Distributed Data Services* (`THREDDS`_) is a server system for providing scientific data and metadata access through various online protocols. The PAVICS platform relies on THREDDS to provide access to all netCDF data archives, as well as output files created by processes. The code is hosted on this `GitHub repository <https://github.com/Unidata/thredds>`_.

ncWMS
    `ncWMS`_ is an implementation of the OGC's Web Mapping Service (WMS) specifically built for multidimensional gridded data such as the netCDF format. The PAVICS platform uses it to convert gridded netCDF data layers from a file or an OPeNDAP link to an image that can be accessed through WMS ``GetMap`` requests. See this `reference paper <https://doi.org/10.1016/j.envsoft.2013.04.002>`_ for more information.

GeoServer
    `GeoServer`_ is an OGC compliant server system built for viewing, editing, and presenting geospatial data. PAVICS uses GeoServer as its database for vectorial geospatial information, such as administrative regions and watersheds. See the `GeoServer documentation <http://docs.geoserver.org/>`_ for more information on its capabilities.


.. _`THREDDS`: https://www.unidata.ucar.edu/software/thredds/current/tds/

.. _`ncWMS`:  https://reading-escience-centre.github.io/ncwms/

.. _`GeoServer`: http://geoserver.org/about/



In-House Projects
-----------------

CRIM and Ouranos have also been actively involved in the planning and development of new and existing 'birds' to better perform very specific functions:

PAVICS-DataCatalog
    A database system for storing and serving information about available climate data.
    `PAVICS-DataCatalog GitHub Repository <https://github.com/Ouranosinc/PAVICS-DataCatalog>`_ 

Magpie
    Authentication and authorization services using RestAPI.
    `Magpie GitHub Repository <https://github.com/Ouranosinc/Magpie>`_

.. todo::
	Ask CRIM to review architecture backend 
