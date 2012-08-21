def rotate(l,n):
  return l[n:]+l[:n]

print rotate(['a','b','c','d','e','f','g','h'],3)
print rotate(['a','b','c','d','e','f','g','h'],-2)
