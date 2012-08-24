def paddingBin(n,width):
  s = bin(n)[2:]
  return "0" * (width - len(s)) + s

#use zero padding binary
def combination(l,n):
  sz = len(l)
  aBin = map(lambda x: paddingBin(x,sz), range(2**sz))
  aNthBin = filter(lambda x: x.count("1")==n, aBin)[::-1]

  aComb = []
  for nthBin in aNthBin:
    aIdx = [n for n in range(len(nthBin)) if nthBin.find("1", n) == n]
    aComb.append([l[i] for i in aIdx])
  return aComb

#test combination
print combination(['a','b','c','d','e','f'],4)

#test paddingBin
#print [paddingBin(i,5) for i in range(1,100)]
