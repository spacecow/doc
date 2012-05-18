def odds_only(ns):
  for n in ns:
    if n%2==1: yield n
print [x for x in odds_only([1,2,3,4,5])] #--> [1, 3, 5]

#list comprehension with a guard or a predicate
print [x for x in [1,2,3,4,5] if x%2==1] #--> [1, 3, 5]
