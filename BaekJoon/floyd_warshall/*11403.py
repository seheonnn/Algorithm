# floyd warshall
import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] != 0 and graph[k][j] != 0:
                    graph[i][j] = 1
                # # floyd warshall 기본형
                # if graph[i][j] > graph[i][k] + graph[k][j]:
                #     graph[i][j] = graph[i][k] + graph[k][j]
floyd_warshall()
for v in graph:
    print(*v) # 리스트의 값만 출력