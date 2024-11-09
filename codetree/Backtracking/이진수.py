import sys

input = sys.stdin.readline

n = int(input().strip())
answer = []

def print_answer():
    for el in answer:
        print(el, end=" ")
    print()

def choose(curr_num): # curr_num : 몇 번째 자리인지, 0 / 1 선택
    if curr_num == n:
        print_answer()
        return

    answer.append(0)
    choose(curr_num + 1)
    answer.pop()

    answer.append(1)
    choose(curr_num + 1)
    answer.pop()

    return

choose(0)

# itertools 사용
# import sys, itertools
# input = sys.stdin.readline
#
# n = int(input().strip())
# # 길이 n의 0과 1로 이루어진 리스트
# lst = [0, 1] * n
# result = itertools.permutations(lst, n)
#
# # 중복을 제거한 결과를 사전 순의 역순으로 정렬
# r = sorted(set(result), reverse=True)
#
# # 출력
# for lst in r:
#     for num in lst:
#         print(num, end=" ")
#     print()

