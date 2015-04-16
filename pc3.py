#http://www.pythonchallenge.com/pc/def/equality.html
#One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
#
#Again source contains large amount of text as comment.
#Page title is re so using the re module for regular expression functionality

import webbrowser, urllib, re

#Save html page as text file
source = urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/equality.html", "source.txt")

#Open and split source file (splitlines removes line breaks)
with open('source.txt') as f:
    mess = f.read().splitlines()

#Join relevant lines to create source text
text = ''.join(mess[21:-1])

#Create expression to match any lowercase letter followed by 3 uppercase bodyguards,
#then one lowercase (round brackets around it means this is whats returned), 3 more uppercase
#bodyguards and finally any lowercase
expression = re.compile('[a-z][A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]')

#Print all matches found as a word by adding them to a list then joining the list items
#I would like to find a neater solution to doing this but this works
word = []
for match in re.findall(expression, text):
    word.append(match)

#Result is 'linkedlist', open new url
webbrowser.open_new('http://www.pythonchallenge.com/pc/def/linkedlist.html')
