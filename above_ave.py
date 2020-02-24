'''
  Problem: Above Average
'''

C = int(input())

for i in range(C):
  grades = [int(x) for x in input().split()]
  N = grades.pop(0)
  average_grade = round(sum([x for x in grades])/N, 3)
  ave = round(len([x for x in grades if x > average_grade])/N * 100, 3)
  print("%.3f" % ave + "%")