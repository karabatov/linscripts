#!/usr/bin/python

# Simple parsing of ESXi FS autodiscovery

import json, sys

obj = json.load(sys.stdin)
for it in obj["data"]:
    if it[u'{#DSNAME}'] == sys.argv[1]:
        if sys.argv[2] == 'acessible': 
            print it[u'{#DSACCESS}']
        elif sys.argv[2] == 'capacity': 
            print it[u'{#DSCAP}']
        elif sys.argv[2] == 'free': 
            print it[u'{#DSFREE}']
        elif sys.argv[2] == 'pfree': 
            print it[u'{#DSPFREE}']
        else:
            print "-1"
