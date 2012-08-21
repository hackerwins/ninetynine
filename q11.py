import itertools

def encodeModified(l):
  res = []
  for k,g in itertools.groupby(l):
    v = list(g)
    res.append(v[0] if len(v) == 1 else [k, len(v)])
  return res

print encodeModified("aaaabccaadeeee")
