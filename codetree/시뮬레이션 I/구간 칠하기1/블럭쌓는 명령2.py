import sys
input = sys.stdin.readline

n, k = map(int, input().split())
block = [0] * n
for _ in range(k):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        block[i-1] += 1

print(max(block))