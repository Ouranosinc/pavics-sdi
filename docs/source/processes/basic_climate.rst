===========================
Basic climate data analysis
===========================

The following processes concern basic climate data analysis, methods for formatting data to examine a specific region or time interval.

..
    Spatial subsetting and regridding are methods of deriving a new set of data from another set of data using interpolation techniques to generate different spatial or temporal resolutions.

    For more information on these processes, see the `NCAR description of regridding page <https://climatedataguide.ucar.edu/climate-data-tools-and-analysis/regridding-overview>`_.


Spatial and temporal subsetting
-------------------------------

* :class:`~flyingpigeon.processes.wps_subset_wfs_polygon.SubsetWFSPolygonProcess` Subset over a contour provided by a WFS service.
* :class:`~flyingpigeon.processes.wps_subset_bbox.SubsetBboxProcess` Subset over a latitude-longitude bounding box.
* :class:`~flyingpigeon.processes.wps_subset_continents.SubsetcontinentProcess` Subset over one or more continent.
* :class:`~flyingpigeon.processes.wps_subset_countries.SubsetcountryProcess` Subset over one or more country.
* :class:`~flyingpigeon.processes.wps_pointinspection.PointinspectionProcess` Extract data over one or more point coordinates.
