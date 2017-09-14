=================
Building the docs
=================

To build the docs, grab a copy of the `pavics-sdi`_ repository on github::

   git clone git@github.com:Ouranosinc/pavics-sdi.git

This is the repository storing the overall system configuration for the PAVICS platform. Because processes are documented using the `autoclass` directive, you'll also need to install a few other packages that constribute services to PAVICS::

    git clone git@github.com:Ouranosinc/flyingpigeon.git
    cd flyingpigeon
    make clean install
    cd ..

    git clone git@github.com:Ouranosinc/malleefowl.git
    cd malleefowl
    make clean install
    cd ..

    git clone https://github.com/bird-house/hummingbird.git
    cd hummingbird
    make clean install
    cd ..

    git clone git@github.com:Ouranosinc/PAVICS-DataCatalog.git
    cd PAVICS-Datacatalog
    python setup.py install
    cd ..

Then if all went well, you should be able to build the docs::

   cd pavics-sdi/docs
   make html

If you have write permissions to `pavics-sdi`_, you can also deploy the html `online <https://ouranosinc.github.io/pavics-sdi/>`_::

   make gh-pages

but this requires creating a build directory according to these `instructions <https://daler.github.io/sphinxdoc-test/includeme.html>`_.


.. _pavics-sdi: https://github.com/Ouranosinc/pavics-sdi.git







