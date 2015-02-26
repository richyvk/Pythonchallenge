#Warming up - http://www.pythonchallenge.com/pc/def/0.html
#Picture of screen with 2 38 written on it
#Hint: try to change the URL address

import webbrowser

number = 2 ** 38
url = "http://www.pythonchallenge.com/pc/def/{0}.html".format(number)

webbrowser.open(url)
