# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# max_sum = 0
# for i in range(n):
#     for j in range(n-2):
#         for x in range(n):
#             if i == x:
#                 for y in range(j+3, n-2):
#                     max_sum = max(max_sum, graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[x][y] + graph[x][y+1] + graph[x][y+2])
#             else:
#                 for y in range(n-2):
#                     max_sum = max(max_sum, graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[x][y] + graph[x][y+1] + graph[x][y+2])
# print(max_sum)

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for i in range(n):
    for j in range(n-2):
        for x in range(n):
                for y in range(n-2):
                    if i == x and abs(j-y) <= 2: # 겹치는 경우
                        continue
                    max_sum = max(max_sum, graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[x][y] + graph[x][y+1] + graph[x][y+2])
print(max_sum)