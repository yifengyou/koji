#!/usr/bin/env python3.6
#pylint: disable=line-too-long
#
#  Copyright (2019).  Fermi Research Alliance, LLC.
#  Initial Author: Pat Riehecky <riehecky@fnal.gov>
#
'''
    Example command to run from listen-on-dbus-for-mqtt-signals.py
'''

## Uncomment these for python2 support
#from __future__ import unicode_literals
#from __future__ import absolute_import
#from __future__ import print_function

import json
import sys
import textwrap

from pprint import pprint

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

    parser.add_argument('signal', help='The dbus signal is set here')

    return parser

##########################################

##########################################
##########################################
if __name__ == '__main__':

    PARSER = setup_args()
    ARGS = PARSER.parse_args()

    MESSAGE = json.loads(sys.stdin.read())
    print("Your dbus-signal was %s" % ARGS.signal)
    print("Your message was decoded as %s (between the lines)" % type(MESSAGE))
    print("------------------------------------------------")
    pprint(MESSAGE)
    print("------------------------------------------------")
