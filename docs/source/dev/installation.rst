============
Installation
============

.. note::
	PAVICS is built to work within POSIX and POSIX-like systems (e.g. Unix/Linux). For Windows users who want to administer a PAVICS data server, you may need to either install `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`_, a Unux/Linux virtual machine or use a POSIX API environment like the `Windows Subsytem for Linux <https://docs.microsoft.com/en-us/windows/wsl/about>`_ or `Cygwin <https://cygwin.com/>`_ to interface with the PAVICS server system.


Deployment methods
==================

PAVICS can be installed from source on `GitHub <https://www.github.com/Ouranosinc/pavics-sdi/>`_ or by using `Docker <https://www.docker.com/what-docker>`_. Git/Github is a versioning software and platform that can fetch development branches of pavics while Docker is a virtualization tool for running isolated service images built with specific library environments. Depending on your needs and interests (e.g. debugging vs deploying) either platform may suit your needs. 

Proposing changes to PAVICS or :ref:`contrib` requires free a `GitHub account <https://github.com/join>`_ but anyone can download the source code for PAVICS withour registering. Git is normally in most standard Linux software repositories and can be installed (using Debian/Ubuntu-based systems) with the following::
  
  # Enable root access
  sudo su

  # Updating software catalogues and and installed libraries
  apt-get update; sudo apt-get upgrade

  # Installing git will also install dependent libraries 
  apt-get install -y git

  # Configuring git for code commits using your user credentials
  exit # Leave superuser
  git config --global user.name "Your Name"
  git config --global user.email "youremail@domain.com"


For Docker installations, begin by following the guide for installing ``Docker Community Edition`` on your home machine from the `Docker Installation Page <https://docs.docker.com/install/>`_. Docker Community Edition is a set of command line tools for creating and launching container-based applications.

Depending on your Linux distribution, you can either download and launch the installer directly or you may need to add a new ppa/apt/yum/dnf/etc. software repository to your system to install the most recent version. For Debian/Ubuntu-based systems::

  # Enable root access  
  sudo su

  # Install base library requirements
  apt-get install -y apt-transport-https ca-certificates wget software-properties-common

  # Install the Docker suite of tools
  apt-get install -y docker docker.io docker-engine 

For users not using Linux, refer to the following installation guides for `Mac OS <https://docs.docker.com/docker-for-mac/>`_ and for `Windows <https://docs.docker.com/docker-for-windows/>`_.

PAVICS and Dockerhub images
===========================

All code produced for the PAVICS project is Open Source and hosted publicly through GitHub repositories. Among our members/users, the preferred method for packaging and deployment relies on Docker images. As such, we use the Docker Image building and hosting features of `DockerHub`_. This feature automatically builds a new image for all major releases to the GitHub repository, for all repositories that include a ``Dockerfile``. The `resulting images <https://hub.docker.com/u/pavics/>`_ are all publicly available for distribution and deployment. Any PAVICS Docker image can be obtained using the following command::

   docker pull pavics/[image_name]

Most of the code base for PAVICS is forked from the `Birdhouse Project <https://birdhouse.readthedocs.io/en/latest/index.html>`_ which already has multiple DockerHub `build processes <https://hub.docker.com/u/birdhouse>`_. Using our own DockerHub build gives us the advantage of having our own upstream build process for the code being modified by CRIM / Ouranos. Many of the modifications to these birdhouse components are merged upstream, but some are specific to the PAVICS project and we felt it was worthwhile to maintain an independent build process.


PAVICS installation with `docker-compose`
===========================================

.. todo:: 
	Base PAVICS installation is incomplete. The following lines refer to Phoenix instance. Need to specify which birds are needed for a bare installation of PAVICS: Phoenix, FlyingPigeon, Malleefowl, Emu, etc.

First mount or create a symlink for the datasets storage at ``/data``.
Mount or make a symlink for the geoserver data storage so that ``/geoserver_data`` could be used (read/write) by geoserver.

