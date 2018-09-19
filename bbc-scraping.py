
from bs4 import BeautifulSoup
from urllib.request import urlopen, quote
import re
import csv

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context


with open('bbclinks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    links_list = []
    for row in csv_reader:
    	links_list.append(row)
    	print(str(row))

# Find story body
def match_class(target):                                                        
    def do_match(tag):                                                          
        classes = tag.get('class', [])                                          
        return all(c in classes for c in target)                                
    return do_match                                                         

# Removes HTML markers
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# Creates text file for each article
count = 1

for link in links_list:
	page = urlopen(link[0])
	soup = BeautifulSoup(page.read(), "html.parser")
	htmlBody = str(soup.find_all(match_class(["story-body"])))

	try:
		file = open("BBC/bbcnewsdata%s.txt" % count, "w") 
		file.write(cleanhtml(htmlBody))
		file.close()
	
	except:
		print ("Error with " + url)

	count += 1




