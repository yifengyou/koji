#!/usr/bin/env python3.6
#pylint: disable=line-too-long
#
#  Copyright (2019).  Fermi Research Alliance, LLC.
#  Initial Author: Pat Riehecky <riehecky@fnal.gov>
#
'''
    Listen to dbus events
'''

## Uncomment these for python2 support
#from __future__ import unicode_literals
#from __future__ import absolute_import
#from __future__ import print_function

import json
import logging
import os.path
import sys
import textwrap

from subprocess import Popen, PIPE

DBUS_INTERFACE = 'org.centos.git.mqtt'

try:
    from pydbus import SystemBus, SessionBus
    from pydbus.generic import signal
except ImportError:  # pragma: no cover
    print("Please install pydbus - rpm: python-pydbus", file=sys.stderr)
    raise

try:
    from gi.repository.GLib import MainLoop
except ImportError:  # pragma: no cover
    print("Please install pygobject - rpm: python-gobject", file=sys.stderr)
    raise

try:
    from argparse import ArgumentParser
except ImportError:  # pragma: no cover
    print("Please install argparse - rpm: python-argparse", file=sys.stderr)
    raise

##########################################
def setup_args():
    '''
        Setup the argparse object.

        Make sure all fields have defaults so we could use this as an object
    '''
    parser = ArgumentParser(description=textwrap.dedent(__doc__))

    parser.add_argument('--debug',action='store_true',
                        help='Print out all debugging actions',
                        default=False)
    parser.add_argument('--dbus-use-system-bus',action='store_true',
                        help='Should we use the global SystemBus or the user SessionBus. The SystemBus requires settings in /etc/dbus-1/system.d/myservice.conf',
                        default=False)
    parser.add_argument('--run-command', metavar='<ABSOLUTE_PATH>',
                        help='Command to run with message payload. sys.argv[1] will be the DBUS signal name, STDIN will be the payload as json. If no run command, simply print the results to STDOUT.',
                        default='', type=str)

    return parser

##########################################

##########################################
##########################################
if __name__ == '__main__':

    PARSER = setup_args()
    ARGS = PARSER.parse_args()

    if ARGS.run_command != '':
        if not os.path.exists(ARGS.run_command):
            raise ValueError('No such file %s', ARGS.run_command)

    MYLOGGER = logging.getLogger()

    if ARGS.debug:
        MYLOGGER.setLevel(logging.DEBUG)
    else:
        MYLOGGER.setLevel(logging.WARNING)

    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    MYLOGGER.addHandler(handler)

    PROGRAM_NAME = os.path.basename(sys.argv[0])
    MYLOGGER.debug('Running:%s args:%s', PROGRAM_NAME, sys.argv[1:])

    if ARGS.dbus_use_system_bus:
        BUS = SystemBus()
    else:
        BUS = SessionBus()

    def signal_recieved(sender, obj, iface, signal, params):
        ''' Define in scope so I can read ARGS '''
        # sanitize all my single quotes
        signal_msg = json.dumps(json.loads(params[0]))

        logging.debug("sender:%s object:%s iface:%s signal:%s all_params:%s signal_msg=%s", sender, obj, iface, signal, params, signal_msg)

        logging.debug("Running %s %s < %s", ARGS.run_command, signal, signal_msg)
        if ARGS.run_command == '':
            print("signal:%s signal_msg:%s" % (signal, signal_msg), file=sys.stderr)
        else:
            # Or you can customize this to fit your needs
            proc = Popen([ARGS.run_command, signal], stdin=PIPE, cwd='/tmp', start_new_session=True, universal_newlines=True)
            proc.communicate(input=signal_msg)
            proc.wait(timeout=300)

    if ARGS.dbus_use_system_bus:
        MYLOGGER.debug('Subscribing to system bus %s', DBUS_INTERFACE)
    else:
        MYLOGGER.debug('Subscribing to session bus %s', DBUS_INTERFACE)

    BUS.subscribe(iface=DBUS_INTERFACE, signal_fired=signal_recieved)

    # loop forever, until CTRL+C, or something goes wrong
    try:
        MainLoop().run()
    except KeyboardInterrupt:
        logging.debug('Got CTRL+C, exiting cleanly')
        raise SystemExit
