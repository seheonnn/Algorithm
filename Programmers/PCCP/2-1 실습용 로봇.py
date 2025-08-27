def solution(command):
    d = 0
    x, y = 0, 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for com in command:
        if com == 'R':
            d = (d + 1) % 4
        elif com == 'L':
            d = (d + 4 - 1) % 4
        elif com == 'G':
            x, y = x + dx[d], y + dy[d]
        elif com == 'B':
            x, y = x - dx[d], y - dy[d]

    return [x, y]