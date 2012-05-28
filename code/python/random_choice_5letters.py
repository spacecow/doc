import string
import random
import doctest
def make_salt():
  """5 random characters
  >>> len(make_salt())
  5
  """
  return "".join(random.choice(string.letters) for _ in xrange(5))
print doctest.testmod()
