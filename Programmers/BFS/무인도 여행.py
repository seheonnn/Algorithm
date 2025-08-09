from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(x, y, maps, visited, n, m):
    queue = deque()
    cnt = int(maps[x][y])
    visited[x][y] = True
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or n <= nx or ny < 0 or m <= ny: continue

            if not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                cnt += int(maps[nx][ny])
                queue.append((nx, ny))

    return cnt

def solution(maps):
    answer = []

    n = len(maps)
    m = len(maps[0])
    visited = [[False] * (m) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j, maps, visited, n, m))

    return sorted(answer) if answer else [-1]