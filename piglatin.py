'''
  Problem: Pig Latin
'''

from sys import stdin

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
punctuations = ['.', '?']
for line in stdin:
  tokens = line.split()
  for i in range(len(tokens)):
    if(tokens[i][0] in vowels):
      tokens[i] += "yay"
    else:
      x = 0
      for c in tokens[i]:
        if(c in vowels):
          break
        x += 1
      first = tokens[i][:x]
      tokens[i] = tokens[i][x:] + first + "ay"
  print(" ".join(tokens))