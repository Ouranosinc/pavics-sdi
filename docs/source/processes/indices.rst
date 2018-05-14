===============
Climate indices
===============

The following processes return general climate indicators based on spatial and temporal grid resolutions.

.. autoprocess:: flyingpigeon.processes.FreezeThawProcess

.. autoprocess:: flyingpigeon.processes.Duration


ICCLIM indices
--------------

..
   import flyingpigeon as fp
   for c in fp.processes.wps_ocgis_func_ICCLIM_PROCESSES:
     s = str(c)
     print('.. autoprocess:: ' + s.split('object')[0][1:-1].replace('wps_ocgis_func.', '') + '\n')


.. autoprocess:: flyingpigeon.processes.ICCLIM_TXXProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_SDProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_R95PProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TX90PProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TG90PProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TXNProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_CDDProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_R99PTOTProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_SUProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_CFDProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TN10PProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TGProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TRProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_RX5DAYProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_VDTRProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_SD50CMProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_CWDProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TN90PProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_R20MMProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_CSUProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_RX1DAYProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_WSDIProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_RR1Process

.. autoprocess:: flyingpigeon.processes.ICCLIM_CSDIProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_R75PTOTProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_R95PTOTProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_R10MMProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_SDIIProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_DTRProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TG10PProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TXProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_PRCPTOTProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TNProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_R75PProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TNXProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_SD5CMProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_FDProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_R99PProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_IDProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_SD1Process

.. autoprocess:: flyingpigeon.processes.ICCLIM_GD4Process

.. autoprocess:: flyingpigeon.processes.ICCLIM_TNNProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_HD17Process

.. autoprocess:: flyingpigeon.processes.ICCLIM_ETRProcess

.. autoprocess:: flyingpigeon.processes.ICCLIM_TX10PProcess

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


