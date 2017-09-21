===============
Using workflows
===============

Creating a climate product usually involves multiple steps:

#. Selecting datasets
#. Subsetting the data to a specific region and period
#. Either regridding the multiple datasets to a common grid or computing spatial averages
#. Computing climate indices
#. Create graphs or tables from the results

Typically each step would involve calling one or many individual processes, and it's convenient to combine these steps into a *workflow*. Here we use *workflow* to mean a formal description of the logical organization and ordering of individual processes. The workflow logic is encapsulated in a ``json`` file using a vocabulary (called a `schema <http://json-schema.org>`_) that we describe below.


Workflow vocabulary
===================

