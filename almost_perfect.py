'''
  Problem: Almost Perfect
'''
import math
from sys import stdin

for line in stdin:
  num = int(line.split()[0])

  nearest_sqrt = round(math.sqrt(num))
  curr = 2
  divs = [1]

  while(curr <= nearest_sqrt):
    if(num % curr == 0):
      quot = num // curr
      divs.append(curr)

      if(quot != curr):
        divs.append(quot)

    curr += 1
    
  if(sum(divs) == num):
    print(num, "perfect")
  elif(0 <= abs(num - sum(divs)) <= 2):
    print(num, "almost perfect")
  else:
    print(num, "not perfect")