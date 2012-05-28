import random
def dierolls():
  while True: yield random.randint(1,6)
for _ in range(5): print next(dierolls()) #5 random numbers
