def mc_problem(start=(3,3,1,0,0,0),goal=None):
  """Solve the missionaries and cannibals problem.
  State is 6 ints: (M1, C1, B1, M2, C2, B2) on the start (1) and other (2) side.
  Find a path that goes from the initial state to the goal state (which, if
  not specified, is the state with no people or boats on the start side."""
  if goal is None: goal = (0,0,0) + start[:3]
  if start == goal: return [start]
  explored = set()
  frontier = [[start]]
  while frontier:
    path = frontier.pop(0)
    s = path[-1]
    for (state,action) in csuccessors(s).items():
      if state not in explored:
        explored.add(state)
        npath = path + [action,state]
        if state == goal: return npath
        else: frontier.append(npath)
 
def csuccessors(state):
  """Find successors (including ones that result in dining) to this state.
  But a state where cannibals can dine has no successors."""
  M1, C1, B1, M2, C2, B2 = state
  ## Check for state with no successors
  if C1 > M1 > 0 or C2 > M2 > 0: return {}
  if B1 > 0: items = [(sub(state,delta), a + '->') for delta,a in deltas.items()]
  if B2 > 0: items = [(add(state,delta), '<-' + a) for delta,a in deltas.items()]
  return dict(items)

def add(X,Y): return tuple(x+y for x,y in zip(X,Y))
def sub(X,Y): return tuple(x-y for x,y in zip(X,Y))

deltas = {(2,0,1,-2, 0,-1):'MM',
          (0,2,1, 0,-2,-1):'CC',
          (1,1,1,-1,-1,-1):'MC',
          (1,0,1,-1, 0,-1):'M',
          (0,1,1, 0,-1,-1):'C'}

import doctest
class TestCannibals: """
>>> csuccessors([3,3,1,0,0,0])
{(2, 3, 0, 1, 0, 1): 'M->', (3, 1, 0, 0, 2, 1): 'CC->', (3, 2, 0, 0, 1, 1): 'C->', (1, 3, 0, 2, 0, 1): 'MM->', (2, 2, 0, 1, 1, 1): 'MC->'}
>>> csuccessors([0,0,0,3,3,1])
{(0, 1, 1, 3, 2, 0): '<-C', (0, 2, 1, 3, 1, 0): '<-CC', (1, 0, 1, 2, 3, 0): '<-M', (2, 0, 1, 1, 3, 0): '<-MM', (1, 1, 1, 2, 2, 0): '<-MC'}
"""
print doctest.testmod() #--> TestResults(failed=0, attempted=2)
print mc_problem()
#--> [(3, 3, 1, 0, 0, 0),
#--> 'CC->',(3, 1, 0, 0, 2, 1),
#--> 'C->', (3, 2, 1, 0, 1, 0),
#--> 'CC->', (3, 0, 0, 0, 3, 1),
#--> 'C->', (3, 1, 1, 0, 2, 0),
#--> 'MM->', (1, 1, 0, 2, 2, 1),
#--> 'MC->', (2, 2, 1, 1, 1, 0),
#--> 'MM->', (0, 2, 0, 3, 1, 1),
#--> 'C->', (0, 3, 1, 3, 0, 0),
#--> 'CC->', (0, 1, 0, 3, 2, 1),
#--> 'C->', (0, 2, 1, 3, 1, 0),
#--> 'CC->', (0, 0, 0, 3, 3, 1)]
