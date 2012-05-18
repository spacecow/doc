fs = frozenset

def bridge_problem(here):
  "Find the fastest (least elapsed time) path to the goal in the bridge problem."
  start = (fs(here) | fs(['light']), fs())
  return lowest_cost_search(start, bsuccessors, all_over, bcost)

def all_over(state):
  here, _ = state
  return not here or here == set('light')

def final_state(path): return path[-1]

def path_cost(path):
  "The total cost of a path (which is stored in a tuple with the final action)."
  if len(path) < 3: return 0
  _, total_cost = path[-2]
  return total_cost

def add_to_frontier(frontier,path):
  """Add path to frontier, replacing costlier path if there is one.
  (This could be done more efficiently.)"""
  old = None
  for i,p in enumerate(frontier):
    if final_state(p) == final_state(path):
      old = i
      break
  if old is not None and path_cost(frontier[old]) < path_cost(path):
    return # Old path was better; do nothing
  elif old is not None:
    del frontier[old] # Old path was worse; delete it
  # Now add the new path and re-sort
  frontier.append(path)
  frontier.sort(key=path_cost)

def lowest_cost_search(start, successors, is_goal, action_cost):
  """Return the lowest cost path, starting from start state
  and considering successors(state) => {state:action,...},
  that ends in a state for which is_goal(state) is true,
  where the cost of a path is the sum of action costs,
  which are given by action_cost(action)."""
  explored = set()
  frontier = [[start]]
  while frontier:
    path = frontier.pop(0)
    nstate = final_state(path) 
    if is_goal(nstate): return path
    explored.add(nstate)
    pcost = path_cost(path)
    for (state,action) in successors(nstate).items():
      if state not in explored:
        total_cost = pcost + action_cost(action)
        npath = path + [(action,total_cost),state]
        #don't check for solution here
        add_to_frontier(frontier,npath)
  return [] 

def bcost(action):
  """ Returns the cost (a number) of an action in the bridge problem.
  An action is an (a,b,arrow) tuple; a and b are times; arrow is a string"""
  a, b, _ = action
  return max(a,b) 

def bsuccessors(state):
  """Return a dict of {state:action} pairs. A state is a (here, there) tuple,
  where here and there are frozensets of people (indicated by their times) and/or
  the 'light."""
  here, there = state
  if 'light' in here:
    return dict(((here - fs([a,b,'light']), there | fs([a,b,'light'])), (a,b,'->'))
                for a in here if a is not 'light' for b in here if b is not 'light')
  else:
    return dict(((here | fs([a,b,'light']), there - fs([a,b,'light'])), (a,b,'<-'))
                for a in there if a is not 'light' for b in there if b is not 'light')

def test():
  assert bsuccessors((fs([1,'light']), fs([]))) == {(fs([]),fs([1,'light'])):(1, 1, '->')}
  assert bsuccessors((fs([]), fs([2,'light']))) == {(fs([2,'light']),fs([])):(2, 2, '<-')}
  here = [1,2,5,10]
  assert bridge_problem(here) == [
          (frozenset([1, 2, 'light', 10, 5]), frozenset([])), 
          ((2, 1, '->'), 2), 
          (frozenset([10, 5]), frozenset([1, 2, 'light'])), 
          ((2, 2, '<-'), 4), 
          (frozenset(['light', 10, 2, 5]), frozenset([1])), 
          ((5, 10, '->'), 14), 
          (frozenset([2]), frozenset([1, 10, 5, 'light'])), 
          ((1, 1, '<-'), 15), 
          (frozenset([1, 2, 'light']), frozenset([10, 5])), 
          ((2, 1, '->'), 17), 
          (frozenset([]), frozenset([1, 10, 2, 5, 'light']))]
  return 'test passes'

print test()
print bridge_problem([1,2,5,10])
#--> [(frozenset([1, 2, 'light', 10, 5]), frozenset([])), ((2, 1, '->'), 2),
#-->  (frozenset([10, 5]), frozenset([1, 2, 'light'])), ((2, 2, '<-'), 4),
#-->  (frozenset(['light', 10, 2, 5]), frozenset([1])), ((5, 10, '->'), 14),
#-->  (frozenset([2]), frozenset([1, 10, 5, 'light'])), ((1, 1, '<-'), 15),
#-->  (frozenset([1, 2, 'light']), frozenset([10, 5])), ((2, 1, '->'), 17),
#-->  (frozenset([]), frozenset([1, 10, 2, 5, 'light']))]
