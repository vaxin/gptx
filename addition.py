n = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

m = {}
for i in range(0, len(n) - 1):
  m[n[i]] = n[i+1]

def next(x):
  if x not in m:
    return None
  else:
    return m[x]

def end(x):
  return x is None

def count(x):
  p, v1 = int(x / 10), x % 10
  v2 = next(v1)
  if end(v2):
    p = count(p)

  x = p * 10 + v2

  return x

x = 0

for i in range(200):
  x = count(x)
  print(x)
