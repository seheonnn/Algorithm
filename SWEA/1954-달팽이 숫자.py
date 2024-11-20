# t = int(input())
#
# for _ in range(t):
#     l, r = map(int, input().split())
#     # Check if R >= 2 * L - 1
#     if r >= 2 * l - 1: # 조건에 만족하면 mod X를 적용했을 때 x / 2보다 큰 N이 발생함
#         print("no")
#     else:
#         print("yes")
#
#
# # 3
# # 1 2
# # 3 4
# # 100 150
#


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
T = int(input())
for t in range(1, T + 1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    nd = 0
    x, y = 0, 0
    for i in range(1, n * n + 1):
        graph[x][y] = i
        nx, ny = x + dx[nd], y + dy[nd]
        if nx < 0 or n <= nx or ny < 0 or n <= ny or graph[nx][ny] != 0:
            nd = (nd + 1) % 4
            x, y = x + dx[nd], y + dy[nd]
        else:
            x, y = nx, ny
    print("#"+str(t))
    for rows in graph:
        for el in rows:
            print(el, end=" ")
        print()

# 2
# 3
# 4