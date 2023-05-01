import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[N for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    graph[i][j] = 0 # 자기 자신과는 친구관계 불가
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

floyd_warshall()
bacon = []
for row in graph:
    bacon.append(sum(row))
print(bacon.index(min(bacon)))