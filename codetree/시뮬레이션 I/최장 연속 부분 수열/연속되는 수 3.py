# import sys
# input = sys.stdin.readline
#
# n = int(input())
# a = []
#
# for _ in range(n):
#     a.append(int(input()))
#
# cnt = 1
# m = 1
# for i in range(1, n):
#     if a[i-1] < 0:
#         if a[i] < 0:
#             cnt += 1
#         else:
#             m = max(m, cnt)
#             cnt = 1
#     elif a[i-1] > 0:
#         if a[i] > 0:
#             cnt += 1
#         else:
#             m = max(m, cnt)
#             cnt = 1
# m = max(m, cnt)
# print(m)

import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

cnt, m = 1, 1

for i in range(1, n):
    if a[i-1] * a[i] > 0: # 부호가 같다면 곱했을 때 양수임
        cnt += 1
    else:
        cnt = 1
    m = max(m, cnt)

print(m)
