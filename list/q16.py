def drop(l,n):
  del l[n-1::n]
  return l

print drop(['a','b','c','d','e','f','g','h','i','k'],3)
