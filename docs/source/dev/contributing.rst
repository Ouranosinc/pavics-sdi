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

Commands to run in Python console:

::

    import pip
    pip.main(['install', 'https://github.com/geopython/pywps/archive/7cab3866e34ce24d3df56e3c1c546739b1cda2d7.zip'])
    pip.main(['install', 'https://github.com/bird-house/OWSLib/archive/pingudev.zip'])


Launching individual local components
=====================================

Public THREDDS
--------------

::

    git clone https://github.com/Ouranosinc/PAVICS.git
    cp PAVICS/birdhouse/templates/docker-compose.override.public_thredds.yml PAVICS/birdhouse/docker-compose.override.yml

In this new docker-compose.override.yml change ${PATH_TO_LOCAL_NETCDF_FILES}
to an actual path on disk with NetCDF files.

::

    docker-compose up -d thredds

Check that thredds is running at localhost:8083/thredds/

HTTPS THREDDS
-------------

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

HTTPS CUSTOM WPS SERVICE
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