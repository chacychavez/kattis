score = 0
num_of_solved = 0
fails = dict()
penalty = 20
while True:
    str_input = input()
    if str_input == "-1":
        break
    else:
        minutes, problem, outcome = str_input.split(" ")
        if outcome == "right":
            score += int(minutes) + (penalty * fails.get(problem, 0))
            num_of_solved += 1
        else:
            if problem not in fails:
                fails[problem] = 1
            else:
                fails[problem] += 1
print(num_of_solved, score)