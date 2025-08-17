def dfs(graph, visited, cur, answer):
    for next in graph.get(cur, []):  # 도착지는 ticketsMap에 없음. Python 에선 KeyError
        if visited[cur][next] > 0:
            visited[cur][next] -= 1
            dfs(graph, visited, next, answer)

    answer.append(cur)


def solution(tickets):
    answer = []

    ticketsMap = {}
    visited = {}
    for src, des in tickets:
        ticketsMap.setdefault(src, [])
        ticketsMap[src].append(des)

        visited.setdefault(src, {})
        visited[src].setdefault(des, 0)
        visited[src][des] += 1

    for src in ticketsMap:
        ticketsMap[src].sort()

    dfs(ticketsMap, visited, "ICN", answer)

    return answer[::-1]  # 재귀는 반대로 저장
