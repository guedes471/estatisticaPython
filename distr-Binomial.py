def fact(n):
  if(n == 0 or n == 1):
    return 1
  else:
    return n * fact(n - 1)

def comb(n ,k):
  if(k == 0 or k == n):
    return 1
  if(k == 1):
    return n
  num = n
  dif = n - k
  res1 = n


  while (num > dif + 1):
    res1 = res1 * (num - 1)
    num= num - 1

  return res1 / fact(k)

def distrib(k, n, p):
  return comb(n,k) * (p**k) * ((1 - p) ** (n - k))


