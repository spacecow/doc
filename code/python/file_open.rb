# file.txt
# --------
# line 1
# line 2

f = open('file.txt', 'r')
for line in f: print line.rstrip()
# line 1
# line 2
