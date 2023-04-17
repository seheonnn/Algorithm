# 피보나치 0, 1 호출 횟수 구하기
# # 시간 초과 실패
# import sys
# T = int(sys.stdin.readline())
#
# def fibonacci(n):
#     global zero_cnt
#     global one_cnt
#     if n == 0:
#         zero_cnt += 1
#         return 0
#     elif n == 1:
#         one_cnt += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for _ in range(T):
#     zero_cnt = 0
#     one_cnt = 0
#     fibonacci(int(sys.stdin.readline()))
#     print(zero_cnt, one_cnt)

# 피보나치 수열에서 각 숫자에서 0과 1을 호출하는 횟수도 피보나치임.
import sys
def fibonacci(n):
    zero_cnt = [1, 0, 1] # 0이 출력되는 횟수 리스트
    one_cnt = [0, 1, 1] # 1이 출력되는 횟수 리스트
    if n >= 3:
        for i in range(2, n):
            zero_cnt.append(zero_cnt[i-1] + zero_cnt[i])
            one_cnt.append(one_cnt[i-1] + one_cnt[i])
    print(zero_cnt[n], one_cnt[n])
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    fibonacci(n)