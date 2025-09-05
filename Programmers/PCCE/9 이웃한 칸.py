def solution(board, h, w):
    answer = 0
    dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
    n = len(board)
    m = len(board[0])
    cnt = 0
    for i in range(4):
        nx, ny = h + dx[i], w + dy[i]
        if nx < 0 or n <= nx or ny < 0 or m <= ny: continue
        if board[h][w] == board[nx][ny]:
            answer += 1
    return answer