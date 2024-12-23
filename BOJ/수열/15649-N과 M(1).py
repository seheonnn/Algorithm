import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())

for i in itertools.permutations(range(1, n + 1), m): # permutaions(리스트, 수열 길이)
    print(" ".join(map(str, i)))

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# answer = []
#
# def backtracking():
#     if len(answer) == m:  # 수열의 길이가 m이 되면 출력
#         print(" ".join(map(str, answer)))
#         return
#
#     for i in range(1, n + 1):  # 1부터 N까지 숫자를 순회
#         if i not in answer:  # 중복을 허용하지 않음 ****
#             answer.append(i)
#             backtracking()  # 다음 숫자를 선택
#             answer.pop()  # 백트래킹: 마지막 숫자 제거
#
# backtracking()
