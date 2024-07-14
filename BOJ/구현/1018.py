# 구현 - 체스판 다시 칠하기

import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(sys.stdin.readline().strip())

result = []

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if graph[a][b] != 'B':
                        cnt1 += 1
                    if graph[a][b] != 'W':
                        cnt2 += 1
                else:
                    if graph[a][b] != 'W':
                        cnt1 += 1
                    if graph[a][b] != 'B':
                        cnt2 += 1

        result.append(cnt1)
        result.append(cnt2)
print(min(result))