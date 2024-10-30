import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
r = 0
for i in range(n):
    sum_el = 0
    cur = i
    for _ in range(m):
        sum_el += arr[cur]
        cur = (arr[cur]-1) % n
    r = max(r, sum_el)
print(r)