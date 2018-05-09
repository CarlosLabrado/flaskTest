#!/usr/bin/env bash

#start wifi connect
echo starting wifi connect
./wifi-connect --portal-listening-port 45454

#start main app
echo .... Running main app ....
python /usr/src/app/front.py