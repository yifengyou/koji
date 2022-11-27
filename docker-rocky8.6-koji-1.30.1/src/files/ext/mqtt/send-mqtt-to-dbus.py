#!/usr/bin/env python3.6
#pylint: disable=line-too-long
#
#  Copyright (2019).  Fermi Research Alliance, LLC.
#  Initial Author: Pat Riehecky <riehecky@fnal.gov>
#
'''
    Connect to the MQTT server and convert messages into dbus signals.
'''

## Uncomment these for python2 support
#from __future__ import unicode_literals
#from __future__ import absolute_import
#from __future__ import print_function

import datetime
import logging
import json
import os.path
import sys
import random
import textwrap

DBUS_INTERFACE = 'org.centos.git.mqtt'

try:
    import paho.mqtt.client
except ImportError:  # pragma: no cover
    print("Please install paho.mqtt.client - rpm: python-paho-mqtt", file=sys.stderr)
    raise

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
    ca_cert = str(os.path.expanduser('~/')) + '.centos-server-ca.cert'
    user_pubkey = str(os.path.expanduser('~/')) + '.centos.cert'
    user_privkey = str(os.path.expanduser('~/')) + '.centos.cert'

    # use a psudo random number for keepalive to help spread out the load
    #  some time between 1m 30s and 2m 10s
    keep_alive = random.randint(90, 130)

    parser = ArgumentParser(description=textwrap.dedent(__doc__))

    parser.add_argument('--debug',action='store_true',
                        help='Print out all debugging actions',
                        default=False)
    parser.add_argument('--client-connection-name', metavar='<UNIQUESTRING>',
                        help='Use this specific name when connecting. Default is a psudo-random string.',
                        default='', type=str)
    parser.add_argument('--mqtt-server', metavar='<HOSTNAME>',
                        help='Connect to this MQTT server',
                        default='mqtt.git.centos.org', type=str)
    parser.add_argument('--mqtt-port', metavar='<PORTNUMBER>',
                        help='Connect to MQTT server on this port',
                        default='8883', type=int)
    parser.add_argument('--mqtt-source-ip', metavar='<SOURCE_IP>',
                        help='Connect to MQTT server from this address. Default is any.',
                        default='', type=str)
    parser.add_argument('--mqtt-topic', metavar='<TOPIC_ID>',
                        action='append', nargs='+', type=str,
                        help='Which MQTT topic should we watch. You may set multiple times.')
    parser.add_argument('--mqtt-keepalive', metavar='<SECONDS>',
                        help='Seconds between MQTT keepalive packets.',
                        default=keep_alive, type=int)
    parser.add_argument('--mqtt-no-ssl', action='store_false', dest='mqtt_ssl',
                        help='Should MQTT use SSL? Default is to use SSL (and the SSL port).')
    parser.add_argument('--mqtt-server-ca', metavar='<ABSOLUTE_PATH>',
                        help='Use this CA cert to validate the MQTT Server.',
                        default=ca_cert, type=str)
    parser.add_argument('--mqtt-client-cert', metavar='<ABSOLUTE_PATH>',
                        help='Use this public key to identify yourself.',
                        default=user_pubkey, type=str)
    parser.add_argument('--mqtt-client-key', metavar='<ABSOLUTE_PATH>',
                        help='The private key that matches with --mqtt-client-cert .',
                        default=user_privkey, type=str)
    parser.add_argument('--dbus-use-system-bus',action='store_true',
                        help='Should we use the global SystemBus or the user SessionBus. The SystemBus requires settings in /etc/dbus-1/system.d/myservice.conf',
                        default=False)
    parser.add_argument('--dbus-config',action='store_true',
                        help='Just output the SystemBus permissions file and exit',
                        default=False)

    return parser

##########################################
class BusMessage(object):
    """
    Server_XML definition.
    """
    dbus = """<?xml version="1.0" encoding="UTF-8" ?>
    <node>
        <interface name="{}">
            <signal name="message">
                <arg type='s'/>
            </signal>
        </interface>
    </node>
    """.format(DBUS_INTERFACE)

    # Function does all the work already
    message = signal()

def DbusPermissionsConf(interface_name):
    '''
        For the SystemBus you need permission to create endpoints
    '''
    import getpass
    whoami = getpass.getuser()

    xml = '''<?xml version="1.0" encoding="UTF-8" ?>
<!-- Copy me into /etc/dbus-1/system.d/{interface_name}.conf and reload dbus -->
<!--  You can send the signal with: dbus-send &dash;&dash;system &dash;&dash;type=signal / org.centos.git.mqtt.message 'string:{{"test": ["1", "2"]}}' -->
<!--  You can watch bus with dbus-monitor &dash;&dash;system 'interface=org.centos.git.mqtt' -->
<!DOCTYPE busconfig PUBLIC
          "-//freedesktop//DTD D-BUS Bus Configuration 1.0//EN"
          "http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
<busconfig>
    <!-- Always allow root to do anything -->
    <policy user="root">
        <allow own="{interface_name}" />
        <allow send_interface="{interface_name}/" />
    </policy>
    <!-- Allow a single non-root user to setup interface and send to endpoint -->
    <!--  You can change this to group='somegroup' if you desire -->
    <policy user="{whoami}">
        <allow own="{interface_name}" />
        <allow send_interface="{interface_name}" send_destination="{interface_name}.message" />
    </policy>
    <!-- Always allow anyone to listen  -->
    <policy context="default">
        <allow receive_interface="{interface_name}" />
        <allow receive_sender="{interface_name}.message" />
    </policy>
</busconfig>
'''
    return xml.format(interface_name=interface_name, whoami=whoami)

