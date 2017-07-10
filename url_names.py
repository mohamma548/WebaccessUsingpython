#!/usr/bin/python
#retriving the last name
# after asigning the position and count
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
count= raw_input("please enter count:")
position= raw_input("please enter the position:")
url=  raw_input("please enter url:")
counter=0
html=urllib.urlopen(url).read()
soup= BeautifulSoup(html)
tags=soup('a')
for tag in tags:
	counter= counter+1
	if counter == 18:
		url1= tag.get('href',None)
		break
print url1
print "*******************************************\n***********************"
	
	
counter=0
url=url1

while count > 0:

	html_1=urllib.urlopen(url).read()
	soup_1=BeautifulSoup(html_1)
	tags_1= soup_1('a')
	for tag_1x in tags_1:
		counter= counter+1
	        if counter == 18:
        	        url2= tag_1x.get('href',None)


			break
		
	print counter
	counter=0
	count=int(count)-1
	url=url2

	#print "here is url2:", url2
	print url
	print "##############################################"
	print count
	
	
html_11=urllib.urlopen(url).read()
soup_11=BeautifulSoup(html_1)
tags_11= soup_1('a')

for x in tags_11:

	print x.get('href',None)

