# 구현 - 행렬 곱셈

import sys

n, m = map(int, sys.stdin.readline().split())
matrix1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

m, k = map(int, sys.stdin.readline().split())
matrix2 = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

result = [[0] * k for _ in range(n)]

for i in range(n): # 순서 주의
    for j in range(k):
        for z in range(m):
            result[i][j] += matrix1[i][z] * matrix2[z][j] # index 주의

for rows in result:
    print(" ".join(map(str, rows)))
