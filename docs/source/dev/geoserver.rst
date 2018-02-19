========================
GeoServer administration
========================


Before you begin
================

It's advised that you create a ``Workspace``. For more information on Workspaces and the data structure of GeoServer, refer to the `GeoServer Online Documentation <http://docs.geoserver.org/stable/en/user/data/webadmin/workspaces.html>`_.


Adding data to GeoServer
========================

There are two possible methods for loading data sets into a store in GeoServer: using SCP/SSH or with QGIS GeoServer Explorer. Both require write access credentials to the GeoServer Administrator panel. Employing SCP/SSH is a more manual method and requires more configuration from within the GeoServer Administration portal while the QGIS GeoServer Explorer can save some time and provide an instantaneous result with less time spent setting layer properties.  


The SCP/SSH method
------------------

.. note::
	
	You must have write access permissions to the server-side GeoServer filesystem.

Folders can be loaded with Vector and Raster data in many formats and can be stored in the same parent folder. 

* Begin by tunneling into the server::

	ssh user@server

* Determine where the GeoServer data folder exists on your server. Navigate to this directory and create a new folder that will contain your new data sets::

	mkdir GeoServer/DATASETS

* On your local terminal, navigate to your directory containing your data and run ``scp`` on the folder recursively::
	
	scp -pr localdata user@server:/PATHTO/GeoServer/DATASETS/

* Login to the GeoServer Administration Panel and click on :guilabel:`Stores` in the sidebar.
* Click on :guilabel:`Add new Store`
* Specify the type of data you are adding (e.g. Shapefile, GeoTIFF, PostGIS DB, etc). Each option will allow you to load one such file at a time. If you already have a Workspace, you can specify to associate the data with it. If you are adding several Shapefiles, select the option for :guilabel:`Directory of Shapefiles`.

For more information on the Data Adding process from the GeoServer Administration Panel, see the `GeoServer Online Documentation <http://docs.geoserver.org/stable/en/user/gettingstarted/shapefile-quickstart/index.html>`_.


.. note::
	
	Click the :guilabel:`Enabled` box or uploaded layers won't be available!


The QGIS GeoServer Explorer method
----------------------------------

.. note::
	
	You must have a working installation of QGIS (2.14.x, 2.18.x) and access to the QGIS Plugin Manager. QGIS is multi-OS and available at `QGIS.org <https://qgis.org/en/site/>`_.

.. note::
	
	At the time of this writing, the newest point release of QGIS (3.0.x) does not support the QGIS GeoServer Explorer

* From the QGIS window menu, select :guilabel:`Plugins` then :guilabel:`Manage and Install Plugins`. From the plugin list, find "GeoServer Explorer" and click :guilabel:`Install Plugin`.
* Open your data layers in QGIS and name them accordingly.
* From the :guilabel:`Web` menu tab, select :guilabel:`GeoServer Explorer` and a new window will pop-up or appear below the processing toolbox.


.. todo::

   * Add images for the step-by-step processes
   * How to modify the meta data associated with layers (how they appear in the interface)

