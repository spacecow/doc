import doctest

def pour(x,y,X,Y): return {((0,x+y) if x+y<=Y else (x-(Y-y),y+(Y-y))):'X->Y',
                           ((x+y,0) if x+y<=X else (x+(X-x),y-(X-x))):'Y->X'}
def empty(x,y,X,Y): return {(0,y):'empty X',(x,0):'empty Y'}
def fill(x,y,X,Y): return {(X,y):'fill X',(x,Y):'fill Y'}

def successors(x,y,X,Y):
  """Return a dict of {state:action} paris describing what can be reached
  from the (x,y) state, and how."""
  assert x<=X and y<=Y
  return dict(fill(x,y,X,Y).items() + empty(x,y,X,Y).items() + pour(x,y,X,Y).items())

def pour_problem(X,Y,goal,start=(0,0)):
  """X and Y are the capacity of the two glasses; (x,y) is current fill levels
  and represents a state. The goal is a level that can be in either glass.
  Start at the start state and follow successors until we reach the goal.
  Keep track of frontier and previously explored; fail when no frontier."""
  if goal in start: return [start]
  explored = set()
  frontier = [[start]]
  while frontier:
    path = frontier.pop(0)
    (x,y) = path[-1]
    for (state,action) in successors(x,y,X,Y).items():
      if state not in explored:
        explored.add(state)
        npath = path + [action,state] 
        if goal in state: return npath
        else: frontier.append(npath)

class Test: """
>>> pour(1,1,9,4)
{(2, 0): 'Y->X', (0, 2): 'X->Y'}
>>> pour(8,3,9,4)
{(7, 4): 'X->Y', (9, 2): 'Y->X'}

>>> empty(2,3,9,4)
{(2, 0): 'empty Y', (0, 3): 'empty X'}

>>> fill(2,3,9,4)
{(9, 3): 'fill X', (2, 4): 'fill Y'}

>>> successors(2,3,9,4)
{(9, 3): 'fill X', (1, 4): 'X->Y', (2, 0): 'empty Y', (5, 0): 'Y->X', (0, 3): 'empty X', (2, 4): 'fill Y'}
"""
print doctest.testmod() #--> TestResults(failed=0, attempted=5)

print pour_problem(9,4,6)
#--> [(0, 0), 'fill X', (9, 0), 'X->Y', (5, 4), 'empty Y', (5, 0), 'X->Y', 
#-->  (1, 4), 'empty Y', (1, 0), 'X->Y', (0, 1), 'fill X', (9, 1), 'X->Y', (6, 4)]
