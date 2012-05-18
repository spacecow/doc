import doctest
fs = frozenset

def elapsed_time(path): return path[-1][2]
def path_actions(path): return path[1::2]

def bridge_problem(here):
  """Find the fastest (least elapsed time) path to the goal in the bridge problem.
  State will be a (peoplelight_here, peoplelight_there, time_elapsed)
  E.g. ({1,2,5,10,'light'}, {}, 0)"""
  here = fs(here) | fs(['light'])
  explored = set()
  frontier = [[(here,fs(),0)]]
  if not here or here == set(['light']): return frontier[0]
  while frontier:
    path = frontier.pop(0)
    here, _, _ = path[-1]
    if not here: return path #check for solution when we pop
    for (state,action) in bsuccessors(path[-1]).items():
      if state not in explored:
        here, there, t = state
        explored.add(state)
        npath = path + [action,state]
        #don't check for solution here
        frontier.append(npath)
        frontier.sort(key=elapsed_time)
  return []

def bsuccessors(state):
  """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
  where here and there are fss of people (indicated by their times) and/or
  the 'light', and t is a number indicating the elapsed time."""
  here, there, t = state
  if 'light' in here:
    return dict(((here - fs([a,b,'light']), there | fs([a,b,'light']), t+max(a,b)),
                 (a,b,'->'))
                for a in here if a is not 'light' for b in here if b is not 'light')
  else:
    return dict(((here | fs([a,b,'light']), there - fs([a,b,'light']), t+max(a,b)),
                 (a,b,'<-'))
                for a in there if a is not 'light' for b in there if b is not 'light')

class TestBridge: """
>>> elapsed_time(bridge_problem([1,2,5,10]))
17

## There are two equally good solutions
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

## Try some other problems
>>> path_actions(bridge_problem([1,2,5,10,15,20]))
[(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> path_actions(bridge_problem([1,2,4,8,16,32]))
[(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (1, 2, '->'), (1, 1, '<-'), (16, 32, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> [elapsed_time(bridge_problem([1,2,4,8,16][:N])) for N in range(6)]
[0, 1, 2, 7, 15, 28]

>>> [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(8)]
[0, 1, 1, 2, 6, 12, 19, 30]

"""

print doctest.testmod()
def test():
  assert bsuccessors((fs([1,'light']), fs([]), 3)) == {(fs([]),fs([1,'light']), 4):(1, 1, '->')}
  assert bsuccessors((fs([]), fs([2,'light']), 0)) == {(fs([2,'light']),fs([]), 2):(2, 2, '<-')}
  return 'tests pass'

print test() #--> tests pass
print bridge_problem([1,2,5,10])
#--> [(frozenset([1, 2, 'light', 10, 5]), frozenset([]), 0), (2, 1, '->'), 
#-->  (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), (1, 1, '<-'),
#-->  (frozenset([1, 10, 5, 'light']), frozenset([2]), 3), (5, 10, '->'),
#-->  (frozenset([1]), frozenset(['light', 2, 10, 5]), 13), (2, 2, '<-'),
#-->  (frozenset([1, 2, 'light']), frozenset([10, 5]), 15), (2, 1, '->'),
#-->  (frozenset([]), frozenset([1, 10, 2, 5, 'light']), 17)]
