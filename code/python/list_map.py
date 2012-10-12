numbers = [1,2,3]
def mysquare(x): return x*x
print map(mysquare,[1,2,3]) #-->[1, 4, 9]

#lambda below is called an anonymous function
print map(lambda(x):x*x,[1,2,3]) #-->[1, 4, 9]

#list comprehension
print [x*x for x in [1,2,3]] #-->[1, 4, 9]

def map_maker1(f): return lambda(a):[f(e) for e in a]
square_map = map_maker1(lambda(x):x*x)
print square_map(numbers) #--> [1, 4, 9]

def map_maker2(f):
  def inner_map(a): return map(f,a)
  return inner_map
square_map = map_maker2(lambda(x):x*x)
print square_map(numbers) #--> [1, 4, 9]
