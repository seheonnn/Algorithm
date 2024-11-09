import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ans = []

def print_ans():
    for el in ans:
        print(el, end=" ")
    print()

def choose(curr_num):
    if curr_num == n:
        print_ans()
        return

    for i in range(1, k+1):
        # 연속하여 같은 숫자가 3번 이상 나오지 않도록 조건 추가
        if len(ans) >= 2 and ans[-1] == ans[-2] == i:
            continue

        ans.append(i)
        choose(curr_num + 1)
        ans.pop()
choose(0)

# itertools 사용
# import sys, itertools
#
# input = sys.stdin.readline
#
# k, n = map(int, input().split())
#
# # k개의 숫자를 n번 포함하는 리스트 생성
# elements = [i for i in range(1, k + 1)] * n
#
# # 길이 n의 중복된 순열을 생성하고, 중복 제거를 위해 set 사용
# unique_permutations = set(itertools.permutations(elements, n))
#
# # 연속된 숫자가 3번 이상 나오지 않도록 필터링하여 출력
# for comb in unique_permutations:
#     valid = True
#     for i in range(2, len(comb)):
#         if comb[i] == comb[i - 1] == comb[i - 2]:  # 연속된 3개의 숫자가 같은 경우
#             valid = False
#             break
#     if valid:
#         print(" ".join(map(str, comb)))
