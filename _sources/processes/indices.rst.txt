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
     print('.. autoprocess:: ' + s.split('object')[0][1:-1].replace('wps_ocgis_func.', 'icclim') + '\n')

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TXXProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_SDProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_R95PProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TX90PProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TG90PProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TXNProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_CDDProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_R99PTOTProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_SUProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_CFDProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TN10PProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TGProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TRProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_RX5DAYProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_VDTRProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_SD50CMProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_CWDProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TN90PProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_R20MMProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_CSUProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_RX1DAYProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_WSDIProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_RR1Process

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_CSDIProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_R75PTOTProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_R95PTOTProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_R10MMProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_SDIIProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_DTRProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TG10PProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TXProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_PRCPTOTProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TNProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_R75PProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TNXProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_SD5CMProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_FDProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_R99PProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_IDProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_SD1Process

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_GD4Process

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TNNProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_HD17Process

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_ETRProcess

.. autoprocess:: flyingpigeon.processes.icclim.ICCLIM_TX10PProcess

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


