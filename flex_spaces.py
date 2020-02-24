'''
  Problem: Flexible Spaces
'''

width, partition  = [int(x) for x in input().split()]
locations         = [int(x) for x in input().split()]
output            = []


locations = [0] + locations + [width]

for i in range(len(locations) - 1, -1, -1):
  for j in range(i):
    if(locations[i] - locations[j] not in output):
      output.append(locations[i] - locations[j])

print(' '.join(str(x) for x in sorted(output)))
