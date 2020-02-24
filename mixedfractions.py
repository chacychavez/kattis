'''
  Problem: Mixed Fraction
'''

from sys import stdin

for line in stdin:
  n, d = [int(x) for x in line.split()]
  if(n != 0 and d != 0):
    print(n // d, n % d, '/', d)
  else:
    break
