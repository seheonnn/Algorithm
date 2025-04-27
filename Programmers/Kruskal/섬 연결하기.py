def find(parents, a):
    if a != parents[a]:
        parents[a] = find(parents, parents[a])
    return parents[a]


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def solution(n, costs):
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    totalCost = 0
    for u, v, w in costs:
        if find(parents, u) != find(parents, v):
            union(parents, u, v)
            totalCost += w

    return totalCost