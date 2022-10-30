#!/usr/bin/python3
import sys
import calendar

command = sys.argv
inputfile = command[1]
outputfile = command[2]
dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

dic = dict()
with open(inputfile, "rt") as ipf:
	for line in ipf:
		text = line.split(",")
		bnumber = text[0]
		date = text[1].split("/")
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		vehicles = int(text[2])
		trips = int(text[3][:-1])
		key = bnumber + "," + dayofweek[day]
		if key in dic:
			value = dic[key].split(",")
			vehicles += int(value[0])
			trips += int(value[1])
		dic[key] = str(vehicles) + "," + str(trips)

with open(outputfile, "at") as opf:
	items = dic.items()
	for item in items:
		opf.write(item[0] + " " + str(item[1]) + "\n")
