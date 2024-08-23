# 완전탐색 1

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

m = sys.maxsize

for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(i-j) * lst[j]
    if m > sum:
        m = sum
print(m)
