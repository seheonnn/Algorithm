# 구현 - 상 하 좌 우

def sol():
    return

def ans():
    n = int(input())
    lst = input().split()
    x, y = 1, 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ["L", "R", "U", "D"]

    for i in lst:
        for j in range(len(move_types)):
            if i == move_types[j]:
                nx = x + dx[j]
                ny = y + dy[j]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x,y = nx, ny

    print(x, y)


ans()
