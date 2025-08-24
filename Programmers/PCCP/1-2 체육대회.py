def backtracking(n, m, ability, visited, total, idx):
    global answer
    if idx == m:
        answer = max(answer, total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtracking(n, m, ability, visited, total + ability[i][idx], idx + 1)
            visited[i] = False

def solution(ability):
    global answer
    answer = 0
    n = len(ability)
    m = len(ability[0])
    visited = [False] * n
    backtracking(n, m, ability, visited, 0, 0)
    return answer