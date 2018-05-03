#!/usr/bin/env bash
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

echo ..... start.sh: Running main app ....
python /usr/src/app/front.py