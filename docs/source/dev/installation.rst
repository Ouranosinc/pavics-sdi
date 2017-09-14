===========================
Installation and Deployment
===========================

Here we'll cover two cases: a local installation for development and testing, and a full installation of all the components from their `docker`_ containers.


Installation from docker containers
===================================

Since all of the code produced for the PAVICS project is hosted on public GitHub repositories, and that the preferred methodology for packaging and deployment uses Docker images, we set out to use the automatic Docker Image building feature of DockerHub. This feature automatically builds a new image for every push to the GitHub repository for all given branches, given that these repositories have a Dockerfile. The `resulting images <https://hub.docker.com/u/pavics/>`_ are all publicly available for container execution and sharing of our work. Any docker image can be obtained using the following command::

   docker pull pavics/pavics-datacatalog

Most of the code base has been forked from the Birdhouse project which already has multiple `DockerHub build processes <https://hub.docker.com/u/birdhouse/`_. Using our own DockerHub builds gives us the advantage of having our own upstream build process for the code being modified by CRIM / Ouranos. Many of the modifications to these birdhouse components are merged upstream, but some are specific to the PAVICS project and we felt it was worthwhile to have this independent build process.

Let's assume that you have a LinuxOS with Docker (>1.10) installed.
First mount or create a symlink for for the datasets storage at ``/data``.
Mount or make a symlink for the geoserver data storage so that ``/geoserver_data`` could be used (read/write) by geoserver
A full install of the PAVICS platform would start by downloading the images for all the components, but instead of doing this manually, we use `docker-compose <https://docs.docker.com/compose/>`_::

   sudo pip install docker-compose

Then get the build recipe from `pavics-sdi`_::

   git clone https://github.com/Ouranosinc/pavics-sdi.git
   cd pavics-sdi/birdhouse

In the file ``docker-compose.yml``, within the ``phoenix/volumes`` configuration, set the environment variable SSL_CERTIFICATE  to a valid certificate. The certificate file should contain both the CERTIFICATE and PRIVATE KEY parts as required by the nginx "ssl_certificate_key" and "ssl_certificate" parameters.

Then simply run the following command, taking care to select an appropriate host name::

   HOSTNAME='boreas.ouranos.ca' bash -c 'docker-compose up -d'


Ports
-----
The ``docker-compose.yml`` config exposes ports for each docker container (left part is the public one, right part the container internal one). We try to respect the following convention::

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









.. _docker: http://docker.com