'''
  Problem: Alphabet Spam
'''

from decimal import *

string = input()

lower = 0
upper = 0
symbol = 0
whitespace = 0

for i in string:
  if(i.islower()):
    lower += 1
  elif(i.isupper()):
    upper += 1
  elif(i == "_"):
    whitespace += 1
  else:
    symbol += 1

print(Decimal(whitespace)/Decimal(lower + upper + symbol + whitespace))
print(Decimal(lower)/Decimal(lower + upper + symbol + whitespace))
print(Decimal(upper)/Decimal(lower + upper + symbol + whitespace))
print(Decimal(symbol)/Decimal(lower + upper + symbol + whitespace))