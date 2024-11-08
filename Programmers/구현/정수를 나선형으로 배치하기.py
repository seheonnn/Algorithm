def solution(n):
    answer = [[0] * n for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    d = 0
    x, y = 0, 0
    for i in range(1, n * n + 1):
        answer[x][y] = i
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or n <= nx or ny < 0 or n <= ny or answer[nx][ny] != 0: # 범위를 벗어나거나 이미 숫자가 채워져 있다면
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]

        x, y = nx, ny

    return answer