#!/usr/bin/python3
import sys

command = sys.argv
inputfile = command[1]
outputfile = command[2]

with open(inputfile, "rt") as ipf:
	for line in ipf:
		text = line.split(",")
