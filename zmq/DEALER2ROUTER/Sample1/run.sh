#!/bin/bash

REVERSE=false
while getopts n OPT
do
    case $OPT in
        -r) REVERSE=true ;;
        --reverse) REVERSE=true ;;
        *) ;;
    esac
done

FRONTENDHOST="127.0.0.1"
FRONTENDPORT=5001
BACKENDHOST="127.0.0.1"
BACKENDPORT=5002
KILLHOST="127.0.0.1"
KILLPORT=5003
python Broker.py --frontendhost $FRONTENDHOST --frontendport $FRONTENDPORT --backendhost $BACKENDHOST --backendport $BACKENDPORT  --killhost $KILLHOST --killport $KILLPORT &
if $REVERSE; then
  python REP.py --host $FRONTENDHOST --port $FRONTENDPORT --reverse &
  python REQ.py --host $BACKENDHOST --port $BACKENDPORT --reverse
else
  python REP.py --host $FRONTENDHOST --port $FRONTENDPORT &
  python REQ.py --host $BACKENDHOST --port $BACKENDPORT
fi