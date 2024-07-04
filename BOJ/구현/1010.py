# 다리 놓기 - 1010
# n C k = n! / (n-k)! k!구

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

import sys
T = int(sys.stdin.readline())

# nCk
for _ in range(T):
    a = list(map(int, sys.stdin.readline().split()))
    n = a[1]
    k = a[0]
    ans = factorial(n) / (factorial(n-k) * factorial(k))
    print(int(ans))
