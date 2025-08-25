from collections import deque


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    parents = [0] * (n + 1)
    parents[1] = -1  # 루트
    queue = deque([1])  # 시작
    order = []

    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)

    while queue:
        cur = queue.popleft()
        order.append(cur)
        for nex in graph[cur]:
            if parents[nex] == 0:
                parents[nex] = cur
                queue.append(nex)

    sub = [1] * (n + 1)  # 서브 트리 크기 (자기 자신 포함)
    for v in reversed(order):
        p = parents[v]
        if p != -1:
            sub[p] += sub[v]

    answer = n  # 최대
    for a, b in wires:
        if parents[a] == b:
            child = a
        elif parents[b] == a:
            child = b

        diff = abs(n - 2 * sub[child])
        if diff < answer:
            answer = diff

    return answer