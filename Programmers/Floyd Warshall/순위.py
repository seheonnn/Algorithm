def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for a, b in results:
        graph[a][b] = 1  # a가 b를 이김 (단방향)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] == 1 or graph[j][i] == 1:
                cnt += 1
        if cnt == n - 1: # 나머지 모든 선수와 경기했는지
            answer += 1

    return answer