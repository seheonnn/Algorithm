import heapq


def dijkstra(n, start, graph):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, cur = heapq.heappop(pq)
        if d > dist[cur]: continue
        for next, w in graph[cur]:
            new_dist = d + w
            if dist[next] > new_dist:
                dist[next] = new_dist
                heapq.heappush(pq, (dist[next], next))

    return dist


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    from_s = dijkstra(n, s, graph)
    from_a = dijkstra(n, a, graph)
    from_b = dijkstra(n, b, graph)

    r = float('inf')
    for i in range(1, n + 1):
        if (from_s[i] != float('inf') and from_a[i] != float('inf') and from_b[i] != float('inf')):
            r = min(r, from_s[i] + from_a[i] + from_b[i])

    return r