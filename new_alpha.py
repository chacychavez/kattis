'''
  Problem: A New Alphabet
'''

new_alpha = {
  'a': "@", 'b': "8",
  'c': "(", 'd': "|)",
  'e': "3", 'f': "#",
  'g': "6", 'h': "[-]",
  'i': "|", 'j': "_|",
  'k': "|<", 'l': "1",
  'm': "[]\/[]", 'n': "[]\[]",
  'o': "0", 'p': "|D",
  'q': "(,)", 'r': "|Z",
  's': "$", 't': "']['",
  'u': "|_|", 'v': "\/",
  'w': "\/\/", 'x': "}{",
  'y': "`/", 'z': "2",
}

string = input()
output = ""

for i in string:
  if i.lower() not in new_alpha:
    output += i
  else:
    output += new_alpha[i.lower()]

print(output)
