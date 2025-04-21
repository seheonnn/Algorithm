import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
graph_reverse = [[] for i in range(n + 1)]
dist_from_x = [INF] * (n + 1)
dist_to_x = [INF] * (n + 1)

def dijkstra(graph, start, dist):
    for i in range(1, n + 1):
        dist[i] = INF
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while(pq):
        d, cur = heapq.heappop(pq)

        if (d > dist[cur]):
            continue

        for next, w in graph[cur]:
            new_dist = d + w
            if (new_dist < dist[next]):
                dist[next] = d + w
                heapq.heappush(pq, (new_dist, next))

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph_reverse[v].append((u, w))

dijkstra(graph, x, dist_from_x)
dijkstra(graph_reverse, x, dist_to_x)

r = 0
for i in range(1, n + 1):
    r = max(r, dist_from_x[i] + dist_to_x[i])

print(r)