To install the suite of docker images you must use `docker-compose <https://docs.docker.com/compose/>`_. Docker-compose is a docker helper for coordinating multiple docker images at once. Docker-compose exists in most Linux software repositories but can also be installed using ``pip`` or ``conda``. Depending on your Linux distribution and whether you have Anaconda/miniconda installed, run any of the following::
  
  # For standard libraries (Ubuntu/Debian)
  sudo apt-get install docker-compose

  # For system-installed Python2 or Python3 (requires sudo)
  sudo apt-get install -y python-dev python3-dev
  sudo -H pip install docker-compose

  # For Anaconda/miniconda (Python2 or Python3)
  conda install docker-compose

.. note:: 
	Presently, the main ``PAVICS`` repo is closed to the public while it is under heavy development

After installing docker-compose, clone the PAVICS repository and navigate to the docker *build recipe* within `PAVICS`_::

  # Cloning the PAVICS repository
  git clone https://github.com/Ouranosinc/PAVICS.git
  cd pavics-sdi/birdhouse
  # Open the docker-compose.yml using a text editor
  nano docker-compose.yml

.. note::
	The :file:`docker-compose.yml` contains many of the setup configurations needed to successfully launch Birdhouse. Be sure to read the :ref:`config` and the :ref:`load_balancing` suggestions before continuing the installation.

After modifying the necessary variables in the :file:`docker-compose.yml` file, simply run the following command, taking care to select an appropriate host name::

   HOSTNAME='<public-ip>' bash -c 'docker-compose up -d'

This installation will run on a single server instance, but there are instructions for :ref:`load_balancing`.


Updating containers to the latest version
=========================================

To synchronize a deployment with the latest container available on dockerhub::

   # Set working directory where the docker-compose.yml is located. Usually :
   cd ~/PAVICS/birdhouse

   # Docker requires root privileges
   sudo su

   # Pull the latest containers (container_name is optional but can limit the operation to only one container rather than applying to all containers)
   HOSTNAME='<public-ip>' bash -c 'docker-compose pull [container_name]'

   # Stopping containers
   HOSTNAME='<public-ip>' bash -c 'docker-compose stop [container_name]'

   # Start again containers (-d is for detached, avoid it to get all output to the command line)
   HOSTNAME='<public-ip>' bash -c 'docker-compose up -d [container_name]'

.. note:: 
	``container_name`` is the name chosen in the docker-compose.yml, not the name of the docker image.


Resetting Bird services
=======================

If a Bird Service becomes unusable, the docker containers can easily be reset to default settings::

   # Docker requires root privileges
   sudo su

   # Stopping and removing containers (this will flush their states)
   HOSTNAME='<public-ip>' bash -c 'docker-compose down'

   # Start again containers (-d is for detached, avoid it to get all output to the command line)
   HOSTNAME='<public-ip>' bash -c 'docker-compose up -d'

.. note::
	Some manual tasks are required after resetting the birdhouse environment : See the manual steps under the Phoenix configuration

Restarting Bird services
========================

If the dockers containers need to be stopped (including the docker service, if required) these steps will preserve the docker state and all configurations set via Bird Service web portals::

   # Docker requires root privileges
   sudo su

   # Stopping running containers
   HOSTNAME='<public-ip>' bash -c 'docker-compose stop'

   # Stopping the docker service
   service docker stop

Restarting Bird Services (required after restarting the host vm)::

   # Docker requires root privileges
   sudo su

   # Starting the docker service
   service docker start

   # Starting the birdhouse containers
   HOSTNAME='<public-ip>' bash -c 'docker-compose start'


Port specification
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

.. _PAVICS: https://github.com/Ouranosinc/PAVICS.git
.. _Docker: http://docker.com
.. _DockerHub: https://hub.docker.com/
.. _ipython:  https://ipython.org

.. todo::
   Update the installation and config with security changes