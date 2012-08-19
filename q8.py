#ugly
def compress (l) :
   last = l[0]
   acc = [last]
   for i in l[1:]:
      if last != i:
         acc.append(i)
         last = i
   return acc

#with itertools
import itertools
def compress (l) :
   return [k for k, v in itertools.groupby(l)]

print compress(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"])
