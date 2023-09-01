=================
Building the docs
=================

These docs are automatically built by ReadTheDocs, but can also be built locally.

To build the docs, grab a copy of the `pavics-sdi`_ repository on github::

  git clone https://github.com/Ouranosinc/pavics-sdi.git

There are requirements (sphinx and a few extensions) that can be installed using `pip`::

   pip install -r requirements.txt

After installing these libraries, you should be able to build the docs without errors::

   cd pavics-sdi/docs
   mkdir source/_static
   make html


Translations
------------

`pavics-sdi`_ is also being translated to French, and it's possible to add other languages. For example to add a German translation,  run ``sphinx-intl`` from the :file:`docs/` directory with the ``de`` locale::

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
