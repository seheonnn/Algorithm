# 파도반 수열의 점화식 P(N) = P(N - 1) + P(N - 5)
import sys

input = sys.stdin.readline

P = [0] * (100 + 1) # 1부터 n 최댓값까지
P[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

t = int(input())

for i in range(6, 101):
    P[i] = P[i - 1] + P[i - 5]

for _ in range(t):
    n = int(input())
    print(P[n])