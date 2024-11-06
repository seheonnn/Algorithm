# import sys
# input = sys.stdin.readline
#
# n = int(input().strip())
# answer = []
# cnt = 0
#
# def check_beautiful():
#     i = 0
#     while i < len(answer):
#         digit = answer[i]
#
#         # answer[i:i+digit]랑 [digit] * digit이 동일하다면 아름다운 수임
#         if answer[i:i + digit] != [digit] * digit:
#             return False
#
#         # i 값 업데이트하여 다음 연속 숫자로 이동
#         i += digit
#     return True
#
# def choose(curr_num):
#     global cnt
#     if curr_num == n:
#         if check_beautiful():  # 함수 호출 수정
#             cnt += 1
#         return
#
#     # 1부터 4까지의 숫자를 선택하는 경우의 수
#     for i in range(1, 4 + 1):
#         answer.append(i)
#         choose(curr_num + 1)
#         answer.pop()
#
# choose(0)
# print(cnt)

# itertools 사용
# import itertools, sys
#
# input = sys.stdin.readline
#
# n = int(input().strip())
# cnt = 0
#
#
# def check_beautiful(sequence):
#     i = 0
#     while i < len(sequence):
#         digit = sequence[i]
#
#         # sequence[i:i+digit]와 [digit] * digit이 동일한지 확인
#         if sequence[i:i + digit] != [digit] * digit:
#             return False
#
#         # i 값 업데이트하여 다음 연속 숫자로 이동
#         i += digit
#     return True
#
#
# # 1부터 4까지의 숫자로 이루어진 리스트 생성
# elements = [1, 2, 3, 4] * n
#
# # 중복된 순열을 제거하기 위해 set 사용
# unique_permutations = set(itertools.permutations(elements, n))
#
# # 각 순열에 대해 아름다운 수인지 확인
# for perm in unique_permutations:
#     if check_beautiful(list(perm)):
#         cnt += 1
#
# print(cnt)
