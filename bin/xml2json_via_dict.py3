#!/usr/bin/env python3

import xmltodict
import sys, getopt, json


inputstream = sys.stdin
input = inputstream.read()

text = '<_><web><ip>truc</ip></web><db><ip>machine</ip></db></_>'
xpars = xmltodict.parse(input)
json = json.dumps(xpars)
print(json)

