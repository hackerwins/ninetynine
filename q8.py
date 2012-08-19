#with itertools
import itertools
def compress (l) :
   return [k for k, v in itertools.groupby(l)]

print compress(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"])
