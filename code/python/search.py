import re
#Find a str where the first digit of a multi-digit number is 0
print re.search(r'\b0[0-9]','400 + 5 == 0405')
#--> <_sre.SRE_Match object at 0x7f611819f098>
