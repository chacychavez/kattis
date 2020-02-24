'''
  Problem: Peragrams
'''

word = input()
freq = [0] * 26
count = 0
has_odd = False

for i in word:
  freq[ord(i) - ord('a')] += 1

for i in freq:
  if(i != 0 and i % 2 != 0 and has_odd):
    count += 1
  elif(i % 2 != 0 and not has_odd):
    has_odd = True

print(count) 