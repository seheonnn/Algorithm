answer = 0

def backtracking(dungeons, k, n, visited, cnt):
    global answer
    answer = max(answer, cnt)

    for i in range(n):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            backtracking(dungeons, k - dungeons[i][1], n, visited, cnt + 1)
            visited[i] = False


def solution(k, dungeons):
    global answer
    n = len(dungeons)
    visited = [False] * (n)
    backtracking(dungeons, k, n, visited, 0)
    return answer