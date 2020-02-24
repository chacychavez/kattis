
def will_attack(aggre, calm, arrival):
  return True if 0 < arrival % (aggre + calm) <= aggre else False

A, B, C, D = [int(x) for x in input().split()]
heroes    = [int(x) for x in input().split()]

for hero in heroes:
  if will_attack(A, B, hero) and will_attack(C, D, hero):
    print("both")
  elif not will_attack(A, B, hero) and will_attack(C, D, hero):
    print("one")
  elif will_attack(A, B, hero) and not will_attack(C, D, hero):
    print("one")
  else:
    print("none")