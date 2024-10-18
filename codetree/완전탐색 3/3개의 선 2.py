import sys

input = sys.stdin.readline

MAX = 10

ans = 0

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(MAX + 1):
    for j in range(MAX + 1):
        for k in range(MAX + 1):
            # x축에 평행한 직선 3개로
            # 모든 점을 지나게 할 수 있는 경우
            success = True  # success : 직선 3개로 모든 점을 지나게 할 수 있으면 true
            for x, y in arr:
                # 해당 점이 직선에 닿는 경우
                if x == i or x == j or x == k:
                    continue
                success = False
            if success:
                ans = 1

            # x축에 평행한 직선 2개와 y축에 평행한 직선 1개로
            # 모든 점을 지나게 할 수 있는 경우
            success = True
            for x, y in arr:
                if x == i or x == j or y == k:
                    continue
                success = False
            if success:
                ans = 1

            # x축에 평행한 직선 1개와 y축에 평행한 직선 2개로
            # 모든 점을 지나게 할 수 있는 경우
            success = True
            for x, y in arr:
                if x == i or y == j or y == k:
                    continue
                success = False
            if success:
                ans = 1

            # y축에 평행한 직선 3개로
            # 모든 점을 지나게 할 수 있는 경우
            success = True
            for x, y in arr:
                if y == i or y == j or y == k:
                    continue
                success = False
            if success:
                ans = 1
print(ans)