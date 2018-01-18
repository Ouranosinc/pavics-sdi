============
Contributing
============

Benchmark development environment
=================================

Recommended VirtualBox installation:

- Install Oracle VM VirtualBox Extension Pack
- Linux Ubuntu 16.04.3 (64-bit)
- >8 gb memory
- >70 gb disk space
- >2 CPUs
- Network bridge access
- Install VBoxGuestAdditions inside the Ubuntu guest for corresponding
  VirtualBox version

Required packages for various PAVICS components:

git docker.io docker-compose


Setting up pycharm
==================

- May need to uninstall wheel
- For missing python modules: https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html

Commands to run in Python console::

    import pip
    pip.main(['install', 'https://github.com/geopython/pywps/archive/7cab3866e34ce24d3df56e3c1c546739b1cda2d7.zip'])
    pip.main(['install', 'https://github.com/bird-house/OWSLib/archive/pingudev.zip'])
