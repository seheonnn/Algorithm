from collections import deque

def bfs(hole, n, m, visited):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque()
    visited[1][1][0] = True
    queue.append((1, 1, 0, 0))
    while queue:
        x, y, k, d = queue.popleft()

        if x == n and y == m:
            return d

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or n < nx or ny < 1 or m < ny: continue
            if not visited[nx][ny][k] and (nx, ny) not in hole:
                visited[nx][ny][k] = True
                queue.append((nx, ny, k, d + 1))

        if k == 0:
            for i in range(4):
                nx = x + 2 * dx[i]
                ny = y + 2 * dy[i]
                if nx < 1 or n < nx or ny < 1 or m < ny: continue
                if not visited[nx][ny][1] and (nx, ny) not in hole:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, d + 1))

    return -1

def solution(n, m, hole):
    answer = 0
    visited = [[([False] * 2) for _ in range(m + 1)] for _ in range(n + 1)]
    return bfs(set(map(tuple, hole)), n, m, visited)