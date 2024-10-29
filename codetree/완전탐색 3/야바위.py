import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

r = 0
for i in range(1, 4):
    cup = [0] * 4
    cup[i] = 1
    cnt = 0
    for a, b, c in arr:
        tmp = cup[a]
        cup[a] = cup[b]
        cup[b] = tmp

        if cup[c] == 1:
            cnt += 1
    r = max(r, cnt)

print(r)