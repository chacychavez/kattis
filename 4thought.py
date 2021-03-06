ops_perms = [
    ["+", "+", "+"],
    ["+", "+", "-"],
    ["+", "+", "*"],
    ["+", "+", "//"],
    ["+", "-", "+"],
    ["+", "-", "-"],
    ["+", "-", "*"],
    ["+", "-", "//"],
    ["+", "*", "+"],
    ["+", "*", "-"],
    ["+", "*", "*"],
    ["+", "*", "//"],
    ["+", "//", "+"],
    ["+", "//", "-"],
    ["+", "//", "*"],
    ["+", "//", "//"],
    ["-", "+", "+"],
    ["-", "+", "-"],
    ["-", "+", "*"],
    ["-", "+", "//"],
    ["-", "-", "+"],
    ["-", "-", "-"],
    ["-", "-", "*"],
    ["-", "-", "//"],
    ["-", "*", "+"],
    ["-", "*", "-"],
    ["-", "*", "*"],
    ["-", "*", "//"],
    ["-", "//", "+"],
    ["-", "//", "-"],
    ["-", "//", "*"],
    ["-", "//", "//"],
    ["*", "+", "+"],
    ["*", "+", "-"],
    ["*", "+", "*"],
    ["*", "+", "//"],
    ["*", "-", "+"],
    ["*", "-", "-"],
    ["*", "-", "*"],
    ["*", "-", "//"],
    ["*", "*", "+"],
    ["*", "*", "-"],
    ["*", "*", "*"],
    ["*", "*", "//"],
    ["*", "//", "+"],
    ["*", "//", "-"],
    ["*", "//", "*"],
    ["*", "//", "//"],
    ["//", "+", "+"],
    ["//", "+", "-"],
    ["//", "+", "*"],
    ["//", "+", "//"],
    ["//", "-", "+"],
    ["//", "-", "-"],
    ["//", "-", "*"],
    ["//", "-", "//"],
    ["//", "*", "+"],
    ["//", "*", "-"],
    ["//", "*", "*"],
    ["//", "*", "//"],
    ["//", "//", "+"],
    ["//", "//", "-"],
    ["//", "//", "*"],
    ["//", "//", "//"],
]


def get_eq(x):
    for ops in ops_perms:
        str_lit = f"4 {ops[0]} 4 {ops[1]} 4 {ops[2]} 4"
        if eval(str_lit) == x:
            print(str_lit.replace("//", "/") + f" = {x}")
            break
    else:
        print("no solution")


n = int(input())
for _ in range(n):
    x = int(input())
    get_eq(x)
