Using the graphical interface
=============================

The frontend is composed of a base map, a tool menu and a dashboard.


The basemap works like similar online maps, with the mouse wheel allowing zoom control, while click and drag lets you move laterally on the map. At the moment, only the standard rectangular projection is supported. There are three different options for the basemap: a satellite view, and an administrative view with and without labels. Let us know which other projection and basemap would be useful for your needs.

At the bottom of the screen is a colorbar with min and max values. Use these to set the limits on the colorbar for displayed netCDF datasets.

Tool menu
~~~~~~~~~
The tool menu is located at the bottom left corner and looks like a pie. It opens five panels that provide methods for interacting with the map and overlayed datsets available within the PAVICS-SDI:

Clicked Point Information
   When a netCDF dataset is displayed on the map, clicking on a grid cell will display the information stored at that point.

A Time Series Chart
   When a netCDF dataset is displayed on the map, clicking on a grid cell will load the time series at that point and display it on a graphic.

A Data Layer Visibility Switcher
   This panel lets user select which basemap, netCDF dataset and geospatial layer is displayed on the map.

A Temporal Slider
   When a netCDF dataset is displayed on the map, the time slider controls which time slice is displayed. You may pick a date then go forward or backward in time by specific increments.

Other Map Controls
   TODO


Each panel element can be used to view/inspect different types and display additional information of the active data.


..
    Example
    ~~~~~~~

    For an example of a climate analysis process using the PAVICS-frontend, see this short :download:`hands-on video <images/PAVICS_process.mp4>`.


Dashboard
---------
The right hand side dashboard contains four different sections: dataset search, project workspace, process and workflow launcher and process monitoring.

Dataset Search
   This interface is used to search for netCDF files on the PAVICS-SDI platform. It initially displays typical search categories that can be refined by loading additional search facets. Click on values for the different categories to restrict the search. Search results appear in the bottom section of the dashboard. Select the datasets of interest and add them to your workspace to visualize them or feed them into an analytical process.

   Search queries or search results can be saved for later use. TODO.

Project Workspace
   The workspace area lets you create projects in which an ensemble of files, search queries, workflows and process outputs can be stored. At the moment it is not possible for users to upload files or geospatial layers to the workspace. Let us know if this is a feature you'd like to have.

Process and Workflows
   This is the interface where computations are launched. You may launch a workflow (see :ref:`sec-workflows`) or a process (see :ref:`sec-processes`). The workflow dashboard let's you select from existing workflows that have been defined within the project or edit a new workflow from a template. Saving the workflow will trigger a validator that will warn you of syntax errors. Once the workflow has been validated, you may launch it already if there are no user defined inputs to be specified. Otherwise a form will appear to let you enter input values before launching the workflow. A notification will let you know if the workflow launched sucessfully or not.

   The process interface first asks you to identify the process provider. We realize that you probably have no idea which services are offered by which provider, and for now, we suggest you search for relevant processes in this documentation, note the package they are coming from and use this as the provider. We'll eventually *flatten* the process list and allow you to search from the list of processes.



