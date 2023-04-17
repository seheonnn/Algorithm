import sys
# 메모리 초과
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# import sys
# n = int(sys.stdin.readline())
# li = []
# for _ in range (n) :
#     li.append(int(sys.stdin.readline()))
# print(sorted(li))
# # print(sorted(li, reverse=True))

# 계수 정렬
import sys
n = int(sys.stdin.readline())
li = [0] * 10001 # 최대수는 10000
for _ in range(n):
    li[int(sys.stdin.readline())] += 1
for i in range(10001):
    if li[i] != 0:
        for _ in range(li[i]):
            print(i)
