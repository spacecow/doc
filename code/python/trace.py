from decorators import decorator
@decorator
def trace(f):
  indent = '  '
  def _f(*args):
    signature = '%s(%s)' % (f.__name__, ', '.join(map(repr,args)))
    print '%s--> %s' % (trace.level*indent,signature)
    trace.level += 1
    try:
      result = f(*args)
      print '%s<-- %s == %s' % ((trace.level-1)*indent,signature,result)
    finally:
      trace.level -= 1
    return result
  trace.level = 0
  return _f

@trace
def fib(n): return 1 if n<=1 else fib(n-1)+fib(n-2)
fib(3)
# --> --> fib(3)
# -->   --> fib(2)
# -->     --> fib(1)
# -->     <-- fib(1) == 1
# -->     --> fib(0)
# -->     <-- fib(0) == 1
# -->   <-- fib(2) == 2
# -->   --> fib(1)
# -->   <-- fib(1) == 1
# --> <-- fib(3) == 3
