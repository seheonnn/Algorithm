r = 0

def dfs(cur, info, graph, sheep, wolf, next_nodes):
    global r

    if info[cur] == 0:
        sheep += 1
    else:
        wolf += 1

    if wolf >= sheep: return

    r = max(r, sheep)

    candidates = next_nodes
    for next in graph[cur]:
        candidates.append(next)

    for i in range(len(candidates)):
        next = candidates.copy()  # == candidates[:] 얕은 복사
        next.pop(i)
        dfs(candidates[i], info, graph, sheep, wolf, next)


def solution(info, edges):
    global r
    n = len(info)
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    dfs(0, info, graph, 0, 0, [])
    return r