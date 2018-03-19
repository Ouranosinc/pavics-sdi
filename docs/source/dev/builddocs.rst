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

Then if all went well, you should be able to build the docs (in both french and english)::

   cd pavics-sdi/docs
   mkdir source/_static
   make html

The output goes into :file:`build/en` and :file:`build/fr`. Note that there are also ``make`` targets called ``html_en`` and ``html_fr`` to build only the english or french documentation.


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

When the source documentation in english changes and the translation needs to be updated, run::

   sphinx-intl update -p build/locale

edit the ``.po`` files and rebuild the documentation.

File :file:`source/_templates/layout.html` extends the ReadTheDocs theme to add a language switcher:

.. code-block:: html

    {% block sidebartitle %}
      {{ super() }}
      <a href="/{{server_root}}/fr/{{pagename}}.html">
      <i class="fa fa-language" aria-hidden="true"></i> Français
      </a>
      |
      <a href="/{{server_root}}/en/{{pagename}}.html">
      <i class="fa fa-language" aria-hidden="true"></i> English
      </a>
    {% endblock %}


The target link is given by ``server_root``, defined in :file:`conf.py` and set to ``pavics-sdi``. The switcher will thus not work as is if deployed on another site or if the site is browsed locally. To use the switcher on your local disk, launch a simple http server (for example `http-server <https://www.npmjs.com/package/http-server>`_) inside the :file:`build` directory and create a symbolic link::

   ln -s  html pavics-sdi

The language switcher should then work.

.. _pavics-sdi: https://github.com/Ouranosinc/pavics-sdi.git







