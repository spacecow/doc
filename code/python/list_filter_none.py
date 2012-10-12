l = [1, None, 2]
"""filter return all the items in the list that match the function.
   if there is no function, match all that are not None"""
print filter(None, (e for e in l)) #--> [1, 2] 
