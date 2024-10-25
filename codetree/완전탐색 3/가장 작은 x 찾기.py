import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = []
for x in range(1, 10001):
    poss = True
    cur = x
    for a, b in arr:
        cur *= 2
        if a > cur or b < cur: # 범위 벗어나면 안 됨
            poss = False

    if poss:
        print(x)
        break