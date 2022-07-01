#!/usr/bin/env python3

import xmltodict
import sys, getopt, json


inputstream = sys.stdin
input = inputstream.read()

text = '<_><web><ip>truc</ip></web><db><ip>machine</ip></db></_>'
input = "<root>" + input + "</root>"
xpars = xmltodict.parse(input)["root"]
json = json.dumps(xpars)
print(json)

