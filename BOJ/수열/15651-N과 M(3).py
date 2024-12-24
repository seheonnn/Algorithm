import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())

for i in itertools.product(range(1, n + 1), repeat=m): # permutaions는 기본적으로 중복 허용 X
    print(" ".join(map(str, i)))

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# answer = []
#
# def backtracking():
#     if len(answer) == m:
#         print(" ".join(map(str, answer)))
#         return
#
#     for i in range(1, n + 1):
#          # 중복 조건문 없음 ****
#         answer.append(i)
#         backtracking()    # 다음 숫자를 선택 (중복 허용)
#         answer.pop()
#
# backtracking()
