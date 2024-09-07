# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# cnt = 0
# sort_b = sorted(B) # 정렬로 아름다운 수열 비교, 중복된 수열 제외
# for i in range(n-m+1):
#     sub_a = sorted(A[i:i+m])
#     if sort_b == sub_a:
#         cnt += 1
# print(cnt)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
# 정렬로 아름다운 수열 비교, 중복된 수열 제외
for i in range(n - m + 1):
    if sorted(A[i:i + m]) == sorted(B):
        cnt += 1

print(cnt)