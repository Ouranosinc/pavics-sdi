Flood Frequency Analysis and Dam Safety in the 21st Century Climate
===================================================================

.. ::

    :ref:`Version en français<Analyse fréquentielle des crues>`


This project completed in March 2021 looked at how climate change information can be integrated into flood design values estimated by frequency analysis. The `report`_ includes maps showing the relative change in 1,000 and 10,000 return values for over 500 watersheds over Canada. The data underlying these figures is available online as a geospatial layer named ``public:decamillenial_flood_CC`` on the `Ouranos GeoServer <pavics.ouranos.ca/geoserver>`. This layer can be downloaded locally, streamed by GIS client (see instructions below) or accessed programmatically (see notebook_).


For each watershed, the results include the following properties:

name
  Watershed name
watershed_area
  Surface area (km²)
NSE
  Nash-Sutcliffe Efficiency of calibrated model
``<gcm>_PWM_<t>_[<p>_]<kind>``
  Climate change factor per unit area (mm/d/km²) computed following these specifications:

  - ``gcm``: Climate model, one of CESM1, CanESM2
  - *Probability Weighted Moments* calibration method
  - ``t``: return period, one of 1000, 10000
  - ``kind``: Factor operation, either additive (+), or multiplicative (*)
  - ``p`` (*optional*): percentile from bootstrap parameter uncertainty assessment, one of 0.75, 0.9, 0.95 or 0.99. If not present, the result is the direct estimate from the PWM method on the full sample.

.. warning::

   The ESRI Shapefile format limits field names to 10 characters. The column names above are thus truncated and replaced by an index (e.g. `CanESM2_18`), which complicates parsing. We recommend using the GeoPackage format when downloading the results.


QGIS Client Instructions
------------------------
#. Add a layer using the Web Feature Services (WFS) standard
   :guilabel:`Layer` -> :guilabel:`Add Layer` -> :guilabel:`Add WFS Layer ...`
#. Click on :guilabel:`New`
#. Enter the name and address of the PAVICS GeoServer
   :guilabel:`Name`: PAVICS
   :guilabel:`URL`: https://pavics.ouranos.ca/geoserver/ows?version=1.1.0&
#. Click :guilabel:`OK`
#. Click :guilabel:`Connect`
#. In table, select ``decamillenial_flood_CC``
#. Click :guilabel:`Add`,  the layer will be downloaded and should appear in the :guilabel:`Layers` widget.
#. Click :guilabel:`Close`

One the layer is available, you can access the various columns of the data table and display them.

#. Right click on ``decamillenial_flood_CC`` layer, select :guilabel:`Properties`
#. Select :guilabel:`Simple fill`
#. Click on icon right of :guilabel:`fill color` to pick which column should be color-coded.


.. _report: http://to.be.completed.pdf
.. _notebook: notebooks/cruesdeca.ipynb



Analyse fréquentielle des crues
===============================

Version en français à venir...
