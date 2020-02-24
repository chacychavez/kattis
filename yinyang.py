'''
  Problem: Yin and Yang Stones
'''


yinyang = input()

if(yinyang.count('B') == yinyang.count('W') or len(yinyang) == 1):
  print(1)
else:
  print(0)