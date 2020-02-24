'''
  Problem: Secret Message
'''
import math

test_case = int(input())

for i in range(test_case):
  string = input()
  output = ""

  nearest_sqrt = math.ceil(math.sqrt(len(string)))
  
  string += '*' * (nearest_sqrt * nearest_sqrt - len(string))

  string = string[::-1]

  j = nearest_sqrt - 1
  count = 0
  k = 0
  while k < len(string):
    output += string[j % len(string)]
    count += 1
    j += nearest_sqrt
    if(count == nearest_sqrt):
      j -= 1
      count = 0
    k += 1

  print(output.replace("*", ""))