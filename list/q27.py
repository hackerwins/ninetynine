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

#diff list
def diff(l1,l2):
  return list(set(l1) - set(l2))

#group with group size
def group(l, aGrpSz):
  aPattern = []

  aG1 = combination(l,aGrpSz[0])
  for g1 in aG1:
    aRemain = diff(l,g1)
    aG2 = combination(aRemain,aGrpSz[1])
    for g2 in aG2:
      aPattern.append((g1, g2, diff(aRemain,g2)))

  return aPattern

aPattern = group(['aldo','beat','carla','david','evi','flip','gary','hugo','ida'],[2,2,5])
#for pattern in aPattern: 
#  print pattern
print "group,",[2,2,5]," pattern size:",len(aPattern)

#three group g1(2),g2(3),g3(4)
aPattern = group(['aldo','beat','carla','david','evi','flip','gary','hugo','ida'],[2,3,4])
#for pattern in aPattern: 
#  print pattern
print "group,",[2,3,4]," pattern size:",len(aPattern)

