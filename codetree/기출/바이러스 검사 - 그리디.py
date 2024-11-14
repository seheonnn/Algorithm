import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
c, m = map(int, input().split())
r = 0
for i in arr:
    i -= c
    r += 1

    if i > 0:
        r += (i + m - 1) // m # 직원 제외

print(r)