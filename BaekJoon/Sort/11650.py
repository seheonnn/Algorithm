# 좌표 정렬ㄴ
n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort()
for p in points:
    print(p[0], p[1])