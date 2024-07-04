# Linked List - 회전하는 큐

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

queue = deque(range(1, n+1))
cnt = 0

for i in lst:
    idx = queue.index(i)
    left = idx
    right = len(queue) - idx
    if left <= right:
        queue.rotate(-left) # queue.rotate(음수) 왼쪽으로 회전
        cnt += left
    else:
        queue.rotate(right) # queue.rotate(양수) 오른쪽으로 회전
        cnt += right
    queue.popleft()

print(cnt)

# from collections import deque
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# lst = list(map(int, sys.stdin.readline().split()))
#
# queue = deque(range(1, n+1))
# cnt = 0
#
# def op1():
#     queue.popleft()
#
# def op2():
#     tmp = queue.popleft()
#     queue.append(tmp)
#
# def op3():
#     tmp = queue.pop()
#     queue.appendleft(tmp)
#
# for i in lst:
#     idx = queue.index(i)
#     left = idx
#     right = len(queue) - idx
#
#     if left <= right:
#         for _ in range(left):
#             op2()
#         cnt += left
#     else:
#         for _ in range(right):
#             op3()
#         cnt += right
#     op1()
# print(cnt)