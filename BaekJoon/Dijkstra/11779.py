import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = 999999

graph = [[] for _ in range(n + 1)]

d = [INF] * (n + 1)
path = [-1] * (n + 1)

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

start, end = map(int, sys.stdin.readline().split())

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    d[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < d[i[0]]:
                d[i[0]] = dist + i[1]
                path[i[0]] = now # 최소 비용 경로를 업데이트
                heapq.heappush(q, (dist + i[1], i[0]))


dijkstra(start)
print(d[end])
