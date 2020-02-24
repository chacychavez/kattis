'''
  Problem: Radio Commercial
'''

N, P = [int(x) for x in input().split()]
arr = [int(x) - P for x in input().split()]

_max = temp_max = arr[0]

for i in arr[1:]:
  if temp_max < 0:
    temp_max = i
  else:
    temp_max += i
  if temp_max >= _max:
    _max = temp_max

print(_max)