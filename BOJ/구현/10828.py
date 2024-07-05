# 구현 - 스택

import sys

# 리스트 구현
stack = []

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
        return stack[size()-1]

n = int(sys.stdin.readline())

for _ in range(n):
    tmp = sys.stdin.readline().split()
    cmd = tmp[0]

    if cmd == "push":
        push(int(tmp[1]))
    elif cmd == "pop":
        print(pop())
    elif cmd == "size":
        print(size())
    elif cmd == "empty":
        print(empty())
    elif cmd == "top":
        print(top())
