for x in items: print x

#python does the conversion
it = iter(items)
try:
  while True:
    x = next(it)
    print x
except StopIteration:
  pass 
