#http://www.pythonchallenge.com/pc/def/ocr.html
#recognize the characters. maybe they are in the book,
#but MAYBE they are in the page source.
#
#Source contains message as comment saying: find rare
#characters in the mess below, followed by lots of junk characters

import webbrowser
import urllib
from collections import defaultdict

#Save html page as text file
source = urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/ocr.html", "source.txt")

#Open source text file
with open("source.txt") as f:
    #Create a list of all lines in the file, \n's are removed
    flist = f.read().splitlines()

#Remove unwanted lines by slicing original list, retaining only 'the mess'
llist = list(flist[37:1257])

#Counting character frequency in 'the mess'

#create empty defaultdict of int type
#see https://docs.python.org/2/library/collections.html#collections.defaultdict
char_count = defaultdict(int)

#for each character in each line add one to the defaultdict value for that character key
for item in llist:
    for char in item:
        char_count[char] += 1

#Print frequencies for each key in the defaultdict
for key in char_count:
    print "{0} : {1}".format(key, char_count[key]) 

#Printing reveals letters amoungst the mess with a frequency of 1
#Namely a,e,i,l,q,u,t and y, or equality

webbrowser.open_new("http://www.pythonchallenge.com/pc/def/equality.html")

