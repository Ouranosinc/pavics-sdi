=========
Notebooks
=========

These notebooks demonstrates a few features of the PAVICS platform: how to access data through the OPeNDAP protocol and subset and retrieve it, how to render an image using the WMS protocol, how to compute climate indices, and perform bias correction.

If you're unfamiliar with notebooks, note that typing `TAB` after an object will display a drop-down menu of the object's attributes and methods, and that you need to hit `CTRL-Enter` to run a *cell*. You can also type `?` after a function or method to display the corresponding help message.

Note that some of these notebooks need the bleeding edge version of OWSLib_ (>=0.17.1) and Birdy_ since some issues were found and fixed in the process of writing these notebooks.

.. toctree::
   :maxdepth: 1

   ..
       subsetting

   rendering
   owslib_wms
   opendap
   finch
   owslib_wms
   pavics_thredds
   WCS_example
   WFS_example
   WPS_example


.. _OWSLib: https://geopython.github.io/OWSLib/
.. _Birdy: https://birdy.readthedocs.io
