# 구현 - 집합

import sys

m = int(sys.stdin.readline())
s = set()

def add(x):
    s.add(x)

def remove(x):
    if x in s:
        s.remove(x)

def check(x):
    if x in s:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)

def all():
    # 전역 변수 주의
    global s
    s = set(range(1, 21))

def empty():
    global s
    s = set()

for _ in range(m):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "add":
        add(int(cmd[1]))
    elif cmd[0] == "remove":
        remove(int(cmd[1]))
    elif cmd[0] == "check":
        check(int(cmd[1]))
    elif cmd[0] == "toggle":
        toggle(int(cmd[1]))
    elif cmd[0] == "all":
        all()
    elif cmd[0] == "empty":
        empty()
