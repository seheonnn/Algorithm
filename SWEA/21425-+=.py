# # 시간 초과
# t = int(input())
#
# for _ in range(t):
#     a, b, n = map(int, input().split())
#     if a > b:
#         x, y = b, a
#     else:
#         x, y = a, b
#     cnt = 1
#     while True:
#         x += y
#         if x > n:
#             break
#         cnt += 1
#
#     print(cnt)

t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())
    cnt = 0
    while max(a, b) <= n:
        if a > b:
            b += a
        else:
            a += b
        cnt += 1
    print(cnt)
