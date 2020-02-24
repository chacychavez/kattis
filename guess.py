
lower = 1
upper = 1001
mid = upper // 2

guesses = 0
while guesses < 10:
  print(mid)
  response = input()
  if response == "lower":
    upper = mid
    mid = (lower + upper) // 2
  elif response == "higher":
    lower = mid
    mid = (lower + upper) // 2
  elif response == "correct":
    break
  guesses += 1