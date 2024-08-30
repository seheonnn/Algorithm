import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue

            # 완전탐색의 숫자가 조건과 일치하는지
            status = True
            for a, a_cnt1, a_cnt2 in arr:
                x = a // 100  # 백의 자릿수
                y = a // 10 % 10  # 십의 자릿수
                z = a % 10  # 일의 자릿수

                cnt1 = 0
                cnt2 = 0
                if x == i:
                    cnt1 += 1
                if y == j:
                    cnt1 += 1
                if z == k:
                    cnt1 += 1
                if x == j or x == k:
                    cnt2 += 1
                if y == i or y == k:
                    cnt2 += 1
                if z == i or z == j:
                    cnt2 += 1

                if cnt1 != a_cnt1 or cnt2 != a_cnt2:
                    status = False
                    break

            if status:
                cnt += 1

print(cnt)