import itertools

#In how many ways can five numbers be ordered?
orderings = list(itertools.permutations([1,2,3,4,5]))
print len(orderings)
#--> 120

#In how many ways can ten numbers be ordered in groups of three?
orderings = list(itertools.permutations('1234567890',3))
print len(orderings)
#--> 720
