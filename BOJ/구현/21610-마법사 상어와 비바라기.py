import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
directions = [list(map(int, input().split())) for _ in range(m)]

# 방향 설정 (←, ↖, ↑, ↗, →, ↘, ↓, ↙)
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름 위치
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for d, s in directions:
    d -= 1  # 방향 인덱스 조정
    s %= n  # 이동 칸 수를 n으로 나눈 나머지로 계산 (범위 넘어가면 순환되어야 함)

    # 1. 구름 이동 및 물 증가
    new_clouds = []
    for x, y in clouds:
        nx, ny = (x + s * dx[d]) % n, (y + s * dy[d]) % n
        graph[nx][ny] += 1
        new_clouds.append((nx, ny))

    # 2. 물복사 버그 처리
    not_cloud = set(new_clouds)  # 물복사 제외할 위치 저장
    for x, y in new_clouds:
        cnt = 0
        for i in range(1, 8, 2):  # 대각선 방향으로 물 확인
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                cnt += 1
        graph[x][y] += cnt

    # 3. 새 구름 생성
    clouds = []
    for x in range(n):
        for y in range(n):
            if (x, y) not in not_cloud and graph[x][y] >= 2:
                clouds.append((x, y))
                graph[x][y] -= 2

# 최종 결과 계산
r = 0
for rows in graph:
    r += sum(rows)
print(r)
