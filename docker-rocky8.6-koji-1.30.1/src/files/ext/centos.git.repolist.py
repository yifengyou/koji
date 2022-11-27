#!/usr/bin/env python
#pylint: disable=line-too-long
#
#  License: GPLv3
#
#  Initial Author: Bonnie King <bonniek@fnal.gov>
#         Updates:
#                  Pat Riehecky <riehecky@fnal.gov>
#
'''Get list of repos from pagure, to grab CentOS sources'''

# for python3 compat
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function

import logging
import sys
import json
import textwrap
import time

sys.setrecursionlimit(500)

try:
    from argparse import ArgumentParser
except ImportError:  # pragma: no cover
    print("Please install argparse - rpm: python-argparse", file=sys.stderr)
    raise

try:
    import requests
except ImportError:  # pragma: no cover
    print("Please install requests - rpm: python-requests", file=sys.stderr)
    raise


def setup_args():
    '''
        Setup the argparse object.

        Make sure all fields have defaults so we could use this as an object
    '''
    parser = ArgumentParser(description=textwrap.dedent(__doc__))

    parser.add_argument('--debug', action='store_true', default=False,
                        help='Print debugging information')
    parser.add_argument('--hostname', default='git.centos.org',
                        type=str, help='What host should we query?')
    parser.add_argument('--apiver', default='0',
                        type=str, help='What api version is the host?')
    parser.add_argument('--namespace', default='rpms',
                        type=str, help='What project namespace?')
    parser.add_argument('--show-forks', action='store_true', default=False,
                        help='Should we also show project forks?')

    return parser

def run_query(hostname, api, namespace, forks):
    '''
        Actually call the API version
    '''
    list_of_urls = []
    if str(api) == '0':
        query = 'https://{hostname}/api/0/projects?per_page=50&namespace={namespace}'.format(hostname=hostname, namespace=namespace)
        if forks:
            query = query + '&forks=1'
        else:
            query = query + '&forks=0'

        fetch_prefix = 'https://{hostname}/'.format(hostname=hostname)

        fetch_next_v0(query, fetch_prefix, list_of_urls)
    else:
        raise NotImplementedError("Unknown API version %s", api)

    list_of_urls.sort()
    return list_of_urls

def fetch_next_v0(page, fetch_prefix, list_of_urls):
    '''
        Recursively fetch the page until we are done
    '''
    logging.debug('Trying to fetch %s', page)
    try:
        req = requests.get(page)
    except requests.exceptions.RequestException as err_msg:
        print(err_msg, file=sys.stderr)
        raise

    try:
        message = json.loads(req.text)
    except ValueError as err_msg:
        print(page, file=sys.stderr)
        print(req.text, file=sys.stderr)
        print(err_msg, file=sys.stderr)
        raise

    for project in message['projects']:
        list_of_urls.append(fetch_prefix + project['fullname'])

    if 'next' in message['pagination']:
        if message['pagination']['next']:
            time.sleep(0.25) # Add a smallish delay to help with load
            fetch_next_v0(message['pagination']['next'], fetch_prefix, list_of_urls)

if __name__ == '__main__':

    PARSER = setup_args()
    ARGS = PARSER.parse_args()

    if ARGS.debug:
        logging.basicConfig(level=logging.DEBUG)

    URLS = run_query(ARGS.hostname, ARGS.apiver, ARGS.namespace, ARGS.show_forks)

    for URL in URLS:
        print(URL)
