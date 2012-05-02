def ints(start,end=None):
  i = start
  while i <= end or end is None:
    yield i
    i += 1

L = ints(0,10**6)
print L
#--> <generator object ints at 0x7fe4f0613960>
print next(L)
#--> 0

#As part of the for protocol the generator function returned will be called
#each time we want the next item in the sequence
def c(sequence):
  """Generate items in sequence; keeping counts as we go. c.starts is the
  number of sequences started; c.items is number of items generated."""
  c.starts += 1
  for item in sequence:
    c.items += 1
    yield item

for item in c(list): pass
