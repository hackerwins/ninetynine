import itertools
def encode(l) :
   print [(len(list(v)), k) for k, v in itertools.groupby(l)]

encode("aaaabccaadeeee")
