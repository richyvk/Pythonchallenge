#What about making trans? - http://www.pythonchallenge.com/pc/def/map.html
#K => M
#O => Q
#E => G
#
#everyone thinks twice before solving this
#
#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
#bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
#sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj

#this helped me figure out maketrans: http://www.tutorialspoint.com/python/string_maketrans.htm
from string import maketrans

lettersin = "abcdefghijklmnopqrstuvwxyz"
lettersout = "cdefghijklmnopqrstuvwxyzab" #move two letters forward for each letter of the alphabet

#map lettersin to lettersout
letterstran = maketrans(lettersin, lettersout)

phrase = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj
'''

print phrase.translate(letterstran)
# => i hope you didnt translate it by hand. thats what computers are for. 
#    doing it in by hand is inefficient and that's why this text is so long. 
#    using string.maketrans() is recommended. now apply on the url

url = "map"
print url.translate(letterstran)
# => ocr
