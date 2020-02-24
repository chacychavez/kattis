'''
  Problem: Permutation Encryption
'''

while(True):
  x = [int(x) for x in input().split()]

  if(x[0] == 0):
    break
  else:
    string = input()
    length = x.pop(0)
    output = ""
    additional = (length - (len(string) % length)) if (len(string) % length != 0) else 0
    string += ' ' * additional
    new_x = []

    for i in range(len(string) // length):
      new_x += [y + (i * length) for y in x]

    for i in range(len(string)):
      output += string[new_x[i] - 1]

    print("\'" + output + "\'")     

