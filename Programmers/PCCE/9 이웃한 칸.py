def solution(board, h, w):
    answer = 0
    n = len(board)

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        nx, ny = h + dx[i], w + dy[i]

        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            continue
        if board[h][w] == board[nx][ny]:
            answer += 1

    return answer