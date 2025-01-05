import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향 설정 (북, 동, 남, 서)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

cnt = 0

while True:
    # 현재 위치 청소
    if graph[x][y] == 0:
        graph[x][y] = 2  # 청소 완료 표시 2
        cnt += 1
    # 주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인
    cleaned = False
    for _ in range(4):
        d = (d + 3) % 4 # 반시계 방향으로 90도 회전 ** 주의 **
        nx, ny = x + dx[d], y + dy[d]
        # 청소되지 않은 빈 칸 발견 시 해당 칸으로 이동
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny
            cleaned = True
            break # 현재 칸에서 다음으로 넘어갈 칸 정해지면 종료

    # 청소되지 않은 빈 칸이 없는 경우 후진 시도
    if not cleaned:
        # 현재 방향에서 후진
        nx, ny = x - dx[d], y - dy[d]
        # 후진할 수 없으면 작동 종료 (벽인 경우)
        if graph[nx][ny] == 1:
            break
        else:
            x, y = nx, ny  # 후진

print(cnt)
