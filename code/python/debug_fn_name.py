def debug_fn(f):
  """Return a modified function that first prints out 
  function name and arguments
  then calls the function.""" # this is the doc string
  def _f(*args):
      """ Here's the bit that prints out the name and args"""
      print "Called %s(%s)"%(f.__name__, ', '.join(map(repr, args)))
      return f(*args)
  return _f

print debug_fn.__name__
# --> debug_fn
