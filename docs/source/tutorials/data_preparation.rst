==============================================
Data preparation for inclusion in the platform
==============================================

NetCDF files
============

File conventions
----------------

NetCDF files integrated in the PAVICS platform must follow the CF Conventions
document: http://cfconventions.org/

In order to benefit from the search engine capabilities, typical global
attributes should be set. Currently the platorms searches the following
fields::

    project
    institute
    model
    experiment
    frequency

For variables, the standard_name and units should follow the CF standard name
table: http://cfconventions.org/standard-names.html

It is recommended to provide a dataset_id as a global attribute
in each NetCDF file that is unique for each collection of files that constitute
a timeseries.

NetCDF files with multiple variables are presently not fully supported.
