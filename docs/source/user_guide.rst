User Guide
============

.. contents:: Topics

Running supervisorclusterctl
```````````````````

Now that you've installed supervisorclusterctl, it's time to get started with some basics.

Edit /etc/ansible/hosts and put one or more remote systems in it, for
which you have your SSH key in ``authorized_keys``::

    [production]
    192.168.0.11
    192.168.0.12
    [development]
    192.168.0.10

This is an inventory file, which is  explained in greater detail in Ansible's documentation

Now run a supervisorclusterctl command to get the status of all Supervisor managed processes on all of your configured production nodes:
  
.. code-block:: bash

   $ supervisorclusterctl production status
   
Run help to see all available command-line commands, arguments and options 

.. code-block:: bash

   $ supervisorclusterctl -h
	usage: supervisorclusterctl [-h] [-v] [-s] [-V]
	                            host-pattern {status,reread,update,start,restart}
	                            ...
	
	supervisorclusterctl is a cmd line tool that allows to control a cluster of
	supervisord instances by utilizing supervisorctl and Ansible.
	
	positional arguments:
	  host-pattern          A host-pattern usually refers to a group of hosts. For
	                        more details, see Ansible documentation about
	                        Patterns.
	  {status,reread,update,start,restart}
	                        One of the available supervisorctl actions.
	    status              Get status info of all processes.
	    reread              Reread the configuration files of supervisord
	    update              Reload the configuration files of supervisord and
	                        add/remove processes as necessary
	    start               Start a process by name
	    start               Stop a process by name
	    restart             Restart a process by name
	    start               Remove a process by name
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --verbose         run in verbose mode (-vvv for more, -vvvv to enable
	                        connection debugging)
	  -s, --sudo            run supervisorctl actions with sudo (nopasswd))
	  -V, --version         show program's version number and exit