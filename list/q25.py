import random

def rnd_permu(l):
  res = []
  for i in range(0,len(l)):
    idx = random.randint(0,len(l)-1) 
    res.append(l[idx])
    del l[idx]
  return res

print rnd_permu(['a','b','c','d','e','f'])
