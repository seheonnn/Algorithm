import sys

INF = int(1e9)
input = sys.stdin.readline

def BellmanFord(graph, dist, start):
    dist[start] = 0
    for _ in range(n):
        for cur in range(1, n + 1):
            for next, w in graph[cur]:
                if dist[cur] != INF and dist[next] > dist[cur] + w:
                    dist[next] = dist[cur] + w

    for cur in range(1, n + 1):
        for next, w in graph[cur]:
            if dist[cur] != INF and dist[next] > dist[cur] + w:
                return True
    return False


tc = int(input())
for t in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dist = [0] * (n + 1)
    for i in range(n + 1):
        dist[i] = INF

    for i in range(m):
        s, e, t1 = map(int, input().split())
        graph[s].append((e, t1))
        graph[e].append((s, t1))

    for i in range(w):
        s, e, t1 = map(int, input().split())
        graph[s].append((e, -t1))

    r = False
    for i in range(1, n + 1):
        if dist[i] == INF:
            if BellmanFord(graph, dist, i):
                r = True
                break

    print("YES" if r else "NO")