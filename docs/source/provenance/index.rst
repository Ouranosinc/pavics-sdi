==========
Provenance
==========

Software
--------
The PAVICS platform relies on a number of independent components, each with its own release schedule. Each component that Ouranos and CRIM maintain is stored in an individual github repository, where every change of the master branch triggers a test suite run. Development occurs in code branches, and modifications are only merged after code reviews have been completed and all tests passed. Official releases are tagged after significant code changes and are authorized by each library's maintainer.

These releases are then deployed by updating the version of the docker image loaded by docker-compose in `birdhouse-deploy`_. Relevant changes are described in file :file:`CHANGES.md`. Pull requests trigger a test suite, where documentation and tutorial notebooks are executed against the platform and compare results with expected outputs.


.. todo::

   Review by CRIM.


_`birdhouse-deploy`: https://github.com/bird-house/birdhouse-deploy

