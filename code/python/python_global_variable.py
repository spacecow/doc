god = 1
def local_func():
  global god
  god = 2
  print god
local_func()
print god
