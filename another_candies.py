"""
    Another Candies
"""

T = int(input())

for i in range(T):
    input()
    total = 0
    N = int(input())
    for j in range(N):
        total += int(input())
    print("YES" if total % N == 0 else "NO")
