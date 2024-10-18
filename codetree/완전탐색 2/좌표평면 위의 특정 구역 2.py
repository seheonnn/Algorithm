import sys

input = sys.stdin.readline

INT_MAX = sys.maxsize

arr = []
n = int(input().strip())
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = INT_MAX

for i in range(n):
    min_x, max_x = INT_MAX, 1
    min_y, max_y = INT_MAX, 1

    for j, (x, y) in enumerate(arr):
        if j == i: # i 번 째 점을 제외하고 계산해 보기
            continue

        # 남은 점들의 최대, 최소를 구하여 직사각형 넓이 계산
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    ans = min(ans, (max_x - min_x) * (max_y - min_y))

print(ans)