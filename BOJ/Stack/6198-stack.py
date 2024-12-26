# 시간 초과
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input().strip()))
# cnt = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if arr[i] > arr[j]:
#             cnt += 1
#         else:
#             break
# print(cnt)

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input().strip()) for _ in range(n)]

cnt = 0
stack = []

for height in arr:
    # 스택에 있는 빌딩 중 현재 빌딩보다 낮은 빌딩들은 볼 수 없으므로 제거
    while stack and stack[-1] <= height:
        stack.pop()
    # 현재 빌딩이 스택에 있는 모든 빌딩을 볼 수 있으므로 그 수를 카운트에 추가
    cnt += len(stack)
    # 현재 빌딩을 스택에 추가
    stack.append(height)

print(cnt)
