# 변수 선언 및 입력
n = int(input())
bomb_shapes = {
    1: [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],  # 세로형 폭탄
    2: [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)],  # 십자형 폭탄
    3: [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]  # 대각선형 폭탄
}

grid = [list(map(int, input().split())) for _ in range(n)]
bomb_pos = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
bomb_types = [0] * len(bomb_pos)
ans = 0
cnt = 0

while cnt >= 0:
    if cnt == len(bomb_pos):
        # 초토화된 영역을 기록할 배열
        bombed = [[False] * n for _ in range(n)]
        destroyed = 0

        # 각 폭탄 위치와 타입에 따라 초토화 영역을 계산
        for idx in range(len(bomb_pos)):
            x, y = bomb_pos[idx]
            b_type = bomb_types[idx]
            for dx, dy in bomb_shapes[b_type]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not bombed[nx][ny]:
                    bombed[nx][ny] = True
                    destroyed += 1

        # 최대 초토화 영역 수 갱신
        ans = max(ans, destroyed)
        cnt -= 1
    else:
        bomb_types[cnt] += 1
        if bomb_types[cnt] > 3:
            bomb_types[cnt] = 0
            cnt -= 1
        else:
            cnt += 1

# 결과 출력
print(ans)
