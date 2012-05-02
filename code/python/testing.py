import time

examples = """TWO + TWO == FOURi
A**2 + B**2 == C**2""".splitlines()

def test():
  t0 = time.clock()
  for example in examples:
    print; print 13*' ',example
    print '%6.4f sec:   %s ' % timedcall(solve, example)
  print '%6.4f tot.' % (time.clock()-t0)

test()
