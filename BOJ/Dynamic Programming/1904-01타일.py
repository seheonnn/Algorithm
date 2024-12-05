# 수열 완전 탐색으로 불가능
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1) # 길이가 i인 2진 수열의 가능한 가짓수
dp[1] = 1 # 길이가 1인 수열은 1만 가능, 00 붙어있으므로 0은 불가
if n > 1:
    dp[2] = 2 # 길이가 2인 경우 11, 00 가능

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746 # i - 1 : 수열 뒤에 1이 붙는 경우, i - 2 : 수열 뒤에 00이 붙는 경우

print(dp[n])
#
# # 피보나치 수열 방식
# # dp[N]=dp[N−1]+dp[N−2] 피보나치 수열 점화식과 동일
# import sys
# input = sys.stdin.readline
#
# n = int(input().strip())
#
# # dp 배열 대신 두 변수만 사용 (공간 최적화)
# a, b = 1, 2  # dp[1], dp[2]
#
# if n == 1:
#     print(1)
# elif n == 2:
#     print(2)
# else:
#     for i in range(3, n + 1):
#         a, b = b, (a + b) % 15746  # 피보나치 수열의 모듈러 연산
#     print(b)

# N = 1,000,000처럼 N이 큰 경우, 일반 피보나치 수열이나 피보나치 수열 + 메모제이션은 시간초과

