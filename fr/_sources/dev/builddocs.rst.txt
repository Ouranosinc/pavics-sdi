=================
Building the docs
=================

To build the docs, grab a copy of the `pavics-sdi`_ repository on github::

   git clone git@github.com:Ouranosinc/pavics-sdi.git

This is the repository storing the overall system configuration for the PAVICS platform. Because processes are documented using the `autoclass` directive, you'll also need to install a few other packages that contribute services::

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

Then if all went well, you should be able to build the docs (in both french and english)::

   cd pavics-sdi/docs
   make html

The output goes into :file:`build/en` and :file:`build/fr`. Note that there are also ``make`` targets called ``html_en`` and ``html_fr`` to build only the english or french documentation.

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







