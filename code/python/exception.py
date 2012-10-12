try:
  print "one" #--> one
  raise Exception("three")
  print "two"
except Exception as problem:
  print problem #--> three
