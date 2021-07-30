Pavics-DataCatalog 
==================

PAVICS-SDI bundles a number of cataloguing services that allow users to search for and add data to its backend catalog service. 

The main cataloguing component within the PAVICS-SDI architecture is `PAVICS-DataCatalog <https://www.github.com/ouranosinc/PAVICS-DataCatalog/>`_, a service that identifies and enables querying of `CF-compliant <http://cfconventions.org/>`_ climate data organized within THREDDS Data Servers. PAVICS-DataCatalog is built with the `Apache Solr <https://lucene.apache.org/solr/>`_ search platform.

PAVICS Catalogue Search
-----------------------
The ``pavicssearch`` service closely mimics the API for the Earth System Grid Federation (ESGF) search. The search fields (or *facets*) include author, category, cf_standard_name, experiment, frequency, institute, model, project, source, subject, title, units, variable and variable_long_name. The search results are returned in a ``json`` file and include the URL to download the file or access it through DAP.

Examples
--------
The following request will launch the crawler on the server filesystem to catalog available data::

  http://localhost:8009/pywps?service=WPS&request=execute&version=1.0.0&identifier=pavicrawler&storeExecuteResponse=true&status=true&DataInputs=

The following request will search for all files that are part of the RCP8.5 experiment and based on the CRCM4 model::
 
  http://localhost:8009/pywps?service=WPS&request=execute&version=1.0.0&identifier=pavicsearch&DataInputs=constraints=model:CRCM4,experiment:rcp85

PAVICS Catalogue Credits
------------------------
PAVICS-DataCatalog is developed by researchers at CRIM and Ouranos.
