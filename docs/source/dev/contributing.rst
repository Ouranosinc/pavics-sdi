.. _contrib:

============
Contributing
============

Benchmark development environment
=================================

For debugging and editing purposes, PAVICS should be set up on a virtual machine. We recommend installing the `Oracle VM VirtualBox with Extensions <https://www.virtualbox.org/wiki/Downloads>`_ and creating a VM with the following base specifications:

- AMD64 Ubuntu Linux 16.04 Long-Term-Support (LTS) (via `Ubuntu Downloads <https://www.ubuntu.com/download/desktop>`_)
- > 8 GB RAM
- > 70 GB Storage
- > 2 CPUs
- Network bridge access
- Install VBoxGuestAdditions within the Ubuntu guest for corresponding
  VirtualBox version. This can be done via the `Devices` tab of the VM via the `Insert Guest Additions ISO image...` and following the install instruction from the ``autorun.sh`` script.

Required VM packages for various PAVICS components (most can be installed via `apt-get` with root privileges):

- python-dev
- curl `or` wget
- git
- docker.io
- docker-compose

Setting up PyCharm
==================

.. note::
	For missing python modules: https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html

The PAVICS back-end relies on developmental builds based on the Open Geospatial Consortium Web Processing Services. To install these libraries in your working environment, run the following within your PyCharm console::

    import pip
    pip.main(['install', 'https://github.com/geopython/pywps/archive/7cab3866e34ce24d3df56e3c1c546739b1cda2d7.zip'])
    pip.main(['install', '--upgrade', '--force-reinstall', 'https://github.com/bird-house/OWSLib/archive/pingudev.zip'])

.. warning::
	Some packages are not happy with Python ``wheel``, try uninstalling it if all else fails.


Launching individual local components
=====================================

Solr
----

::

    docker pull pavics/solr
    docker run --name my_solr -d -p 8983:8983 -t pavics/solr

Check that Solr is running at http://localhost:8983/solr/#/birdhouse

Public THREDDS
--------------

::

    git clone https://github.com/Ouranosinc/PAVICS.git
    cp PAVICS/birdhouse/templates/docker-compose.override.public_thredds.yml PAVICS/birdhouse/docker-compose.override.yml

In this new docker-compose.override.yml change ${PATH_TO_LOCAL_NETCDF_FILES}
to an actual path on disk with NetCDF files.

::

    docker-compose up -d thredds

Check that thredds is running at http://localhost:8083/thredds/

Secure THREDDS (HTTPS)
----------------------

First you will need a self-signed certificate:

::

    openssl req -x509 -nodes -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

This will ask for various inputs that may be left blank.

::

    cat key.pem >> cert.pem

cert.pm is your self-signed certificate.

::

    git clone https://github.com/Ouranosinc/PAVICS.git

Switch to PAVICS/birdhouse directory.

::

    ./set_hostname.sh dummy

Add this dummy hostname to /etc/hosts

::

    127.0.0.1       dummy.crim.ca

Either set SSL_CERTIFICATE to the location of cert.pem and HOSTNAME to
dummy.crim.ca or use the template docker-compose_shorcut.sh and set those
values in it (here renamed to mycompose.sh).

::

    cp PAVICS/birdhouse/templates/docker-compose.override.local_https_thredds.yml PAVICS/birdhouse/docker-compose.override.yml

In this override file specify the path to local netcdf files and set
localhost IP.

::

    ./mycompose.sh up -d thredds proxy magpie twitcher

It may take a minute for twitcher to get online. If it does not
respond after a while, try to restart everything once or twice.

::

    ./mycompose down
    ./mycompose.sh up -d thredds proxy magpie twitcher

Check that twitcher is running at https://localhost/twitcher/ (returns hello)

Check that magpie is running at https://localhost/magpie/

Check that thredds is running at https://localhost/twitcher/ows/proxy/thredds/

Play around with magpie permissions to check that the security is working

HTTPS custom WPS service
------------------------

Follow all the steps of the HTTPS THREDDS setup above up to the
template copy, instead use::

    cp PAVICS/birdhouse/templates/docker-compose.override.local_https_wps.yml PAVICS/birdhouse/docker-compose.override.yml

In this override file, set the localhost IP, then you can switch the
wpsandbox image for the wps service image of your choice and assign it
an available port of your choice. Then assign a corresponding port to
the proxy. A new proxy configuration file need to be added to
PAVICS/birdhouse/config/proxy/conf.d/wpsandbox.conf for this service,
e.g.::

    server {
        listen 8081;
        location / {
            proxy_pass http://wpsandbox;
        }
    }

::

    ./mycompose.sh up -d proxy magpie twitcher wpsandbox

It may take a minute for twitcher to get online. If it does not
respond after a while, try to restart everything once or twice.

::

    ./mycompose down
    ./mycompose.sh up -d thredds proxy magpie twitcher

Check that twitcher is running at https://localhost/twitcher/ (returns hello)

Check that magpie is running at https://localhost/magpie/

Register the new wps service in magpie: In Home > Edit Services >
wps > Add Service. In our case the name is wpsandbox and the public
url is https://dummy.crim.ca/twitcher/ows/proxy/wpsandbox with the wps
service type. Then edit this new service Protected URL to
http://dummy.crim.ca:8081

Alternatively, this can be entered in
PAVICS/birdhouse/config/magpie/providers.cfg

Check that the wps is running at https://localhost/twitcher/ows/proxy/wpsandbox/pywps?service=WPS&version=1.0.0&request=GetCapabilities

Play around with magpie permissions to check that the security is working

PAVICS-DataCatalog development
------------------------------

::

  git clone https://github.com/Ouranosinc/PAVICS-DataCatalog.git
  cd PAVICS-DataCatalog
  cp catalog.cfg ~/catalog.cfg

Edit ~/catalog.cfg with Solr address. Note that within docker, localhost
is not the same as the workstation localhost, so the address must use the ip
of the local machine (retrieve with, e.g., ifconfig). Also point to a
valid thredds server.

::

  # Docker requires root privileges
  sudo su
  docker build -t pavics-datacatalog .
  docker run --name pavics-datacatalog1 -d -v ~/catalog.cfg:/home/catalog.cfg -p 8009:80 pavics-datacatalog

Check that the wps is running at http://localhost:8009/pywps?service=WPS&request=GetCapabilities&version=1.0.0

Note that when running with magpie, the root directory of thredds does not
properly redirect to the proxy. To crawl a thredds server with threddsclient,
provide the birdhouse root directory of thredds (e.g. in catalog.cfg)::

    https://localhost/twitcher/ows/proxy/thredds/catalog/birdhouse

Flyingpigeon development
------------------------

::

    git clone https://github.com/Ouranosinc/flyingpigeon.git
    cd flyingpigeon
    git checkout pavics

Need to either add a custom.cfg or modify profiles/base.cfg with::

    [settings]
    geoserver = http://host:port/geoserver/wfs

Then proceed with installation::

    make clean install
    make test
    make start

The WPS will be running at::

    http://localhost:8093/wps?service=WPS&version=1.0.0&request=GetCapabilities

To restart flyingpigeon (e.g. after modifications)::

    make stop
    make start

Malleefowl development
----------------------

::

    git clone https://github.com/Ouranosinc/malleefowl.git
    cd malleefowl
    git checkout pavics

Need to either add a custom.cfg or modify profiles/base.cfg with::

    [settings]
    persist-path = /tmp
    archive-root = /

Then proceed with installation::

    make clean install
    make test
    make start

The WPS will be running at::

    http://localhost:8091/wps?service=WPS&version=1.0.0&request=GetCapabilities
