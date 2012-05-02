import time

def timedcall(fn,*args):
  "Call function with args; return the time in seconds and result."
  t0 = time.clock()
  result = fn(*args)
  t1 = time.clock()
  return t1-t0,result

def timedcalls(n, fn, *args):
  """Call fn(*args) repeatedly: n times if n is an int, or up to
  n seconds if n is a float; return the min, avg and max time."""
  if isinstance(n,int):
    times = [timedcall(fn,*args)[0] for _ in range(n)]
  else:
    times = []
    while sum(times) < n:
      times.append(timedcall(fn,*args)[0])
  return min(times), average(times), max(times)

def average(n):
  "Return the average (arithmetic mean) of a sequence of numbers."
  return sum(n) / float(len(n))

def loop(stop): 
  for _ in range(stop): pass

print timedcalls(10, loop,10**6)
#--> (0.02, 0.028, 0.04)

print timedcalls(10., loop,10**6)
#--> (0.02, 0.027, 0.04) takes 10s
