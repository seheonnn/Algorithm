# 시간 초과
# import sys, itertools
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# for i in itertools.product(range(1, n + 1), repeat = m):
#     if list(i) == sorted(i): # 오름차순일 때만 출력
#         print(" ".join(map(str, i)))

import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())

for i in itertools.combinations_with_replacement(range(1, n + 1), m):
    if list(i) == sorted(i): # 오름차순일 때만 출력
        print(" ".join(map(str, i)))


# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# answer = []
#
# def backtracking(start):
#     if len(answer) == m:
#         print(" ".join(map(str, answer)))
#         return
#
#     for i in range(start, n + 1):
#         answer.append(i)
#         backtracking(i)   # 다음 숫자에 현재 숫자 포함 ****
#         answer.pop()
#
# backtracking(1)
