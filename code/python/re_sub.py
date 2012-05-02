import re
print re.sub(r"[0-9]+", "NUMBER", "22 + 33 = 55") 
#--> NUMBER + NUMBER = NUMBER
