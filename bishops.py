'''
  Problem: Bishops
'''

from sys import stdin

for line in stdin:
  num = int(line.split()[0])
  if num == 1:
    print(1)
  elif num == 0:
    print(0)
  elif num > 0:
    print(2 * num - 2)