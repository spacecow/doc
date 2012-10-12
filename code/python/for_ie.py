a = [10, 20, 30]
print [a[i] for i in range(len(a))] #--> [10, 20, 30]
print [e for e in a] #--> [10, 20, 30]
print [e for i,e in enumerate(a)] #--> [10, 20, 30]
