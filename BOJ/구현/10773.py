# 구현 - 제로

import sys

stack = []

k = int(sys.stdin.readline())

for _ in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

result = 0
for i in stack:
    result += i

print(result)