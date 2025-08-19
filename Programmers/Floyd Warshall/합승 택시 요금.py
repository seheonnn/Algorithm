# 플로이드 와샬
def solution(n, s, a, b, fares):
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    # 주의
    for i in range(1, n + 1):
        dist[i][i] = 0

    for u, v, w in fares:
        dist[u][v] = w
        dist[v][u] = w

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 합승 지점 탐색
    return min(dist[s][i] + dist[i][a] + dist[i][b] for i in range(1, n + 1))