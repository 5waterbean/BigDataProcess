#!/usr/bin/python3
import sys

command = sys.argv
inputfile = command[1]
outputfile = command[2]

dic = dict()
with open(inputfile, "rt") as ipf:
	for line in ipf:
		text = line.split("::")
		genres = text[2]
		glist = genres.split("|")
		for g in glist:
			if g.endswith("\n"):
				g = g[:-1]
			if g not in dic:
				dic[g] = 1
			else:
				dic[g] += 1

with open(outputfile, "at") as opf:
	items = dic.items()
	for item in items:
		opf.write(item[0] + " " + str(item[1]) + "\n")
