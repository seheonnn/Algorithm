# import sys
# input = sys.stdin.readline
#
# n = int(input())
# stack = []
#
# for _ in range(n):
#     tmp = list(input().split())
#
#     if tmp[0] =="push":
#         stack.append(tmp[1])
#
#     elif tmp[0] == "top":
#         if len(stack) > 0:
#             print(stack[-1])
#         else:
#             print(-1)
#
#     elif tmp[0] == "size":
#         print(len(stack))
#
#     elif tmp[0] == "empty":
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#
#     elif tmp[0] == "pop":
#         if len(stack) > 0:
#             print(stack.pop())
#         else:
#             print(-1)


import sys
from collections import deque
input = sys.stdin.readline

stack = deque()

def push(num):
    stack.append(num)

def pop():
    if size() == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if size() == 0:
        return 1
    else:
        return 0

def top():
    if size() == 0:
        return -1
    else:
        return stack[size() - 1]

n = int(input())
for _ in range(n):
    tmp = input().split()
    cmd = tmp[0]
    if cmd == "push":
        push(tmp[1])
    elif cmd == "pop":
        print(pop())
    elif cmd == "size":
        print(size())
    elif cmd == "empty":
        print(empty())
    elif cmd == "top":
        print(top())