===================
Workflow vocabulary
===================

Creating a climate product usually involves multiple steps:

#. Selecting datasets
#. Subsetting the data to a specific region and period
#. Either regridding the multiple datasets to a common grid or computing spatial averages
#. Computing climate indices
#. Create graphs or tables from the results

Typically each step would involve calling one or many individual processes, and it's convenient to combine these steps into a *workflow*. Here we use *workflow* to mean a formal description of the logical organization and ordering of individual processes. The workflow logic is encapsulated in a ``json`` file using a vocabulary (called a `schema <http://json-schema.org>`_) that we describe below.

Workflows are built by combining ``Workflow_task`` into ``Group_of_task``. These groups are then executed sequentially or in parallel, as indicated in the ``Workflow`` field (see the :ref:`schema`).


.. json:object:: Workflow

   High-level object describing a workflow.

  :property str name:  Workflow name
  :property list tasks:  Array of :json:object:`Workflow_task`. [optional*]
  :property list parallel_groups: Array of :json:object:`Group_of_tasks` being executed on multiple processes. [optional*]

.. note::

   Either ``tasks`` or ``parallel_groups`` must be specified.


.. json:object:: Workflow_task

   Describe an individual task.

   :property str name: Unique name given to each workflow task
   :property str url: Url of the WPS provider
   :property str identifier: Identifier of a WPS process
   :property dict inputs: Dictionary of inputs that must be fed to the WPS process. The key is the input name and the value is either the input data or an array of data if multiple values are allowed for this input. [optional]
   :property dict linked_inputs: Dictionary of dynamic inputs that must be fed to the WPS process and obtained by the output of other tasks. The key is the input name (or None) and the value is an :json:object:`Input_description` dictionary or an array of them if multiple values are allowed for this input. [optional]
   :property list progress_range: [optiona] Array [start, end] defining the overall progress range of this task. Default value is [0, 100].

.. note::

   * Allow to plan the execution of a task after another one without feeding any output of the previous one to an input.


.. json:object:: Group_of_task

   :property str name: Group of task name.
   :property int max_processes: Number of processes to run concurrently to process the data.
   :property map: Object describing what has to be mapped inside the group or an array of data that has to be mapped directly.
   :proptype map: :json:object:`Input_description`
   :property reduce: Object describing what has to be reduced before leaving the group.
   :proptype reduce: :json:object:`Input_description`
   :property list tasks: Array of :json:object:`Workflow_task` to run concurrently inside the group.


.. json:object:: Input_description

   Identifies the output of a process included in the workflow that serves as an input in a downstream process.

  :property str task: Name of the task from which the input should be taken (if from a :json:object:`Group_of_task`, this is from its map element).
  :property str output: Output name in the task provided above. Not required if the task has only one output or when referring to the map/reduce tasks of a group. [optional]
  :property boolean as_reference: Specify if the task output should be obtained as a reference (URL) or not (data directly). False is the default value if ommited. [optional]

.. note::

  The workflow executor is able obviously to assign a reference output to an expected reference input and a data output to an expected data input but will also be able to read the value of a reference output to send the expected data input. However, a data output linked to an expected reference input will yield an exception.

