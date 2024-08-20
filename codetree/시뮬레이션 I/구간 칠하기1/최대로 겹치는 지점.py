import sys
input = sys.stdin.readline

MAX_R = 100

n = int(input())
block = [0] * (MAX_R + 1)

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1): # 끝점이 닿는 경우도 겹치는 것으로
        block[i] += 1

print(max(block))