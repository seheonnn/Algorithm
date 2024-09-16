# import sys
# input = sys.stdin.readline

# k, n = map(int, input().split())
# arrs = [list(map(int, input().split())) for _ in range(k)]

# r = -sys.maxsize
# ans = 0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             continue
#         cnt = 0

#         for arr in arrs:
#             if arr.index(i) <= arr.index(j):
#                 cnt += 1

#         if r == cnt:
#             ans += 1
#         elif r < cnt:
#             r = cnt
#             ans = 1
# print(ans)

import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arrs = [list(map(int, input().split())) for _ in range(k)]

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue

        correct = True
        for arr in arrs:
            # 한 번이라도 i 개발자가 j 개발자보다 뒤에 있다면 correct를 False로 바꿈
            if arr.index(i) > arr.index(j):
                correct = False

        if correct:
            ans += 1

print(ans)
