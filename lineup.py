'''
  Problem: Line Them Up
'''


n = int(input())
_list = []

for i in range(n):
  _list.append(input())


trend = "DECREASING" if _list[0] > _list[1] else "INCREASING"

for i in range(1, n - 1):
  if _list[i] < _list[i + 1] and trend == "INCREASING":
    continue
  elif _list[i] > _list[i + 1] and trend == "DECREASING":
    continue
  else:
    trend = "NEITHER"

print(trend)

