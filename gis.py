'''
    Problem: Greedy Increasing Sequence
'''
N = int(input())
A = [int(x) for x in input().split()]
out = [A[0]]

max_num = A[0]
for i in range(1, len(A)):
    if A[i] > max_num:
        out.append(A[i])
        max_num = A[i]
print(len(out))
print(" ".join([str(x) for x in out]))