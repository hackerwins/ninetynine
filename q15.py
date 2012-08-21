import itertools

def flatten(l):
  return list(itertools.chain.from_iterable(l))

def dupli(l,n):
  return flatten([[i]*n for i in l])

print dupli(['a','b','c'],3)
