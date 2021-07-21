#!/usr/bin/python2

import cgi 
import commands
import os
#bgroup=cgi.FormContent('city')[0]
bgroup="A+"
city=[]
getdata="curl -X GET 127.0.0.1:3001/blocks -H 'Content-Type: application/json'"
#dat=commands.getoutput(getdata).split('\n')[3]
fh=open('/home/abhishek/new.txt','r')
dat=fh.read()
 

for value in dat:
	templist=value['data'].split('_')
	if templist[0]==bgroup:
		if templist.count(templist[2])==0:
			city.append(templist[2])
print city


