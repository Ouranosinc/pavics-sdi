=================
Building the docs
=================

To build the docs, grab a copy of the `pavics-sdi`_ repository on github::

   git clone git@github.com:Ouranosinc/pavics-sdi.git

This is the repository storing the overall system configuration for the PAVICS platform. Because processes are documented using the `autoprocess` directive, you'll also need to install a few other packages that contribute services::

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

There are other requirements (sphinx and a few extensions) that can be installed using pip::

   pip install -r requirements.txt

Then if all went well, you should be able to build the docs::

   cd pavics-sdi/docs
   make html

If you have write permissions to `pavics-sdi`_, you can also deploy the html `online <https://ouranosinc.github.io/pavics-sdi/>`_::

   make gh-pages

but this requires creating a build directory according to these `instructions <https://daler.github.io/sphinxdoc-test/includeme.html>`_.


Translations
============

`pavics-sdi`_ is being translated in french, and it's possible to add other languages. For example to add a german translation,  run ``sphinx-intl`` from the :file:`docs/` directory with the ``de`` locale::

   sphinx-intl update -p build/locale -l de

This will create a :file:`locale/de/LC_MESSAGES` folder storing ``.po`` files.

Translators will then be able to edit those ``.po`` files to translate the documentation content. Once that's done, the documentation can be compiled using::

   make -e SPHINXOPTS="-D language='de'" html


A ``make`` command to build the french documentation has been created to facilitate building::

   make html_fr

When the source documentation in english changes and the translation needs to be updated, run::

   sphinx-intl update -p build/locale

edit the ``.po`` files and rebuild the documentation.




.. _pavics-sdi: https://github.com/Ouranosinc/pavics-sdi.git







