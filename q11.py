import itertools

def encodeModified(l):
   encode = []
   for k,g in itertools.groupby(l):
      sz = len(list(g))
      encode.append(sz > 1 and "Multiple %d '%s'"%(sz,k) or "Single %s"%k)
   return encode

print encodeModified("aaaabccaadeeee")
