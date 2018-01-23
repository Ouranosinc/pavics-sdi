============
Contributing
============

Benchmark development environment
=================================

Recommended VirtualBox installation:

- Install Oracle VM VirtualBox Extension Pack
- Linux Ubuntu 16.04.3 (64-bit)
- >8 gb memory
- >70 gb disk space
- >2 CPUs
- Network bridge access
- Install VBoxGuestAdditions inside the Ubuntu guest for corresponding
  VirtualBox version

Required packages for various PAVICS components:

git docker.io docker-compose


Setting up pycharm
==================

- May need to uninstall wheel
- For missing python modules: https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html

Commands to run in Python console::

    import pip
    pip.main(['install', 'https://github.com/geopython/pywps/archive/7cab3866e34ce24d3df56e3c1c546739b1cda2d7.zip'])
    pip.main(['install', 'https://github.com/bird-house/OWSLib/archive/pingudev.zip'])


Launching individual local components
=====================================

Public THREDDS
--------------

::

    git clone https://github.com/Ouranosinc/PAVICS.git

Copy PAVICS/birdhouse/templates/docker-compose.override.public_thredds.yml
to docker-compose directory (PAVICS/birdhouse/) as docker-compose.override.yml
and specify the path to local netcdf files::

    docker-compose up -d thredds

Check that thredds is running at localhost:8083/thredds/

HTTPS THREDDS
-------------

First you will need a self-signed certificate::

    openssl req -x509 -nodes -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

This will ask for various inputs that may be left blank::

    cat key.pem >> cert.pem

cert.pm is your self-signed certificate::

    git clone https://github.com/Ouranosinc/PAVICS.git

Switch to PAVICS/birdhouse directory::

    ./set_hostname.sh dummy

Either set SSL_CERTIFICATE to the location of cert.pem and HOSTNAME to
dummy.crim.ca or use template docker-compose_shorcut (here renamed to
mycompose.sh). Copy
PAVICS/birdhouse/templates/docker-compose.override.local_https_thredds.yml to
docker-compose directory (PAVICS/birdhouse/) as docker-compose.override.yml and
specify the path to local netcdf files and set localhost IP::

    ./mycompose.sh up -d thredds proxy magpie twitcher

Check that twitcher is running at https://localhost/twitcher/ (returns hello)

Check that magpie is running at https://localhost/magpie/

Check that thredds is running at https://localhost/twitcher/ows/proxy/thredds/

Play around with magpie permissions to check that the security is working
