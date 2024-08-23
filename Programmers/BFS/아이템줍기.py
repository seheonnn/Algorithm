from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1] * (102) for _ in range(102)] # 범위 주의 ! 좌표의 최댓값 50
    for lst in rectangle:
        x1, y1, x2, y2 = lst[0] * 2, lst[1] * 2, lst[2] * 2, lst[3] * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    visited = [[0] * (102) for _ in range(102)]
    queue = deque()

    queue.append((characterX * 2, characterY * 2))
    visited[characterX * 2][characterY * 2] = 1

    dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
    while queue:
        x, y = queue.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return answer