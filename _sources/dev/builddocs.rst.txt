=================
Building the docs
=================

To build the docs, grab a copy of the `pavics-sdi`_ repository on github::

   git clone git@github.com:Ouranosinc/pavics-sdi.git

This is the repository storing the overall system configuration for the PAVICS platform. Because processes are documented using the `autoprocess` directive, you'll also need to install a few other packages that contribute services::

    git clone git@github.com:Ouranosinc/flyingpigeon.git
    cd flyingpigeon
    git checkout pavics
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
   mkdir source/_static
   make html



Publishing the docs online
--------------------------

If you have write permissions to `pavics-sdi`_, you can also deploy the html `online <https://ouranosinc.github.io/pavics-sdi/>`_.
To do so for the first time, create a new directory next to the :file:`pavics-sdi` directory and clone the repo into an :file:`html` directory::

   mkdir pavics-sdi-docs
   cd pavics-sdi-docs
   git clone git@github.com:Ouranosinc/pavics-sdi.git html

Then enter :file:`html`, checkout the `gh-pages` branch and enter some voodoo incantations::

   cd html
   git checkout gh-pages
   git symbolic-ref HEAD refs/heads/gh-pages  # auto-switches branches to gh-pages
   rm .git/index
   git clean -fdx

You'll also need to add a :file:`.nojekyll` file to make sure the stylesheets are loaded on github.io::

   git add .nojekyll
   git commit -m 'added .nojekyll'
   git push

You should then be able to go back to pavics-sdi/docs and run make `gh-pages`, which will build the html docs,
copy them to the :file:`pavics-sdi-docs` just created and push them to the github gh-branch::

   make gh-pages

For more details, see the original `instructions <https://daler.github.io/sphinxdoc-test/includeme.html>`_.








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







