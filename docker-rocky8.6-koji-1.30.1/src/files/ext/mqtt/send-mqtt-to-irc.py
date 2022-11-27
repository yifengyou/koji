#!/usr/bin/env python3.6
#pylint: disable=line-too-long
#
#  Copyright (2019).  Fermi Research Alliance, LLC.
#  Initial Author: Pat Riehecky <riehecky@fnal.gov>
#
'''
    Connect to the MQTT server and convert messages into irc messages.
'''

## Uncomment these for python2 support
#from __future__ import unicode_literals
#from __future__ import absolute_import
#from __future__ import print_function

import datetime
import logging
import os.path
import sys
import random
import textwrap

try:
    import paho.mqtt.client
except ImportError:  # pragma: no cover
    print("Please install paho.mqtt.client - rpm: python-paho-mqtt", file=sys.stderr)
    raise

try:
    import irc.client
except ImportError:  # pragma: no cover
    print("Please install irc - pip install --user irc", file=sys.stderr)
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
    parser.add_argument('--irc-server', metavar='<HOSTNAME>',
                        help='The hostname of your irc server.',
                        default='chat.freenode.net', type=str)
    parser.add_argument('--irc-port', default=6667, type=int,
                        help='IRC port number.',
    parser.add_argument('--irc-bot-name', metavar='<BOT_NIC>',
                        help='The name of your IRC bot.',
                        default='testbot__', type=str)
    parser.add_argument('--irc-bot-password', metavar='<PASSWORD>',
                        help='The password for your IRC bot.',
                        type=str)
    parser.add_argument('--irc-bot-admin', metavar='<YOUR_NIC>',
                        help="The name of your IRC bot's owner.",
                        default='', type=str)
    parser.add_argument('--irc-channel', metavar='<WHERE_TO_POST>',
                        help="The name of an IRC channel where your bot will psot.",
                        default='#bot-testing', type=str)

    return parser

##########################################
class IRCBot(irc.client.SimpleIRCClient):
    ''' An IRC bot as an object '''
    def __init__(self, channel, admin_nic):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.target_channel = channel
        self.admin_nic = admin_nic

        if self.admin_nic == '':
            raise ValueError("You must set an owner for your bot")

    def on_welcome(self, connection, event):
        if irc.client.is_channel(self.target_channel):
            connection.join(self.target_channel)
            self.connection.notice(self.target_channel, "Hello, I am a bot owned by " + self.admin_nic)

    def on_disconnect(self, connection, event):
        sys.exit(0)

    def send_message(self, message):
        self.connection.notice(self.target, message)

##########################################
def on_mqtt_message(client, userdata, message):
    ''' What should I do if I get a message? '''
    logging.debug('Message received topic:%s payload:%s', message.topic, message.payload.decode("utf-8"))

    # Or you can customize this to fit your needs

    logging.debug('Sending signal: %s', signal)

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
        userdata['emit'].message(str(signal))

##########################################
##########################################
if __name__ == '__main__':

    PARSER = setup_args()
    ARGS = PARSER.parse_args()

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

    MYBOT = IRCBot(ARGS.irc_channel, ARGS.irc_bot_name, ARGS.irc_server, ARGS.irc_port, ARGS.irc_channel, ARGS.irc_bot_admin)

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

    if not ARGS.mqtt_topic:
        ARGS.mqtt_topic = ['git.centos.org/#',]

    CLIENT.user_data_set({'topics': ARGS.mqtt_topic, 'emit': DBUS_MESSAGE})

    # loop_start will run in background async
    CLIENT.loop_start()

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
