

T, N = [int(x) for x in input().split()]
tasks = [int(x) for x in input().split()]

i = 1
total = tasks[0]
while total <= N:
  if i >= len(tasks):
    print(i)
    break
  total += tasks[i]
  i += 1
else:
  print(i - 1)