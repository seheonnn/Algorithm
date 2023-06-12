import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = 999999

graph = [[] for _ in range(n + 1)]

d = [INF] * (n + 1)

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
                heapq.heappush(q, (dist + i[1], i[0]))


dijkstra(start)
print(d[end])
print("d:", d)
print(graph)
