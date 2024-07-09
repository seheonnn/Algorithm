# 구현 - 에라토스테네스의 체

# # 에라토스테네스의 체 알고리즘
# import sys
# import math
#
# n = int(sys.stdin.readline().strip())
# primes = [True] * (n+1) # 모든 수가 소수라고 가정하여 시작
# primes[0] = primes[1] = False # 0과 1은 소수가 아님
#
# for i in range(2, int(math.sqrt(n))+1): # +1 주의
#     if primes[i]:
#         for j in range(i * i, n+1, i):
#             primes[j] = False # i의 배수들은 소수가 아니다
#
# result = [i for i in range(len(primes)) if primes[i]]
# print(result)

import sys

n, k = map(int, sys.stdin.readline().split())
primes = [True] * (n + 1)
primes[0] = primes[1] = False

removed = []

for i in range(2, n + 1):
    if primes[i]:
        for j in range(i, n + 1, i): # 소수가 아닌 수부터 False -> 이후 소수들 False
            if primes[j]:
                primes[j] = False
                removed.append(j)

print(removed[k-1])
