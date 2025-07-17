import sys, heapq

input = sys.stdin.readline


def prim(start, graph, visited):
    pq = []
    total = 0
    heapq.heappush(pq, (0, start))

    while pq:
        d, cur = heapq.heappop(pq)

        if visited[cur]: continue
        visited[cur] = True
        total += d
        for next, w in graph[cur]:
            if visited[next] == False:
                heapq.heappush(pq, (w, next))
    return total


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

print(prim(1, graph, visited))