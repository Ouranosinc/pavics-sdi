===========================
Basic climate data analysis
===========================

Spatial subsetting and regridding is a method of deriving a new set of data from another set of data using interpolation techniques to generate different spatial or temporal resolutions.

For more information on these processes, see the `NCAR description of regridding page <https://climatedataguide.ucar.edu/climate-data-tools-and-analysis/regridding-overview>`_. 


Spatial and temporal subsetting
-------------------------------

.. autoprocess:: flyingpigeon.processes.SubsetWFSProcess

.. autoprocess:: flyingpigeon.processes.AveragerWFSProcess

.. autoprocess:: flyingpigeon.processes.ClippingProcess

.. autoprocess:: flyingpigeon.processes.ClipcontinentProcess

.. autoprocess:: flyingpigeon.processes.ClipregionseuropeProcess

.. autoprocess:: flyingpigeon.processes.PointinspectionProcess

.. autoprocess:: flyingpigeon.processes.LandseamaskProcess

.. autoprocess:: pavics_datacatalog.wps_processes.Period2Indices

.. autoprocess:: pavics_datacatalog.wps_processes.GetPoint


Spatial regridding
----------

.. todo::
	Add content to the basic climate data analysis section

