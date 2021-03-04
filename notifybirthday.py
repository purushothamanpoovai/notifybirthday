#!/usr/bin/env python
#Author: Purushothaman K
#To print the birthday list everyday

#Birthday list:
data={
	"0101":["karthickraja"],
	"1701":["Thulasi"],
	"2101":["Padmanagarajan"],
	"2201":["Purushothaman"],

	"0102":["Muthukumar"],
	"1802":["Vinothini"],

	"2703":["Sathiya"],

	"0204":["Neelaveni","Maharajan"],
	"0604":["Kiruthika"],
	"0904":["Karuppaiyah"],

	"2505":["Gobinath"],

	"1006":["Lakshmiprabha"],
	"1606":["aSuresh"],
	"1806":["Vijayapriya"],
	"2406":["Kannan"],
	"2906":["Edison"],
	"3006":["Suresh"],

	"1807":["Venkatesh"],
	# "1907":["Savithiri"],
	"2707":["Ram kumar","Ramya"],
	"2607":["Dayanesh"],

	"0108":["Sureshkumar"],
	"3008":['Anniversary'],

	"1809":["Vallarasu"],

	"0309":["Muthukaruppasamy"],
	"2909":["Mekala "],

	"0610":["Vijayshankar"],

	"1211":["Balaji"],

	"1412":["Hariharan"],
	"2612":["Balakrishnan"],
	"2912":["B Hari"],

#2020 batch

	"2602":["Saravanan"],

	"2706":["Prasanth"],

	"3103":["Rubinath"],
	"2103":["Ranjith"]
}

#EOD


import datetime
import time
import re

#TODO : get employ list by the birthday date/month

while True:
	print "This month birthday list:"
	for key in data:
		if(re.search("^\d\d"+datetime.datetime.now().strftime("%m")+"$",key)):
			print "\033[1;36m\t" + key[0:2] +  ":" ,"\033[1;32m" ,  ",".join(data[key])+"\033[0m"
		
	#Take today and tomorrow birthday list
	try:
		print "Today birthday\n\t", "\033[1;32m", ",".join(data[datetime.datetime.now().strftime("%d%m")]),"\033[0m"
	except KeyError:
		print "\033[1;33mNo birthday today\033[0m"
	try:
		print "Tomorrow birthday\n\t","\033[1;32m", ",".join(data[(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%d%m")]),"\033[0m" 
	except KeyError:
		print "\033[1;33mNo birthday tomorrow\033[0m"
	print "\033[0m"

	break  
	time.sleep(60*60*24)   
