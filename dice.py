'''
  Problem: Dice Game
'''

gunnar  = [int(x) for x in input().split()]
emma    = [int(x) for x in input().split()]

if(sum(gunnar) > sum(emma)):
  print("Gunnar")
elif(sum(gunnar) < sum(emma)):
  print("Emma")
else:
  print("Tie")