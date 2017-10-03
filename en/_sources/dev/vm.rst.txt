================
VM configuration
================

For development and testing it can be useful to install pavics-sdi in a virtual machine. Here we describe the configuration for an `OpenStack`_ environment.

Data volumes
============

* Attach 2 openstack volumes to the vm (take note of its name looking like ``/dev/vdx``)
* Mount them at ``/data`` and ``/geoserver_data`` using the following command::

     mount /dev/vdx /[geoserver_]data

* New volumes must first be formatted using the command :command:`mkfs.ext4 /dev/vdx`

Docker volume
=============

Docker can take a lot of space to maintain all containers and the default directory ``/var/lib/docker`` on the host can rapidly run out of disk space. The easy solution is to mount a bigger volume at this position:

#. Attach an openstack volume to the vm (take note of its name looking like ``/dev/vdx``)
#. Stop the docker service : :command:`service docker stop`
#. Mount the new volume at :file:`/var/lib/docker` using the following command::

      mount /dev/vdx /var/lib/docker

#. Start the docker service: :command:`service docker start`

Automount
=========

To automatically mount volumes at reboot we modified the :file:`/etc/fstab` file to include the attached `OpenStack`_ volumes. For example (mind the tabspaces):

.. code-block:: bash
   :caption: :file:`/etc/fstab`

   LABEL=cloudimg-rootfs   /        ext4   defaults        0 0
   /dev/vdb        none            swap    sw,comment=cloudconfig  0       0
   /dev/vdd        /data           ext4    defaults        0 0
   /dev/vdc        /var/lib/docker ext4    defaults        0 0


Hostname resolution
===================

The virtual machine is publicly visible by using the `OpenStack`_ external IP. But this IP is not visible from inside, the internal IP must be used. To resolve this issue, create a DNS entry mapping a hostname to the external IP and edit :file:`/etc/hosts` from inside the VM so that the same hostname maps the internal IP.

For example, ``outarde.crim.ca`` is resolved as 132.217.140.52 (OpenStack external IP) everywhere but from the inside of this vm the :file:`/etc/hosts` config resolve this hostname to 192.168.101.91 (OpenStack internal IP).


.. _`OpenStack`: https://www.openstack.org/