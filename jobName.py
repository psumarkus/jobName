'''
Created on Jan 30, 2016

@author: tbrown
'''

fname = "labelPDF.txt"
fh = open(fname)
count = -1 #only needed if line numbers need to be checked


#open txt file from automator pdf to text convert and split into individual components
for line in fh:
    words = line.split()
    size = len(words)
    
#remove funky '????' from date   
    date =[]
    date = words[0]
    labelDate = date[4:]

#format extracted text for label
    print words[40], words[35], words[36], labelDate
    print words[5], words[6], words[9], words[12], words[13]
    print "To schedule a consultation about this print, please email: makercommons@psu.edu"
    
    
# look at text file structure with line numbers to indicate item index for formatting of label
    #for word in words:
        #count = count + 1
        #print count, word
