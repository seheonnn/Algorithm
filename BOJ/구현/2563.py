# 구현 - 색종이

# 모서리 주의

import sys

graph = [[0] * 101 for _ in range(101)]

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if 0 < i and i <= 100 and 0 < j and j <= 100:
                graph[i][j] = 1

# result = 0
# for i in range(1, 101):
#     for j in range(1, 101):
#         if graph[i][j] == 1:
#             result += 1
# print(result)

result = sum(sum(row) for row in graph)
print(result)