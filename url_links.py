#!/usr/bin/python
import urllib
from BeautifulSoup import *
url = raw_input('plear enter the url:')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

tags=soup('a')
for tag in tags:
	print tag.get('href',None)

