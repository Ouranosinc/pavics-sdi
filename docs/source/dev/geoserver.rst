========================
Geoserver administration
========================


Before you Begin
================

It's advised that you create a ``Workspace``. For more information on Workspaces and the data structure of GeoServer, refer to the .. _GeoServer Online Documentation: http://docs.geoserver.org/stable/en/user/data/webadmin/workspaces.html


Methods of adding data to GeoServer 
===================================

There are two possible methods for loading data sets into a store in GeoServer. Both require write access credentials to the GeoServer Administrator panel. Employing SCP/SSH is a more manual method and the 


The SCP/SSH Method
------------------

.. note::
	
	You must have a user with write access to the server-side GeoServer filesystem. 

Folders can be loaded with Vector and Raster data in many formats and can be stored in the same parent folder. 

* Begin by tunneling into the server::

	ssh user@server

* Determine where the GeoServer exists on your server. Navigate to this directory and create a new folder that will contain your new data sets::

	mkdir /GeoServer/DATASETS	

* On your local terminal, navigate to your directory containing your data and run ``scp`` on the folder recursively::
	
	scp -pr localdata user@server:/PATHTO/GeoServer/DATASETS/

* login to the GeoServer Administration Panel, login and click on "Stores" in the sidebar.

* Click on "Add new Store"

* Specify the type of data you are adding (e.g. Shapefile, GeoTIFF, PostGIS DB, etc.). Each option will allow you to load one such file at a time. If you already have a Workspace, you can specify to associate the data with it. If you are adding several Shapefiles, select the option for "Directory of Shapefiles".

.. note::
	
	Click the "Enabled" box or uploaded layers won't be available!


The QGIS GeoServer Explorer Method
----------------------------------

.. note::
	
	You must have a working installation of QGIS (2.14.x, 2.18.x, 3.x) and access to the QGIS Plugin Manager. QGIS is multi-OS and available at .. _QGIS.org: https://qgis.org/en/site/

* From the QGIS window menu, select ``Plugins`` --> ``Manage and Install Plugins``. From the plugin list, find "GeoServer Explorer" and click "Install Plugin". 

* Open your data layers in QGIS and name them accordingly. 

* From the ``Web`` menu tab, select ``GeoServer Explorer`` and a new window will pop-up or appear below the processing toolbox. 




.. todo::

	Add images for the step-by-step processes

	How to modify the meta data associated with layers (how they appear in the interface)

