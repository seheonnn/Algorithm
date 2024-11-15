# # 완전 탐색
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# # i, j 시작점일 때
# tets = [
#     [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], # 1x4 일자 형태
#     [(0, 1), (1, 0), (1, 1)], # 2x2 형태
#     [(1, 0), (1, 1), (2, 1)], [(0, -1), (1, -1), (1, -2)], # z자 (회전), 네 방향일 필요가 없는 이유는 다른 방향은 다른 점을 시작으로 했을 때 동일한 모양이 나오기 때문
#     [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)], # z자 (대칭)
#     [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (1, 0)], # ㄴ자 (회전)
#     [(0, 1), (1, 1), (2, 1)], [(0, 1), (0, 2), (-1, 2)],
#     [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 2)], # ㄴ자 (대칭)
#     [(1, 0), (2, 0), (0, 1)], [(1, 0), (1, 1), (1, 2)],
#     [(1, 0), (1, 1), (1, -1)], [(1, 0), (1, 1), (2, 0)], # ㅗ자 (회전)
#     [(0, -1), (1, 0), (0, 1)], [(0, 1), (-1, 1), (1, 1)]
# ]
#
# def func(x, y, tet):
#     tmp = graph[x][y] # 시작 위치는 범위 내 유효한 값
#     for dx, dy in tet:
#         nx, ny = x + dx, y + dy # 테트로미노 모양
#         if nx < 0 or n <= nx or ny < 0 or m <= ny:
#             return 0
#         tmp += graph[nx][ny] # 범위 안이라면 값 누적
#     return tmp
#
# r = 0
# for i in range(n):
#     for j in range(m):
#         for tet in tets:
#             temp = func(i, j, tet)
#             r = max(r, temp)
#
# print(r)

# dfs + 백트래킹 가지치기 이용 / 느림
import sys
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

r = 0
# lst 탐색 중인 좌표 저장 리스트
def dfs(depth, lst, cnt):
    global r
    # 네 칸만 탐색
    if depth == 4:
        if cnt > r:
            r = cnt
        return

    for x, y in lst:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue

            if (nx, ny) not in lst:
                lst.append((nx, ny))
                dfs(depth + 1, lst, cnt + graph[nx][ny])
                lst.pop()

for i in range(n):
    for j in range(m):
        dfs(1, [(i, j)], graph[i][j]) # 시작점

print(r)