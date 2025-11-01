from collections import deque

def canChange(cur, target):
    cnt = sum([1 for a, b in zip(cur, target) if a != b])
    return cnt == 1

def bfs(begin, target, words):
    queue = deque()
    n = len(words)
    queue.append((begin, 0))
    visited = [False] * n

    while queue:
        cur, cnt = queue.popleft()

        if cur == target: return cnt

        for i in range(n):
            if not visited[i] and canChange(cur, words[i]):
                visited[i] = True
                queue.append((words[i], cnt + 1))
    return 0

def solution(begin, target, words):
    return bfs(begin, target, words)