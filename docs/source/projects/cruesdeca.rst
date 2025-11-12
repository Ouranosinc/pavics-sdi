Flood Frequency Analysis and Dam Safety in the 21st Century Climate
===================================================================

:ref:`Version en français<Analyse de fréquence des crues et sécurité des barrages dans le climat du 21e siècle>`


This project completed in March 2021 looked at how climate change information can be integrated into flood design values estimated by frequency analysis. The `report`_ includes maps showing the relative change in 1,000 and 10,000 return values for over 500 watersheds over Canada, comparing the 2080-2100 period to 1990-2010. The data underlying these figures is available online as a geospatial layer named ``public:decamillenial_flood_CC`` on the `Ouranos GeoServer <pavics.ouranos.ca/geoserver>`. This layer can be downloaded locally, streamed by GIS client (see instructions below) or accessed programmatically (see notebook_).

For each watershed, the results include the following properties:

name
    Watershed name
watershed_area
    Surface area (km²)
NSE
    Nash-Sutcliffe Efficiency of calibrated model
``<gcm>_PWM_<t>_[<p>_]<kind>``
    Climate change factor per unit area (mm/d/km²) computed following these specifications:

    - ``gcm``: Climate model, one of CESM1, CanESM2
    - *Probability Weighted Moments* calibration method
    - ``t``: return period, one of 1000, 10000
    - ``kind``: Factor operation, either additive (+), or multiplicative (*)
    - ``p`` (*optional*): percentile from bootstrap parameter uncertainty assessment, one of 0.75, 0.9, 0.95 or 0.99. If not present, the result is the direct estimate from the PWM method on the full sample.

.. warning::

    The ESRI Shapefile format limits field names to 10 characters. The column names above are thus truncated and replaced by an index (e.g. `CanESM2_18`), which complicates parsing. We recommend using the GeoPackage format when downloading the results.


QGIS Client Instructions
------------------------

.. note::

    These instructions were written for QGIS version 3.10.

#. Add a layer using the Web Feature Services (WFS) standard
   :guilabel:`Layer` -> :guilabel:`Add Layer` -> :guilabel:`Add WFS Layer ...`
#. Click on :guilabel:`New`
#. Enter the name and address of the PAVICS GeoServer
   :guilabel:`Name`: PAVICS
   :guilabel:`URL`: https://pavics.ouranos.ca/geoserver/ows?version=1.1.0&
#. Click :guilabel:`OK`
#. Click :guilabel:`Connect`
#. In table, select ``decamillenial_flood_CC``
#. Click :guilabel:`Add`,  the layer will be downloaded and should appear in the :guilabel:`Layers` widget.
#. Click :guilabel:`Close`

Once the layer is available, you can access the various columns of the data table and display them.

#. Right click on ``decamillenial_flood_CC`` layer, select :guilabel:`Properties`
#. In left menu, select :guilabel:`Symbology`
#. In top right menu, select :guilabel:`Graduated`
#. On next line, pick the value to display.
#. Modify as needed the legend format, color ramp and number of classes.
#. Click :guilabel:`Classify`
#. Click :guilabel:`Apply` then :guilabel:`OK`.

.. _report: https://www.ouranos.ca/wp-content/uploads/FrigonKoenig_2021_FloodFreqAnalDamSafetyCC_EN.pdf
.. _notebook: notebooks/cruesdeca.ipynb

Analyse de fréquence des crues et sécurité des barrages dans le climat du 21e siècle
====================================================================================

Ce projet complété en mars 2021 s'intéresse à l'intégration des projections climatiques dans l'estimation des crues de conception estimée par analyse fréquentielle. Le `rapport` présente des cartes illustrant le changement relatif des crues de temps de retour 1:1,000 et 1:10,000 pour plus de 500 bassins versants au Canada, comparant la période 2080-2100 à celle de 1990-2010. Les données utilisées pour créer ces cartes sont disponibles sous forme de couches géospatiales ( ``public:decamillenial_flood_CC``) sur le `GeoServer d'Ouranos <pavics.ouranos.ca/geoserver>`. Ces couches peuvent être téléchargées manuellement, via un client SIG (voir instructions plus bas), ou accédées par une interface de programmation (voir notebook_, en anglais).

Pour chaque bassin versant, le tableau de résultats incluent les colonnes suivantes:

name
  Nom du bassin versant
watershed_area
  Superficie (km²)
NSE
  Nash-Sutcliffe Efficiency (NSE) du modèle hydrologique
``<gcm>_PWM_<t>_[<p>_]<kind>``
  Facteur de changement climatique de la crue par unité de surface (mm/d/km²) calculé selon les paramètres suivants:

  - ``gcm``: Modèle de climat, soit CESM1 ou CanESM2
  - *Probability Weighted Moments* méthode de calibration des paramètres de la GEV
  - ``t``: période de retour, soit 1000 ou 10000
  - ``kind``: Type d'opération à effectuer pour appliquer le facteur de changement, soit une addition (+), ou une multiplication (*)
  - ``p`` (*optional*): percentile estimé par *bootstrap* , l'un de 0.75, 0.9, 0.95 or 0.99. Si `p` est absent, les résultats sont une estimation directe des paramètres par PWM, sans *bootstrap*.

.. warning::

   Le format *shapefile* limite les noms de colonnes à 10 caractères. Les noms de colonnes décrit plus haut sont donc tronqués et remplacés par un nombre (e.g. `CanESM2_18`), ce qui rend les résultats inintelligibles. On recommande utiliser le format `GeoPackage` pour télécharger les résultats.


Instructions pour QGIS
-----------------------

#. Ajouter une couche de type *Web Feature Services* (WFS)
   :guilabel:`Couche` -> :guilabel:`Ajouter une couche` -> :guilabel:`Ajouter une couche WFS ...`
#. Cliquer sur :guilabel:`Nouveau`
#. Entrer le nom et l'adresse URL du Geoserver de PAVICS
   :guilabel:`Name`: PAVICS
   :guilabel:`URL`: https://pavics.ouranos.ca/geoserver/ows?version=1.1.0&
#. Cliquer :guilabel:`OK`
#. Cliquer :guilabel:`Connexion`
#. Dans les résultats, selectionner ``decamillenial_flood_CC``
#. Cliquer :guilabel:`Ajouter`, la couche devrait être téléchargée et apparaître dans le menu :guilabel:`Couches`.
#. Cliquer :guilabel:`Fermer`

Une fois la couche ajoutée, les différentes colonnes de la table de données peuvent être affichées.

#. Cliquer sur la couche ``decamillenial_flood_CC`` avec le bouton droit, sélectionner :guilabel:`Propriétés`
#. Dans le menu de gauche, sélectionner :guilabel:`Symbologie`
#. Dans le menu de droite, en haut complètement, sélectionner :guilabel:`Gradué`
#. À la ligne suivante choisissez la variable à illustrer.
#. Choisir au besoin le format de légende, la palette de couleur et le nombre de classes.
#. Cliquer sur :guilabel:`Classer`
#. Cliquer sur :guilabel:`Appliquer`, puis :guilabel:`OK`

.. _rapport: https://www.ouranos.ca/wp-content/uploads/FrigonKoenig_2021_FloodFreqAnalDamSafetyCC_FR.pdf
