'''
  Problem: Sum Kind of Problem
'''

n = int(input())
for i in range(n):
  c, num = [int(x) for x in input().split()]
  first_n = (num / 2) * ((2 * 1) + ((num - 1) * 1))
  first_n_odd = (num / 2) * ((2 * 1) + ((num - 1) * 2))
  first_n_even = (num / 2) * ((2 * 2) + ((num - 1) * 2))

  print(c, int(first_n), int(first_n_odd), int(first_n_even))