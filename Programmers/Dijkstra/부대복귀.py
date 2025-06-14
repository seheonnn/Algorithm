import heapq


def dijkstra(n, start, dist, graph):
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, cur = heapq.heappop(pq)

        if d > dist[cur]: continue
        for next in graph[cur]:
            new_dist = d + 1
            if new_dist < dist[next]:
                dist[next] = new_dist
                heapq.heappush(pq, (dist[next], next))


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)

    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    dijkstra(n, destination, dist, graph)

    for src in sources:
        if dist[src] == float('inf'):
            answer.append(-1)
        else:
            answer.append(dist[src])

    return answer