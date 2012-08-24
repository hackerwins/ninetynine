def lsort(l):
  return sorted(l, key=lambda x:len(x))

def ifsort(l):
  hFreq = {}
  for item in l:
    sz = len(item)
    if not hFreq.has_key(sz):
      hFreq[sz] = 0
    hFreq[sz] += 1

  return sorted(l, key=lambda x:hFreq[len(x)])
  
print lsort([['a','b','c'],['d','e'],['f','g','h'],['d','e'],['i','j','k','l'],['m','n'],['o']])
print ifsort([['a','b','c'],['d','e'],['f','g','h'],['d','e'],['i','j','k','l'],['m','n'],['o']])
