# import sys
# sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline
#
# n = int(input())
# arr1 = list(map(int, input().split()))
# arr1.sort()
#
# m = int(input())
# arr2 = list(map(int, input().split()))
#
# def binary_search(target, start, end):
#     if start > end: # 탐색 범위가 없으면 종료
#         return False
#
#     mid = (start + end) // 2
#     if arr1[mid] == target:
#         return True
#     elif arr1[mid] > target:
#         return binary_search(target, start, mid - 1)
#     elif arr1[mid] < target:
#         return binary_search(target, mid + 1, end)
#
# for target in arr2:
#     if binary_search(target, 0, n-1):
#         print(1, end=" ")
#     else:
#         print(0, end=" ")

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == target:
            return True
        elif arr1[mid] > target:
            end = mid - 1
        elif arr1[mid] < target:
            start = mid + 1
    return False

for target in arr2:
    if binary_search(target, 0, n-1):
        print(1, end=" ")
    else:
        print(0, end=" ")