'''
  Problem: Height Ordering

'''

def count_steps(arr):
  count = 0
  for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
      if(arr[j] > arr[j + 1]):
        count += 1
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return count

n = int(input())

for i in range(n):
  arr = [int(x) for x in input().split()]
  c = arr[0]
  arr = arr[1:]
  print(c, count_steps(arr))