#anonymous function
numbers = [1,2,3,4]
print filter(lambda(x):x%2==1, numbers) #--> [1, 3]

#list comprehension
print [x for x in numbers if x%2==1] #--> [1, 3]

def filter_maker1(f): return lambda a:[e for e in a if f(e)]
filter_odds = filter_maker1(lambda(x):x%2==1)
print filter_odds(numbers) #--> [1, 3]

def filter_maker2(f):
  def inner_filter(a): return filter(f,a)
  return inner_filter
filter_odds = filter_maker2(lambda(x):x%2==1)
print filter_odds(numbers) #--> [1, 3]
