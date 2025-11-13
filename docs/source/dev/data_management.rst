=======================
NetCDF data  management
=======================

The PAVICS architecture relies on the Thematic Real-time Environmental Distributed Data Service (THREDDS) server to distribute netCDF files. This service allows for real-time collection and presentation of archived data and metadata using remote access protocols to bridge the gap between data providers and researchers.

The THREDDS Project is an Open Source initiative maintained by UCAR's Unidata Program. For more information on Unidata, see the `Project Home Page <https://www.unidata.ucar.edu/>`_. To learn more about THREDDS, view the `Project Description <https://github.com/Unidata/thredds/>`_ on GitHub.

To better understand the way THREDDS integrates within PAVICS, see the System Architecture :doc:`../arch/overview`.

Data preparation for inclusion in the platform
----------------------------------------------

NetCDF files integrated in the PAVICS platform must follow the CF Conventions document: http://cfconventions.org/

For variables, the standard_name and units should follow the CF standard name table: http://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html

Adding files
------------

NetCDF files can be added to the THREDDS Data Server by system administrators, simply by copying them to the directory used as a docker volume in ``docker-compose.yml``. Contact mailto:pavics@ouranos.ca if there are datasets you'd like to see included.

Inspecting metadata
-------------------

An essential requirement for a functional platform is that netCDF data stored in THREDDS has complete and uniform metadata. Work is in progress to validate metadata fields as part of the cataloguing process.
