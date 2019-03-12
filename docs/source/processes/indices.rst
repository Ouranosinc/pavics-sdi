===============
Climate indices
===============

The following processes return general climate indicators based on spatial and temporal grid resolutions.

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.FreezeThawProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.Duration


ICCLIM indices
--------------

..
   import flyingpigeon as fp
   for c in fp.processes.wps_ocgis_func_ICCLIM_PROCESSES:
     s = str(c)
     print('.. autoprocess:: ' + s.split('object')[0][1:-1].replace('wps_ocgis_func.', 'icclim') + '\n')

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TXXProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_SDProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_R95PProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TX90PProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TG90PProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TXNProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_CDDProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_R99PTOTProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_SUProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_CFDProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TN10PProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TGProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TRProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_RX5DAYProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_VDTRProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_SD50CMProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_CWDProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TN90PProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_R20MMProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_CSUProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_RX1DAYProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_WSDIProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_RR1Process

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_CSDIProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_R75PTOTProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_R95PTOTProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_R10MMProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_SDIIProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_DTRProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TG10PProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TXProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_PRCPTOTProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TNProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_R75PProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TNXProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_SD5CMProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_FDProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_R99PProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_IDProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_SD1Process

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_GD4Process

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TNNProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_HD17Process

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_ETRProcess

.. autoprocess:: flyingpigeon.processes.wps_ocgis_func.ICCLIM_TX10PProcess

..
    Climate Extreme indices
    -----------------------

    Averaged Climate indices
    ------------------------

    Temporal Indices
    ----------------

..
    .. autoprocess:: flyingpigeon.processes.ProcesssSimpleIndice

    .. autoprocess:: flyingpigeon.processes.ProcessPercentileIndice

    .. autoprocess:: flyingpigeon.processes.ProcessMultivarIndice


