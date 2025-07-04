import heapq


def dijkstra(graph, dist, start):
    dist[start] = 0
    pq = [(dist[start], start)]
    while pq:
        d, cur = heapq.heappop(pq)

        if d > dist[cur]: continue
        for next in graph[cur]:
            new_dist = d + 1
            if new_dist < dist[next]:
                dist[next] = new_dist
                heapq.heappush(pq, (new_dist, next))


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)

    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    dijkstra(graph, dist, destination)

    for src in sources:
        if dist[src] == float('inf'):
            answer.append(-1)
        else:
            answer.append(dist[src])

    return answer