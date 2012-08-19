#ugly
def flatten(l) :
   def surf(l, acc) : 
      for i in l:
         if type(i) == list:
            surf(i, acc)
         else :
            acc.append(i)
      return acc
   return surf(l, [])

print flatten([0,[1,2,3],[4,5,6],[7,8,[9]]])
