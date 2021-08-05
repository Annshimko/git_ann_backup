n0 = n = int(input())
#n0 = n = 594825322637004536

if (n >= 4) and n%4 == 0:
  n //= 4

d = 3
while d*d <= n:
  while n%(d*d) == 0:
      n //= d*d

  d += 2
print (n0//n)