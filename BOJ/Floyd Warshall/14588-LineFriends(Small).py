import sys

input = sys.stdin.readline

INF = float('inf')
n = int(input())
dist = [[INF] * (n) for _ in range(n)]
arr = []
for i in range(n):
    l, r = map(int, input().split())
    arr.append((l, r))
    dist[i][i] = 0

for i in range(n):
    for j in range(i + 1, n):
        l1, r1 = arr[i]
        l2, r2 = arr[j]

        if not (r1 < l2 or r2 < l1):
            dist[i][j] = 1
            dist[j][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    result = dist[a][b] if dist[a][b] != INF else -1
    print(result)