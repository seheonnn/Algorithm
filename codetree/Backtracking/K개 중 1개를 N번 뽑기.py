import sys

input = sys.stdin.readline

K, N = map(int, input().strip().split())
answer = []


def print_answer():
    for el in answer:
        print(el, end=" ")
    print()


def choose(curr_num):
    if curr_num == N:
        print_answer()
        return

    for i in range(1, K + 1):  # curr_num : 몇 번째 자리인지, 1 ~ K 중 선택
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()


choose(0)

# itertools 사용
# import sys, itertools
# input = sys.stdin.readline
#
# K, N = map(int, input().strip().split())
#
# # K개의 숫자를 N번 포함하는 리스트 생성
# elements = [i for i in range(1, K + 1)] * N
#
# # 길이 N의 순열을 생성하고 중복 제거를 위해 set 사용
# unique_permutations = set(itertools.permutations(elements, N))
#
# # 각 순열을 출력
# for comb in sorted(unique_permutations):
#     print(" ".join(map(str, comb)))

