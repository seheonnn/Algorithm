import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
studets = [0] * (n+1)

r = -1
for _ in range(m):
    i = int(input())
    studets[i] += 1
    if studets[i] >= k:
        r = i
        break
print(r)