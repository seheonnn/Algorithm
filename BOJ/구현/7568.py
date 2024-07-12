# 구현 - 덩치

import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    stack.append(list(map(int, sys.stdin.readline().split())))

result = []

for i in range(n):
    rank = 1
    for j in range(n):
        if stack[j][0] > stack[i][0] and stack[j][1] > stack[i][1]:
            rank += 1
    result.append(rank)

print(" ".join(map(str, result)))