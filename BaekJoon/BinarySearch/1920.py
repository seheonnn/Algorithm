# 이분탐색 재귀 풀이
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
import sys
def binary_search(start, end, x, A):
    if start > end:
        return 0
    mid = (start + end) // 2
    if A[mid] == x:
        return 1
    elif A[mid] > x:
        return binary_search(start, mid-1, x, A)
    else:
        return binary_search(mid+1, end, x, A)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()

for i in B:
    print(binary_search(0, N-1, i, A))


# # python 자료형 이용
# import sys
# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# B = list(map(int, sys.stdin.readline().split()))
# for i in B:
#     if i in A:
#         print(1)
#     else:
#         print(0)