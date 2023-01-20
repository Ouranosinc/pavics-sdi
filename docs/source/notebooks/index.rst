=========
Notebooks
=========

These notebooks demonstrate a few features of the PAVICS platform: how to access data through the OPeNDAP protocol and
subset and retrieve it, how to render an image using the WMS protocol, how to compute climate indices, and perform bias
correction.

If you're unfamiliar with notebooks, note that typing `TAB` after an object will display a drop-down menu of the
object's attributes and methods, and that you need to hit `CTRL-Enter` to run a *cell*. You can also type `?` after a
function or method to display the corresponding help message.


.. toctree::
   :maxdepth: 1

   rendering
   opendap
   esgf-dap
   pavics_thredds
   climex
   forecasts
   eccc-geoapi-climate-stations
   eccc-geoapi-xclim
   WCS_example
   WFS_example
   WPS_example
   WMS_example
   regridding
   subset-user-input


.. include:: ../deprecated/index.rst

-------------------------
Optional Notebooks
-------------------------

These following notebooks demonstrate *additional* and *optional* features of the PAVICS platform when corresponding
|pavics-components|_ or |pavics-opt-comp|_ are enabled.

.. toctree::
   :maxdepth: 1

   ../notebook-components/weaver_example


.. |pavics-components| replace:: Components
.. _pavics-components: https://github.com/bird-house/birdhouse-deploy/blob/master/birdhouse/components/README.rst
.. |pavics-opt-comp| replace:: Optional Components
.. _pavics-opt-comp: https://github.com/bird-house/birdhouse-deploy/blob/master/birdhouse/optional-components/README.rst
