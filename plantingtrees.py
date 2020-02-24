
T = int(input())
trees = [int(x) for x in input().split()]

trees.sort(reverse=True)
_max = 0
for i in range(1, len(trees) + 1):
  if trees[i - 1] + i > _max:
    _max = trees[i - 1] + i
    total = _max

print(_max + 1)