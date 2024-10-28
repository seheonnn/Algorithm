# import sys
# input = sys.stdin.readline

# a, b, c = map(int, input().split())

# a1 = c // a
# b1 = c // b

# r = 0
# s = 0
# for i in range(a1+1):
#     for j in range(b1+1):
#         if (a * i) + (b * j) <= c:
#             s = (a * i) + (b * j)
#         else:
#             continue
#     r = max(r, s)
# print(r)

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

ans = 0
for i in range(c // a + 1):
    cnt = a * i

    num_b = (c - cnt) // b  # a를 i회 더한 후 남은 값

    cnt += num_b * b

    ans = max(ans, cnt)
print(ans)