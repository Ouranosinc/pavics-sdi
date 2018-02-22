============
Installation
============

.. todo::
   Update the installation and config with security changes

All code produced for the PAVICS project is Open Source and hosted publicly through GitHub repositories. Among our members/users, the preferred methodology for packaging and deployment relies on Docker images, as such we employ the automatic Docker Image building feature of `DockerHub`_. This feature automatically builds a new image for every push to the GitHub repository for all given branches, for all repositories that include a ``Dockerfile``. The `resulting images <https://hub.docker.com/u/pavics/>`_ are all publicly available for container execution and distribution. Any docker image can be obtained using the following command::

   docker pull pavics/pavics-datacatalog

Most of the code base has been forked from the Birdhouse project which already has multiple DockerHub `build processes <https://hub.docker.com/u/birdhouse>`_. Using our own DockerHub build gives us the advantage of having our own upstream build process for the code being modified by CRIM / Ouranos. Many of the modifications to these birdhouse components are merged upstream, but some are specific to the PAVICS project and we felt it was worthwhile to maintain an independent build process.


Docker Resources
================

Begin by following the guide for installing ``Docker Community Edition`` on your home machine from <https://docs.docker.com/install/>_. Docker Community Edition is a set of command line tools for creating and launching container-based applications.

Depending on your Linux distribution, you may need to either add a new ppa/apt/yum/dnf repository to your system or you can download and launch the installer directly.

For users not using Linux, refer to the following guides for 'Mac OS <https://docs.docker.com/docker-for-mac/>'_ and for `Windows <https://docs.docker.com/docker-for-windows/>`_.


PAVICS Installation using ``docker-compose``
============================================

First mount or create a symlink for the datasets storage at ``/data``.
Mount or make a symlink for the geoserver data storage so that ``/geoserver_data`` could be used (read/write) by geoserver.

To install the suite of docker images you must use `docker-compose <https://docs.docker.com/compose/>`_. Docker-compose is a docker helper for coordinating multiple docker images at once. Run the following::

   sudo pip install docker-compose

Then get the *build recipe* from `pavics-sdi`_::

   git clone https://github.com/Ouranosinc/pavics-sdi.git
   cd pavics-sdi/birdhouse ### TO BE REVISED


.. todo:: 
	Base PAVICS installation is incomplete. The following lines refer to Phoenix instance. Need to specify which birds are needed for a bare installation of PAVICS: Phoenix, FlyingPigeon, Malleefowl, Emu, etc.

In the file :file:`docker-compose.yml`, within the `phoenix/volumes` configuration, set the environment variable SSL_CERTIFICATE  to a valid certificate. This certificate file should contain both the CERTIFICATE and PRIVATE KEY parts as required by the nginx "ssl_certificate_key" and "ssl_certificate" parameters.

Then simply run the following command, taking care to select an appropriate host name::

   HOSTNAME='boreas.ouranos.ca' bash -c 'docker-compose up -d'

This installation will run on a single server instance, but there are instructions for :ref:`load_balancing`.


Updating containers to the latest version
========================================

To synchronize a deployment with the latest container available on dockerhub::

   # Set working directory where the docker-compose.yml is located. Usually :
   cd ~/pavics-sdi/birdhouse ### TO BE REVISED 

   # Docker required sudo access
   sudo su

   # Pull the latest containers (container_name is optional but can limit the operation to only one container rather than applying to all containers)
   HOSTNAME='<public-ip>' bash -c 'docker-compose pull [container_name]'

   # Stopping containers
   HOSTNAME='<public-ip>' bash -c 'docker-compose stop [container_name]'

   # Start again containers (-d is for detached, avoid it to get all output to the command line)
   HOSTNAME='<public-ip>' bash -c 'docker-compose up -d [container_name]'

.. note:: 
	``container_name`` is the name chosen in the docker-compose.yml, not the name of the docker image.


Resetting Birdhouse
===================

If a service becomes unusable the docker containers can easily be reset to default::

   # Docker required sudo access
   sudo su

   # Stopping and removing containers (this will flush their states)
   HOSTNAME='<public-ip>' bash -c 'docker-compose down'

   # Start again containers (-d is for detached, avoid it to get all output to the command line)
   HOSTNAME='<public-ip>' bash -c 'docker-compose up -d'

  Some manual tasks are required after resetting the birdhouse environment : See the manual steps under the Phoenix configuration

Restarting Birdhouse
====================

If the dockers containers need to be stopped (including the docker service, if required) these steps will preserve the docker state and all configurations done using the websites::

   # Docker management requires sudo access
   sudo su

   # Stopping running containers
   HOSTNAME='<public-ip>' bash -c 'docker-compose stop'

   # Stopping the docker service
   service docker stop

And starting dockers (required after restarting the host vm)::

   # Docker required sudo access
   sudo su

   # Starting the docker service
   service docker start

   # Starting the birdhouse containers
   HOSTNAME='<public-ip>' bash -c 'docker-compose start'


Port Specification
==================

The :file:`docker-compose.yml` config file exposes ports for each docker container (left part is the public one, right part the container internal one). We try to respect the following convention::

   8xxx : port usually responding for the service (The HTTP port)
   28xxx: https port
   38xxx: the output port (To be documented)
   48xxx: the supervisor port of the container

Container xxx value::

   Phoenix : 443 (With 8081 as http and 8443 as https)
   Malleefowl : 091
   Flyingpigeon : 093
   Emu : 094
   Solr : 983 (No https or output ports)
   ncWMS2 : 080 (No https or output ports)
   thredds : 083 (No https or output ports)
   pavics-catalog : 086 (No https or output ports)
   geoserver : 087 (No https or output ports)

The exception is the Pavics-frontend, which has port 3000.

.. _pavics-sdi: https://github.com/Ouranosinc/pavics-sdi.git
.. _Docker: http://docker.com
.. _DockerHub: https://hub.docker.com/
.. _ipython:  https://ipython.org

