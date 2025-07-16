import sys

input = sys.stdin.readline

def find(parents, a):
    if parents[a] != a:
        parents[a] = find(parents, parents[a])
    return parents[a]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    if a > b:
        parents[b] = a
    else:
        parents[a] = b

def kruskcal(parents, graph):
    total = 0
    graph.sort()
    # graph.sort(lambda x : x[0])
    for c, a, b in graph:
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            total += c
    return total

v, e = map(int, input().split())
graph = []
parents = [i for i in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

print(kruskcal(parents, graph))