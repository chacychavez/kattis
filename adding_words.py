from sys import stdin

data = {}


def assign(line, data):
    data[line[1]] = line[2]


def calc(line, data):
    temp = ""
    for i in line:
        if i not in ["+", "-", "="]:
            if i in data:
                temp += data.get(i)
            else:
                return "unknown"
        else:
            temp += i
    inv_mapping = {v: k for k, v in data.items()}
    final = inv_mapping.get(str(eval(temp[:-1])))
    if final:
        return final
    else:
        return "unknown"


for line in stdin.readlines():
    words = line.split()
    if words[0] == "def":
        assign(words, data)
    elif words[0] == "calc":
        print(f"{line[5:-2]} = {calc(words[1:], data)}")
    elif words[0] == "clear":
        data.clear()
