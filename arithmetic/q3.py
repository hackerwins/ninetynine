def primeFactorsMulti(n):
  hFreq = {}
  for i in range(2, n/2+1):
    while True:
      if n % i != 0:
        break
      if not hFreq.has_key(i):
        hFreq[i] = 0
      hFreq[i] += 1
      n /= i
  return [[k,v] for k,v in hFreq.iteritems()] 

print primeFactorsMulti(315)
