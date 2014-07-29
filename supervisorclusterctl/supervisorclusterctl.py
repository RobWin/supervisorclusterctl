from __init__ import __version__, __programm_name__, __programm_description__
from argparse import ArgumentParser
from subprocess import call
import sys

DEBUG = 1

class CLIError(Exception):
    """Generic exception to raise and log different fatal errors."""
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None):
    """Command line options."""
   
    program_name = __programm_name__
    program_version = "v%s" % __version__
    program_descrption = __programm_description__

    try:
        # Setup argument parser
        parser = ArgumentParser(prog=program_name, description=program_descrption)
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="run in verbose mode (-vvv for more, -vvvv to enable connection debugging)")
        parser.add_argument("-s", "--sudo", action="store_true", help="run supervisorctl actions with sudo (nopasswd))")
        parser.add_argument("-V", "--version", action="version", version=program_version)
        parser.add_argument("host-pattern", help="A host-pattern usually refers to a group of hosts. For more details, see Ansible documentation about Patterns.")
        #parser.add_argument("supervisorctl-action", help="A supervisorctl action (and optional argument). For more details, see Supervisor documentation about the available supervisorctl actions.")
        
        subparsers = parser.add_subparsers(help="One of the available supervisorctl actions.", dest="supervisorctl-action")
        subparsers.add_parser("status", help="Get status info of all processes.")
        subparsers.add_parser("reread", help="Reread the configuration files of supervisord")
        subparsers.add_parser("reload", help="Restart remote supervisord")
        subparsers.add_parser("update", help="Reload the configuration files of supervisord and add/remove processes as necessary")
        start_subparser = subparsers.add_parser("start", help="Start a process by name")
        start_subparser.add_argument("process-name", help="Name of the process")
        stop_subparser = subparsers.add_parser("stop", help="Stop a process by name")
        stop_subparser.add_argument("process-name", help="Name of the process")
        restart_subparser = subparsers.add_parser("restart", help="Restart a process by name")
        restart_subparser.add_argument("process-name", help="Name of the process")
        remove_subparser = subparsers.add_parser("remove", help="Remove a process by name")
        remove_subparser.add_argument("process-name", help="Name of the process")
        
        # Process arguments
        args = parser.parse_args(argv)
        verbose = args.verbose
        host_pattern = getattr(args, "host-pattern")
        supervisorctl_action = getattr(args, "supervisorctl-action")        
        
        sudo = args.sudo
        ansible_executable = "ansible"
        supervisorctl_executable = "supervisorctl"
        ansible_action_option = "-a"
        
        if sudo:
            supervisorctl_command = "sudo " + supervisorctl_executable + " " + supervisorctl_action
        else:
            supervisorctl_command = supervisorctl_executable + " " + supervisorctl_action
          
        if (supervisorctl_action not in ['status', 'reread', 'update']):
            supervisorctl_argument = getattr(args, "process-name")
            supervisorctl_command = supervisorctl_command + ' ' + supervisorctl_argument
            
        if verbose >0:
            verbose_level = "-"+ "v"*verbose
            print("Verbose mode on: " + verbose_level)
            print "Parsed arguments:"
            print args   
            call([ansible_executable, host_pattern, verbose_level, ansible_action_option, supervisorctl_command,])
        else:
            call([ansible_executable, host_pattern, ansible_action_option, supervisorctl_command])
        
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main(["dev", "-v", "-s", "start", "test"]))