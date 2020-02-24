'''
  Problem: ABC
'''

A = [int(x) for x in input().split()]
a = list(input())

if a[0] > a[1]:
  if A[0] < A[1]:
    A[0], A[1] = A[1], A[0]
else:
  if A[0] > A[1]:
    A[0], A[1] = A[1], A[0]

if a[0] > a[2]:
  if A[0] < A[2]:
    A[0], A[2] = A[2], A[0]
else:
  if A[0] > A[2]:
    A[0], A[2] = A[2], A[0]

if a[1] > a[2]:
  if A[1] < A[2]:
    A[1], A[2] = A[2], A[1]
else:
  if A[1] > A[2]:
    A[1], A[2] = A[2], A[1]


print(" ".join([str(x) for x in A]))