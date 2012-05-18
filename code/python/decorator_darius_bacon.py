from functools import update_wrapper
def decorator(d):
  "Make function d a decorator: d wraps a function fn."
  return lambda fn: update_wrapper(d(fn),fn)
decorator = decorator(decorator) 
