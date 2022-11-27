# MQTT scripts

The mqtt.git.centos.org server requires authentication.  As a result we've provided some client server scripts that will let you protect your keys.

These can also be used as a basis for building your own MQTT automation scripts.

## Scripts:

* send-mqtt-to-dbus.py - Connects the MQTT messages to a dbus interface.
    To fully protect your keys you can setup the system bus (a config is provided by --dbus-config)
    Then you can have this run as a dedicated user that has access to your keys.
    See the `on_mqtt_connect` and `on_mqtt_message` functions for customizing the behavior.

* listen-on-dbus-for-mqtt-signals.py - Listens to messages sent to dbus and performs an action.
    You can set this to run a generic command or customize it to fit your needs.
    See the `signal_recieved` function for customizing the behavior.

* example-safe-command.py - It is an example of how to run a command from listen-on-dbus-for-mqtt-signals.py

* send-mqtt-to-irc.py - An untested IRC bot that will (in theory) chat out the messages.

## Systemd Unit:

Some sample systemd unit files are provided to work with the example scripts.

NOTE: They require customization before use.
      You must at minimum set the User= to a trusted user.

* listen-on-dbus-for-mqtt-signals.service
    You should adjust the path of commands and select a safe command to execute.

* send-mqtt-to-dbus.service
    You should setup the system dbus profile with --dbus-config

## Container notes:

It is _not_ considered safe to share the host dbus (system or session) with a container.  This can permit the container to escape into the host and violate the security of your system.

For example, here is how you can reboot a host from dbus if you've got rights.
```
DBUS_SYSTEM_BUS_ADDRESS=unix:path=/run/dbus/system_bus_socket \
  dbus-send --system --print-reply    \
  --dest=org.freedesktop.systemd1     \
  /org/freedesktop/systemd1           \
  org.freedesktop.systemd1.Manager.Reboot
```
