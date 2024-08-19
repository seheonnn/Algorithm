import sys
input = sys.stdin.readline

OFFSET = 100
MAX_R = 200
block = [0] * (MAX_R + 1)
n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    s, e = s + OFFSET, e + OFFSET

    for i in range(s, e): # 끝점이 닿는 것은 겹치는 것이 아님. [2,4]와 [4,5]는 겹치지 않음
        block[i] += 1

print(max(block))