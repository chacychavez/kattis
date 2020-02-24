'''
  Problem: Paul Eigon
'''

N, P, Q = [int(x) for x in input().split()]

if((P + Q) // N % 2 == 1):
  print('opponent')
else:
  print('paul')