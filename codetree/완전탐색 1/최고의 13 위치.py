import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
for i in range(n):
    for j in range(n-2): # 셋 씩 짝을 지었을 때 범위 밖으로 나가면 안 됨
        max_cnt = max(max_cnt, graph[i][j] + graph[i][j+1] + graph[i][j+2])

print(max_cnt)