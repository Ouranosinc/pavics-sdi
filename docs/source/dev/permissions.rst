=========================
User and Group management
=========================

The following guide explains the management of users, groups, and permissions for the PAVICS deployment. Permissions and group settings for users both server-side and client-side and can be configured to unique deployment specifications.

As mentioned, PAVICS is built to work within POSIX and POSIX-like systems. As such, user/group management within servers running PAVICS is synonymous with conventions for user/group management in Linux and Unix systems.


.. warning::
	Are we clarifying both within-server permissions and permissions as set within the Birds?

Adding Users and Groups to PAVICS server
========================================

Users added to the PAVICS server for the purpose of adding data or administering Bird services may need unique access privileges. Once a user has been created with `useradd <https://linux.die.net/man/8/useradd>`_ and groups initiatialized with `groupadd <https://linux.die.net/man/8/groupadd>`_ group membership and privileges can be later specified with ``usermod`` and ``groupmod``.   

Begin by tunneling into the server::

	ssh user@server

User and Group management for Bird services
===========================================

.. todo::

   How authorizations for services work (the concept)
   How to grant users access to data and services


Permissions and authorizations
------------------------------

Twitcher?
---------


Malleefowl?
-----------





