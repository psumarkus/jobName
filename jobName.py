'''
Created on Feb 9, 2016

@author: tbrown
'''
import os
import re
from bs4 import BeautifulSoup #installation at http://www.crummy.com/software/BeautifulSoup/     $ pip install beautifulsoup4



fname = "MakerBot Innovation Center.html"
soup = BeautifulSoup(open(fname), 'html.parser') 
out = "clipboard.txt"

#print soup.prettify()

nameGetter = soup.find_all(text = re.compile("^Requestor"))[0].next
emailGetter = soup.find_all(text = re.compile("^Requestor Email"))[0].next.next.next_element
#filamentGetter = soup.find_all(text = re.compile("Filament Usage Actual"))[0].next
#notesGetter = soup.find_all(text = re.compile("^Campus"))#not yet implemented in form

print nameGetter
print emailGetter
#keep additional options out for now in case html is from rest page instead of jobs. once location parsing or printer name is added 
#print filamentGetter
#print notesGetter
#print " "#space the final frontier

#open output file for writing results
f = open(out, 'w')
    
#format extracted text for label
lineOne = (nameGetter,'\n', emailGetter, '\n', "\n Failing to add a Raft or \n Supports when preparing the \n .makerbot file is the most \n common reason for a failed print. \n Please check: \n makercommons.psu.edu/fail \n for more info.  Consultations \n can be scheduled by emailing  \n makercommons@psu.edu.")

f.writelines(lineOne)
print lineOne

f.close()

os.system("lpr o landscape -P DYMO_LabelWriter_450_Turbo clipboard.txt")
