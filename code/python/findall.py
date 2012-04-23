import re
re.findall(r"[0-9]","1+2==3")
#--> ['1','2','3']
re.findall(r"[0-9][0-9]","12345")
#--> ['12','34']
re.findall(r"[0-9]+","13 from 1 in 1776")
#--> ['13', '1', '1776'] Maximal Munch. Don't stop early. go all the way