##########################################
def on_mqtt_message(client, userdata, message):
    ''' What should I do if I get a message? '''
    logging.debug('Message received topic:%s payload:%s', message.topic, message.payload.decode("utf-8"))

    # Or you can customize this to fit your needs
    signal = {message.topic: json.loads(message.payload.decode("utf-8"))}
    userdata['emit'].message(json.dumps((signal)))

    logging.debug('Sending signal: %s', json.dumps(signal))

def on_mqtt_disconnect(client, userdata, rc):
    ''' If you get a connection error, print it out '''
    if rc:
        logging.error('Disconnected with error ErrCode:%s', rc)
        logging.error('ErrCode:%s might be - %s', rc, paho.mqtt.client.error_string(rc))
        logging.error('ErrCode:%s might be - %s', rc, paho.mqtt.client.connack_string(rc))
        raise SystemExit

    logging.error('Disconnected from MQTT Server')

def on_mqtt_connect(client, userdata, flags, rc):
    ''' Automatically subscribe to all topics '''
    logging.debug('Connected with status code : %s', rc)

    for topic in userdata['topics']:
        client.subscribe(topic)
        logging.info('Subscribing to topic %s', topic)
        signal = {'mqtt.setup': 'Subscribing to topic {} at {}'.format(topic, datetime.datetime.now())}
        userdata['emit'].message(json.dumps(signal))

##########################################
##########################################
if __name__ == '__main__':

    PARSER = setup_args()
    ARGS = PARSER.parse_args()

    if ARGS.dbus_config:
        print(DbusPermissionsConf(DBUS_INTERFACE))
        raise SystemExit

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

    if ARGS.client_connection_name:
        MYLOGGER.info('Attempting to connect as %s to %s:%s', ARGS.client_connection_name, ARGS.mqtt_server, ARGS.mqtt_port)
    else:
        MYLOGGER.info('Attempting to connect with random name to %s:%s', ARGS.mqtt_server, ARGS.mqtt_port)

    CLIENT = paho.mqtt.client.Client(client_id=ARGS.client_connection_name, clean_session=True)

    if ARGS.mqtt_ssl:
        ARGS.mqtt_server_ca = os.path.expanduser(ARGS.mqtt_server_ca)
        if not os.path.exists(ARGS.mqtt_server_ca):
            raise ValueError('No such file %s', ARGS.mqtt_server_ca)

        ARGS.mqtt_client_cert = os.path.expanduser(ARGS.mqtt_client_cert)
        if not os.path.exists(ARGS.mqtt_client_cert):
            raise ValueError('No such file %s', ARGS.mqtt_client_cert)

        ARGS.mqtt_client_key = os.path.expanduser(ARGS.mqtt_client_key)
        if not os.path.exists(ARGS.mqtt_client_key):
            raise ValueError('No such file %s', ARGS.mqtt_client_key)

        MYLOGGER.info('SSL enabled CA=%s PUBKEY=%s PRIVKEY=%s', ARGS.mqtt_server_ca, ARGS.mqtt_client_cert, ARGS.mqtt_client_key)
        CLIENT.tls_set(ca_certs=ARGS.mqtt_server_ca, certfile=ARGS.mqtt_client_cert, keyfile=ARGS.mqtt_client_key)

    try:
        CLIENT.enable_logger(logger=MYLOGGER)
    except AttributeError:
        # Added in 1.2.x of mqtt library
        pass

    CLIENT.on_connect = on_mqtt_connect
    CLIENT.on_message = on_mqtt_message
    CLIENT.on_disconnect = on_mqtt_disconnect

    CLIENT.connect_async(host=ARGS.mqtt_server, port=ARGS.mqtt_port, keepalive=ARGS.mqtt_keepalive, bind_address=ARGS.mqtt_source_ip)

    DBUS_MESSAGE = BusMessage()

    if not ARGS.mqtt_topic:
        ARGS.mqtt_topic = ['git.centos.org/#',]

    CLIENT.user_data_set({'topics': ARGS.mqtt_topic, 'emit': DBUS_MESSAGE})

    # loop_start will run in background async
    CLIENT.loop_start()

    if ARGS.dbus_use_system_bus:
        BUS = SystemBus()
    else:
        BUS = SessionBus()

    if ARGS.dbus_use_system_bus:
        MYLOGGER.debug('Publishing to system bus %s', DBUS_INTERFACE)
    else:
        MYLOGGER.debug('Publishing to session bus %s', DBUS_INTERFACE)

    BUS.publish(DBUS_INTERFACE, DBUS_MESSAGE)

    # loop forever, until CTRL+C, or something goes wrong
    try:
        MainLoop().run()
    except KeyboardInterrupt:
        CLIENT.disconnect()
        logging.debug('Got CTRL+C, exiting cleanly')
        raise SystemExit
    except:
        CLIENT.disconnect()
        raise
    finally:
        CLIENT.disconnect()
