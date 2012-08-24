import random

def rnd_select(n,m):
  res = []
  l = range(1,m+1)
  for i in range(0,n):
    idx = random.randint(0,len(l)-1) 
    res.append(l[idx])
    del l[idx]
  return res

print rnd_select(6,49)
