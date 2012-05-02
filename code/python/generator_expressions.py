def sq(x): print 'sq called', x; return x*x
g = (sq(x) for x in range(10) if x%2 == 0)
next(g)
#--> sq called 0
next(g)
#--> sq called 2
next(g)
#--> sq called 4
next(g)
#--> sq called 6
next(g)
#--> sq called 8
next(g)
#..> ...
#--> StopIteration

#To not bother dealing with the StopIteration, use a for-loop
for x2 in (sq(x) for x in range(10) if x%2 == 0): pass
#--> sq called 0
#--> sq called 2
#--> sq called 4
#--> sq called 6
#--> sq called 8

print list((sq(x) for x in range(10) if x%2 == 0))
#--> sq called 0
#--> sq called 2
#--> sq called 4
#--> sq called 6
#--> sq called 8
#--> [0, 4, 16, 36, 64]
