import random

def rnd_select(l,n):
  res = []
  for i in range(0,n):
    idx = random.randint(0,len(l)-1) 
    res.append(l[idx])
    del l[idx]
  return res

print rnd_select(['a','b','c','d','e','f','g','h'],3)
