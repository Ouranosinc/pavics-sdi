Overview
========

PAVICS is a Spatial Data Infrastructure (SDI) for climate data. It is composed of modular components that together provide access to data and a library of climate services. It is meant to facilitate climate data analysis for both researchers and climate service providers. PAVICS is not intended to be installed on individual computers, but rather on servers located close to data archives.





There are multiple building blocks composing the PAVICS SDI:

`PAVICS-frontend`_
   The user interface (UI) handling user accounts, workspace, workflows and data visualization.

`PAVICS-DataCatalog`_
   The database storing the information about the climate data available to users.

`Birdhouse`_
   A collection of Web Processing Services (WPS) supporting data processing in the climate science community. It includes multiple sub-components.

Birdhouse/`Malleefowl`_
   Access to ESGF data nodes and THREDDS catalogs, workflow engine.

Birdhouse/`Flyingpigeon`_
   Climate services including indices computation, spatial analogs, weather analogs, species distribution model, subsetting and averaging, climate fact sheets, etc.

Birdhouse/`Hummingbird`_
   Climate Data Operators (CDO) and compliance-checker for netCDF files.

`Magpie`_
   Authentication and authorization services.

`THREEDS`_
   netCDF data server.

`GeoServer`_
   Geospatial data server.


These components work together to offer users a seamless access to data and a suite of services that can convert raw climate data into useful information, graphics and tables.


.. _PAVICS-frontend: https://github.com/Ouranosinc/PAVICS-frontend

.. _Magpie: https://github.com/Ouranosinc/Magpie

.. _PAVICS-DataCatalog: https://github.com/Ouranosinc/PAVICS-DataCatalog

.. _Birdhouse: http://bird-house.github.io/

.. _Flyingpigeon: https://github.com/bird-house/flyingpigeon

.. _Malleefowl: https://github.com/bird-house/malleefowl

.. _Hummingbird: https://github.com/bird-house/hummingbird

.. _GeoServer: http://geoserver.org/

.. _THREEDS: http://www.unidata.ucar.edu/software/thredds/current/tds/



