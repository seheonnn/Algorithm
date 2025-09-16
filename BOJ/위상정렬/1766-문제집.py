import sys, heapq  # 1번 문제가 가장 쉬운 문제 -> 우선순위큐 써야함

input = sys.stdin.readline

def bfs(n, graph, inDegree):
    answer = ""
    pq = []
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            heapq.heappush(pq, i)

    while pq:
        cur = heapq.heappop(pq)
        answer += (str(cur) + " ")
        for next in graph[cur]:
            inDegree[next] -= 1 # cur가 실행되었으므로 next의 선행조건이 줄음
            if inDegree[next] == 0:
                heapq.heappush(pq, next)
    return answer


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

print(bfs(n, graph, inDegree))