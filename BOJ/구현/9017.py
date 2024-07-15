# 구현 - 크로스 컨트리

import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    scores = list(map(int, input().rstrip().split()))
    counter = {}
    for i in scores:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    board = {}
    tmp = 0
    for i in range(n):
        if counter[scores[i]] < 6:
            tmp += 1
            continue
        if scores[i] in board:
            board[scores[i]].append(i - tmp)
        else:
            board[scores[i]] = [i - tmp]
    print(sorted(board, key=lambda x:(sum(board[x][0:4]), board[x][4]))[0])