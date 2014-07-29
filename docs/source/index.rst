.. supervisorclusterctl documentation master file, created by
   sphinx-quickstart on Tue Jul 29 08:58:56 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

supervisorclusterctl's documentation
================================================

supervisorclusterctl is a cmd line tool that allows to control a cluster of processes by utilizing `Supervisor <http://supervisord.org/>`_ and `Ansible <http://docs.ansible.com/>`_.

The tool uses Ansible and Supervisor's supervisorctl to control remote Supervisor daemons (supervisord). 
The primary goal of supervisorclusterctl is to simplify the use of Ansible and Supervisor's supervisorctl by focusing on the most used supervisorctl actions.

.. toctree::
   :maxdepth: 2

   installation
   user_guide

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

