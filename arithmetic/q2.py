def primeFactors(n):
  aFactor = []
  for i in range(2, n/2+1):
    while True:
      if n % i != 0:
        break
      aFactor.append(i)
      n /= i
  return aFactor

print primeFactors(315)
