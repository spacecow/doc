from collections import defaultdict
cache = defaultdict(int)
for c in 'abcd':
  cache[c] += 1
print cache #--> defaultdict(<type 'int'>, {'a': 1, 'c': 1, 'b': 1, 'd': 1})
