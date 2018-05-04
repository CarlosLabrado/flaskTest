#! /bin/bash
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket
dbus-send --system --print-reply --dest=org.freedesktop.NetworkManager /org/freedesktop/NetworkManager org.freedesktop.DBus.Properties.Set string:"org.freedesktop.NetworkManager" string:"WirelessEnabled" variant:boolean:false

echo activate connection first
python /usr/src/app/activate_connection.py

echo ..... start.sh: Running main app ....
python /usr/src/app/front.py