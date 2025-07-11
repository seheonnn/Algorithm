from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(n, x, y, board, visited):
    queue = deque()
    queue.append((x, y, -1, 0))

    while queue:
        x, y, last, cost = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
            # 회전(500) + 다음칸(100)
            newCost = cost + 100 if last == -1 or last == i else cost + 600

            # 이미 방문했더라도 더 작은 Cost의 경로가 있다면 방문
            if visited[nx][ny][i] > newCost and board[nx][ny] == 0:
                visited[nx][ny][i] = newCost
                queue.append((nx, ny, i, newCost))

def solution(board):
    answer = 0
    n = len(board)
    visited = [[[float('inf') for _ in range(4)] for _ in range(n)] for _ in range(n)]

    bfs(n, 0, 0, board, visited)
    answer = min(visited[n-1][n-1])
    return answer