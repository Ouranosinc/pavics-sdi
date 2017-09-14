===========================
Installation and Deployment
===========================

Since all of the code produced for the PAVICS project is hosted on public GitHub repositories, and that the preferred methodology for packaging and deployment uses Docker images, we set out to use the automatic Docker Image building feature of `DockerHub`_. This feature automatically builds a new image for every push to the GitHub repository for all given branches, given that these repositories have a Dockerfile. The `resulting images <https://hub.docker.com/u/pavics/>`_ are all publicly available for container execution and sharing of our work. Any docker image can be obtained using the following command::

   docker pull pavics/pavics-datacatalog

Most of the code base has been forked from the Birdhouse project which already has multiple DockerHub `build processes <https://hub.docker.com/u/birdhouse>`_. Using our own DockerHub builds gives us the advantage of having our own upstream build process for the code being modified by CRIM / Ouranos. Many of the modifications to these birdhouse components are merged upstream, but some are specific to the PAVICS project and we felt it was worthwhile to have this independent build process.

Installation using ``docker-compose``
=====================================

Let's assume that you have a LinuxOS with `Docker`_ (>1.10) installed.
First mount or create a symlink for for the datasets storage at ``/data``.
Mount or make a symlink for the geoserver data storage so that ``/geoserver_data`` could be used (read/write) by geoserver
A full install of the PAVICS platform would start by downloading the images for all the components, but instead of doing this manually, we use `docker-compose <https://docs.docker.com/compose/>`_::

   sudo pip install docker-compose

Then get the build recipe from `pavics-sdi`_::

   git clone https://github.com/Ouranosinc/pavics-sdi.git
   cd pavics-sdi/birdhouse

In the file :file:`docker-compose.yml`, within the ``phoenix/volumes`` configuration, set the environment variable SSL_CERTIFICATE  to a valid certificate. The certificate file should contain both the CERTIFICATE and PRIVATE KEY parts as required by the nginx "ssl_certificate_key" and "ssl_certificate" parameters.

Then simply run the following command, taking care to select an appropriate host name::

   HOSTNAME='boreas.ouranos.ca' bash -c 'docker-compose up -d'


Updating container to the latest version
========================================

To synchronize a deployment with the latest version of container available on dockerhub::

   # Set working directory where the docker-compose.yml is located. Usually :
   cd ~/pavics-sdi/birdhouse

   # Docker required sudo access
   sudo su

   # Pull the latest containers (container_name is optional but can limit the operation to only one container rather than applying to all containers)
   HOSTNAME='<public-ip>' bash -c 'docker-compose pull [container_name]'

   # Stopping containers
   HOSTNAME='<public-ip>' bash -c 'docker-compose stop [container_name]'

   # Start again containers (-d is for detached, avoid it to get all output to the command line)
   HOSTNAME='<public-ip>' bash -c 'docker-compose up -d [container_name]'

.. note:: ``container_name`` is the name chosen in the docker-compose.yml, not the name of the docker image.


Resetting the birdhouse dockers
===============================

If the VM became unusable the docker containers can easily be reset to default::

   # Docker required sudo access
   sudo su

   # Stopping and removing containers (this will flush their states)
   HOSTNAME='<public-ip>' bash -c 'docker-compose down'

   # Start again containers (-d is for detached, avoid it to get all output to the command line)
   HOSTNAME='<public-ip>' bash -c 'docker-compose up -d'

  Some manual tasks are required after resetting the birdhouse environment : See the manual steps under the Phoenix configuration

Restarting the birdhouse dockers
================================

If the dockers containers need to be stopped (including the docker service if required). These steps will preserve the docker state and thus all configurations done using the web sites::

   # Docker required sudo access
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



Ports
=====

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


Individual Components Configuration
===================================


Phoenix
-------

.. code-block:: bash
   :caption: :file:`/config/phoenix/custom.cfg`

   [settings]
   # User: admin, Password: querty
   phoenix-password = sha256:...

To change password get into the phoenix running container and use ``make passwd``. This will update the persistant host :file:`custom.cfg` with the new password hash.
If an error about missing ``IPython.lib`` occurs install `ipython`_ like this::

   source $ANACONDA_HOME/bin/activate birdhouse
   pip install ipython

Phoenix still need manual configuration so SOLR indexes correctly the TREDDS catalog. Here are the steps:


.. _pavics-sdi: https://github.com/Ouranosinc/pavics-sdi.git
.. _Docker: http://docker.com
.. _DockerHub: https://hub.docker.com/
.. _ipython:  https://ipython.org
