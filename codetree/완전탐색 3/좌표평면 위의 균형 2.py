# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     arr.append((x, y))

# r = sys.maxsize
# for i in range(0, 100, 2):
#     for j in range(0, 100, 2):

#         cnt1 = 0
#         cnt2 = 0
#         cnt3 = 0
#         cnt4 = 0

#         tmp = -sys.maxsize
#         for x, y in arr:
#             nx, ny = x-i, y-j
#             if nx > 0 and ny > 0:
#                 cnt1 += 1
#             elif nx < 0 and ny > 0:
#                 cnt2 += 1
#             elif nx < 0 and ny < 0:
#                 cnt3 += 1
#             else:
#                 cnt4 += 1
#         tmp = max(cnt1, cnt2, cnt3, cnt4) # 한 구역 점의 최대값 M
#         r = min(r, tmp) # M 중 최소값
# print(r)

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

r = sys.maxsize
for i in range(0, 100, 2):
    for j in range(0, 100, 2):

        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0

        tmp = -sys.maxsize
        for x, y in arr:
            if x > i and y > j:
                cnt1 += 1
            elif x < i and y > j:
                cnt2 += 1
            elif x < i and y < j:
                cnt3 += 1
            else:
                cnt4 += 1
        tmp = max(cnt1, cnt2, cnt3, cnt4) # 한 구역 점의 최대값 M
        r = min(r, tmp) # M 중 최소값
print(r)