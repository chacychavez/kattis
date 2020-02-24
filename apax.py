'''
  Problem: Apaxiaaaaaaaaaaaans!
'''

string = input()
length = len(string)
i = 0
while i < length - 1:
  c = string[i]
  j = i + 1
  while j < length:
    if(c == string[j]):
      string = string[:j] + string[j + 1:]
      length -= 1
    else:
      break
  i += 1
print(string)
    
