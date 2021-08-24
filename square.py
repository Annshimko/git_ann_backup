#square divider
n0 = n = int(input())

if (n >= 4) and n%4 == 0:
  n //= 4

d = 3
while d*d <= n:
  while n%(d*d) == 0:
      n //= d*d

  d += 2
print (n0//n)
