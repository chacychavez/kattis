'''
  Problem: 3D Printer Statue
'''
num = int(input())

i = 1
curr = 1
while(curr < num):
  curr = 1 << i
  i += 1
print(i)

