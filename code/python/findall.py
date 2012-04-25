import re
print re.findall(r"[0-9]","1+2==3")
#--> ['1','2','3']
print re.findall(r"[0-9][0-9]","12345")
#--> ['12','34']
print re.findall(r"[0-9]+","13 from 1 in 1776")
#--> ['13', '1', '1776'] Maximal Munch. Don't stop early. go all the way
print "".join(set(re.findall(r'[A-Z]','I+I=ME')))
#--> IEM, Find all unique capital letters
