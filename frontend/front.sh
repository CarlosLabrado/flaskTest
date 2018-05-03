#!/usr/bin/env bash
sleep 10

echo try to run ap
nmcli connection up petrologap
echo running ap

echo ..... start.sh: Running main app ....
python /usr/src/app/front.py