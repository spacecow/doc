def mysquare(x): return x*x
print map(mysquare,[1,2,3]) #-->[1, 4, 9]

#lambda below is called an anonymous function
print map(lambda(x):x*x,[1,2,3]) #-->[1, 4, 9]

#list comprehension
print [x*x for x in [1,2,3]] #-->[1, 4, 9]
