'''
  Problem: Collatz Conjecture

'''

def first(n, visited):
  while n > 1:
    n = 3 * n + 1 if n % 2 == 1 else n // 2
    visited.append(n)

def second(n, visited):
  counter = 0
  if n not in visited:
    while n > 1:
      counter += 1
      n = 3 * n + 1 if n % 2 == 1 else n // 2
      if n in visited:
        return n, counter, n
  return n, counter, n

while(True):
  _a, _b = [int(x) for x in input().split()]
  a, b = _a, _b
  if(a == 0 and b == 0):
    break
  else:
    visited = [a]
    same = 0

    first(a, visited)
    b, counter, same = second(b, visited)
    
    print(_a, "needs", visited.index(same), "steps,", _b, "needs", counter, "steps, they meet at", same)