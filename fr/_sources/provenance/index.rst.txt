==========
Provenance
==========

The code base is divided into multiple components each having its own release schedule. Each component is stored on a
individual github repository, where every change of the master branch triggers a test suite run and a build of the
corresponding docker image (available on `DockerHub`_). Development occurs in code branches, and modifications are only
merged after code reviews have been completed and all tests passed. Official releases are tagged after significant code
changes and are authorized by ?. The project documentation is entirely contained within the various sections of this
document.

pavics-sdi is relying on a number of different packages developed by other teams. Minor pavics releases will be created following major releases of these critical third party packages if they do not coincide with a major internal release. Package whose upgrade whose trigger a minor pavics release include ocgis, flyingpigeon and malleefowl.

Ouranos deployment
------------------
A pre-release version is deployed on an experimental server and integration testing is performed to make sure the platform is in working order. If everything is in order, the pre-release version becomes the release version and is deployed on the pavics server.



.. todo::

   Review by CRIM.



.. _DockerHub: https://hub.docker.com/