import itertools
def encode(l) :
   return [[len(list(v)), k] for k, v in itertools.groupby(l)]

print encode("aaaabccaadeeee")
