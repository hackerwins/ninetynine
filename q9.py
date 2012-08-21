import itertools
def pack(l):
   return [list(v) for k, v in itertools.groupby(l)]

print pack(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e'])
