#!/usr/bin/env bash
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

echo try to run ap

# 2. Is there Internet connectivity?
nmcli -t g | grep full

nmcli connection up petrologap
echo running ap

echo ..... start.sh: Running main app ....
python /usr/src/app/front.py