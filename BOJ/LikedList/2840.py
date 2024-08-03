import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
w = deque(['?'] * n)

for i in range(k):
    s, c = input().split()
    s = int(s) % n

    # deque의 rotate를 사용하여 회전 처리
    w.rotate(s)

    # 움직인 후에 화살표가 가리키는 자리(circle[0])이 '?'일 때
    if w[0] == '?':
        # 입력된 문자가 이미 존재하는 경우, 해당하는 행운의 바퀴 존재하지 않음
        if c in w:
            print('!')
            sys.exit()
        # 처음 넣는 문자일 경우, 해당 자리에 문자 넣음.
        w[0] = c
    # 화살표가 가리키는 자리가 현재 문자와 같은 경우 넘김.
    elif w[0] == c:
        continue
    # 화살표가 가리키는 자리에 현재 문자와 다른 문자가 존재함. 자리가 겹치므로 바퀴 성립 X
    else:
        print('!')
        sys.exit()

for i in w:
    print(i, end="")

