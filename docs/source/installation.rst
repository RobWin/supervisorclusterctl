Installation
============

.. contents:: Topics

.. _control_machine_requirements:

Control Machine Requirements
````````````````````````````

supervisorclusterctl requires `Ansible <http://docs.ansible.com/>`_ to be installed on the control machine. 
You only need to install Ansible on one machine and it can control an entire fleet of remote nodes from that central point.  

Currently Ansible can be run from any machine with Python 2.6 installed (Windows isn't supported for the control machine).
This includes Red Hat, Debian, CentOS, OS X, any of the BSDs, and so on.

Ansible can be installed via "pip", the Python package manager.  If 'pip' isn't already available in
your version of Python, you can get pip by::

   $ sudo easy_install pip

Then install Ansible with::

   $ sudo pip install ansible

.. note::   
   Some Linux distributions offer a version of Ansible that is installable through the system package manager. 
   Use the package management tools of your distribution to check availability.

.. _managed_node_requirements:

Managed Node Requirements
`````````````````````````
supervisorclusterctl requires `Supervisor <http://supervisord.org/>`_ to be installed on the remote nodes. 

Supervisor can also be installed via "pip"

   $ sudo pip install supervisor
   
.. note::
   Some Linux distributions offer a version of Supervisor that is installable through the system package manager.
   Use the package management tools of your distribution to check availability.
 
.. _installing_supervisorclusterctl: 
 
Installing supervisorclusterctl
````````````````````````````   

.. _from_source:

Installing from source
+++++++++++++++++++

supervisorclusterctl is trivially easy to install from source. No daemons or database setup are required.  

To install from source.

.. code-block:: bash

    $ git clone https://github.com/RobWin/supervisorclusterctl.git
    $ cd ./supervisorclusterctl
    $ sudo python setup.py install

.. _create_rpm:

Create RPM package
+++++++++++++++++++
You can create a RPM package which can be used by many of popular Linux distributions, including Red Hat, SuSE:

   $ sudo python setup.py bdist_rpm
      
.. _create_rpm:   
   
Installing from tarball or zipball
+++++++++++++++++++++++++++

A zipball or tarball of the source are available on the `Project page <http://robwin.github.io/supervisorclusterctl/>`_.