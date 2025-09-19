def solution(park, routes):
    dic = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    n = len(park)
    m = len(park[0])
    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x, y = i, j
                break

    for route in routes:
        cmd, w = route.split()
        w = int(w)
        dx, dy = dic[cmd]
        valid = True
        nx, ny = x, y
        for _ in range(w):
            nx += dx
            ny += dy
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                valid = False
                break
            if park[nx][ny] == 'X':
                valid = False
                break
        if valid:
            x, y = nx, ny

    return [x, y]