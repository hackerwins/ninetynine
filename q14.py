import itertools

def flatten(l):
  return list(itertools.chain.from_iterable(l))

def dupli(l):
  return flatten([[i,i] for i in l])

print dupli(['a','b','c','c','d'])
