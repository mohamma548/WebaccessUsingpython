#!/usr/bin/python
#retriving data from the url and compute the sum of the numbers
import urllib
from BeautifulSoup import *
total=0
url= raw_input("Enter the url to retrive the data:")
html= urllib.urlopen(url).read()

soup=BeautifulSoup(html)
tags= soup('span')
for tag in tags:
	total=total + int(tag.contents[0])

print "sum is:",total
	

