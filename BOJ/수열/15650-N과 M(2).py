import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())

for i in itertools.permutations(range(1, n + 1), m):
    if list(i) == sorted(i): # 오름차순일 때만 출력
        print(" ".join(map(str, i)))
#
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
#     for i in range(start, n + 1):  # 오름차순을 유지하기 위해 `start`부터 시작
#         answer.append(i)
#         backtracking(i + 1)  # 다음 숫자는 `i+1`부터 선택 ****
#         answer.pop()
#
# backtracking(1)
