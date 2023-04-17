# 8x8 체스판 만들기

import sys
N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board+=(sys.stdin.readline().split())
minCnt = N * M
for i in range(N-7):
    for j in range(M-7):
        cntW = 0 # 맨 왼쪽 위 칸이 흰색인 체스판을 만들 때 칠해야 하는 정사각형 개수
        cntB = 0 # 맨 왼쪽 위 칸이 검은색인 체스판을 만들 때 칠해야 하는 정사각형 개수
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] == "B":
                        cntW += 1
                    else:
                        cntB += 1
                else:
                    if board[x][y] == "B":
                        cntB += 1
                    else:
                        cntW += 1
        count = min(cntW, cntB)
        if count <= minCnt:
            minCnt = count
print(minCnt)

