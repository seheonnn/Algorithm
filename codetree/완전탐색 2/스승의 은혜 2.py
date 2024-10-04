# import sys
# input = sys.stdin.readline

# n, b = map(int, input().split())
# p = [int(input()) for _ in range(n)]

# p.sort()
# r = 0

# for i in range(n):
#     tmp = b
#     cnt = 0
#     tmp -= p[i] // 2

#     for j in range(n):
#         if i == j:
#             continue
#         if tmp >= p[j]:  # 선물의 값이 예산보다 크다면 구입
#             tmp -= p[j]
#             cnt += 1
#         else:
#             break
#     cnt += 1
#     r = max(r, cnt)
# print(r)


import sys
input = sys.stdin.readline

n, b = map(int, input().split())
p = [int(input()) for _ in range(n)]

ans = 0

for i in range(n):
    tmp = p.copy()
    tmp[i] /= 2

    tmp.sort()

    student = 0
    cnt = 0

    for j in range(n):
        if cnt + tmp[j] > b: # cnt : 현재까지 쓴 돈
            break
        cnt += tmp[j]
        student += 1

    ans = max(ans, student)

print(ans)