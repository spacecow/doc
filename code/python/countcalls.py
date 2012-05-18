from __future__ import division
from decorators import decorator,memo

@decorator
def countcalls(f):
  def _f(*args):
    callcounts[_f] += 1
    return f(*args)
  callcounts[_f] = 0
  return _f 
callcounts = {}

prev_calls = 1
for n in range(32):
  @countcalls
  def fib(n): return 1 if n<=1 else fib(n-1) + fib(n-2)
  result,calls = fib(n),callcounts[fib]
  print '%2d %7d %8d %1.4f' % (n,result,calls,calls/prev_calls)
  prev_calls = calls
# ...
# --> 30 1346269  7049123 1.6180
# --> 31 2178309 11405740 1.6180

for n in range(32):
  @countcalls
  @memo
  def fib(n): return 1 if n<=1 else fib(n-1) + fib(n-2)
  result,calls = fib(n),callcounts[fib]
  print '%2d %7d %8d %1.4f' % (n,result,calls,calls/prev_calls)
  prev_calls = calls
# ...
# --> 30 1346269       59 1.0351
# --> 31 2178309       61 1.0339




