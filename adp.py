'''
  Problem: A Different Problem
'''


from sys import stdin


for line in stdin:
  token = [int(x) for x in line.split()]
  print(abs(token[0] - token[1]))