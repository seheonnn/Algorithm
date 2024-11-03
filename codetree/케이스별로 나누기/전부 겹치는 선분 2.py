import sys
input = sys.stdin.readline

n = int(input().strip())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

poss = False
for i in range(n):
    max_a = 0
    min_b = sys.maxsize
    for j in range(n):
        if i == j:
            continue
        a1, b1 = arr[j]
        max_a = max(max_a, a1)
        min_b = min(min_b, b1)

    if min_b >= max_a : # 하나라도 전부 겹치면 YES
        poss = True

print("Yes" if poss else "No")