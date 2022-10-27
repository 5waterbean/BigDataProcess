#!/usr/bin/python3
import sys
import calendar

command = sys.argv
inputfile = command[1]
outputfile = command[2]
dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

list = []
with open(inputfile, "rt") as ipf:
	for line in ipf:
		text = line.split(",")
		bnumber = text[0]
		date = text[1].split("/")
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		vehicles = text[2]
		trips = text[3][:-1]
		list.append(bnumber + "," + dayofweek[day] + " " + vehicles + "," + trips + "\n")

with open(outputfile, "at") as opf:
	for line in list:
		opf.write(line)
