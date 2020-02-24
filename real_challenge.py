'''
  Problem: A Real Challenge
'''

from decimal import *

getcontext().prec = 50

n = Decimal(input())
print(Decimal(n).sqrt() * 4)