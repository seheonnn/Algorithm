# 적어도 M미터의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값.
import sys

def binary_search(trees, M, start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    total = sum([tree - mid if tree > mid else 0 for tree in trees])
    if total >= M:
        return binary_search(trees, M, mid + 1, end)
    else:
        return binary_search(trees, M, start, mid - 1)

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(trees)
result = binary_search(trees, M, start, end)
print(result)