supervisorclusterctl
=======

supervisorclusterctl is a cmd line tool that allows to control a cluster of processes by utilizing Supervisor and Ansible.

The tool uses Ansible and Supervisor's supervisorctl to control remote Supervisor daemons (supervisord). 
The primary goal of supervisorclusterctl is to simplify the use of Ansible and Supervisor's supervisorctl by focusing on the most commonly used supervisorctl actions.

Read the documentation at http://supervisorclusterctl.readthedocs.org/

The project is build and tested with Travis CI. Build status of master branch is:

.. image:: https://travis-ci.org/RobWin/supervisorclusterctl.svg?branch=master
    :target: https://travis-ci.org/RobWin/supervisorclusterctl