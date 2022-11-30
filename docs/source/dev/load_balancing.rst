.. _load_balancing:

==============
Load balancing
==============

Here we'll cover the case where pavics-sdi is installed on more than one machine and you want to balance the load across these machines. This is done with `NGINX`_ and requires modifications to :file:`docker-compose.yml` and creating a configuration file for the `NGINX`_ server.

Modifying the :file:`docker-compose.yml`
========================================

To enable load balancing, we need a proxy to redirect requests to machines according to their usage. This is done by mapping proxy ports (5XXXX) to the *service* ports, such as those of flyingpigeon (8093) and malleefowl (8091).

.. code-block:: bash
   :caption: :file:`docker-compose.yml`

   proxy:
     image: nginx
     ports:
       - "58094:8094"
       - "58093:8093"
       - "58091:8091"
     volumes:
       - ./config/proxy/conf.d:/etc/nginx/conf.d
       - ./config/proxy/nginx.conf:/etc/nginx/nginx.conf
     restart: always



Modifying the Nginx configuration
---------------------------------

In the :file:`config/proxy` directory, there should be a file named :file:`nginx.conf`. This file can be edited for example to specify the number of *worker_processes*. In the :file:`conf.d` directory, there are a number of additional configuration file for each *load balanced* service, for example :file:`flyingpigeon.conf`, which would look like:

.. code-block:: bash
   :caption: :file:`config/proxy/conf.d/flyingpigeon.conf`

   upstream flyingpigeon {
       hash $http_machineid;
       server <server1 url>:8093;
       server <server2 url>:8093;
       server <server3 url>:8093;
   }
   server {
       listen 8093;
       location / {
           proxy_pass http://flyingpigeon;
       }
   }

This tell the proxy, listing on port 8093, to redirect requests to servers 1, 2 or 3 according to the ``machineid`` argument passed in the request header. That is, requests with the same ``machineid`` will be sent to the same server. This is important to control since output files are not automatically visible to all servers. So if for example process A downloads a file from a remote server and process B subsets the file, both have to be run on the same machine otherwise process B won't find the downloaded file.

.. note::

   * Server configuration is static
   * It is not possible to assign port numbers to environment variables (eg ``$PORT_NUMBER``)
   * When you change a configuration file and restart NGINX to pick up the new configuration, it implements a *graceful restart*. Both the old and new copies of NGINX run side-by-side for a short period of time. The old processes don’t accept any new connections and terminate once all their existing connections terminate.

.. _NGINX: https://nginx.org
