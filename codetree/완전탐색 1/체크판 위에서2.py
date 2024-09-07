import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [input().split() for _ in range(r)]

cnt = 0
for i in range(1, r): # 출발지점 제외
    for j in range(1, c):
        for k in range(i+1, r - 1): # 도착지점 제외
            for l in range(j+1, c - 1):
                if graph[0][0] != graph[i][j] and graph[i][j] != graph[k][l] and graph[k][l] != graph[r-1][c-1]:
                    cnt += 1

print(cnt)