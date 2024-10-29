import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
speak = []
for _ in range(5): # 리스트 하나로 받기
    speak += list(map(int, input().split()))

def check():
    bingo = 0

    # 가로줄 확인
    for rows in board:
        if rows.count(0) == 5:
            bingo += 1

    # 세로줄 확인
    # 방법 1)
    columns = list(map(list, zip(*board))) # 세로줄로 리스트 생성
    for e in columns:
        if e.count(0) == 5:
            bingo += 1

    # 방법 2)
    # for i in range(5):
    #     cnt_bin = 0
    #     for j in range(5):
    #         if board[j][i] == 0:
    #             cnt_bin += 1
    #     if cnt_bin == 5:
    #         bingo += 1

    # 왼쪽 위에서 오른쪽 아래로 내려가는 대각선 확인
    d1 = 0
    for i in range(5):
        if board[i][i] == 0:
            d1 += 1
    if d1 == 5:
        bingo += 1

    # 오른쪽 위에서 왼쪽 아래로 내려가는 대각선 확인
    d2 = 0
    for i in range(5):
        if board[i][4 - i] == 0:
            d2 += 1
    if d2 == 5:
        bingo += 1

    return bingo

for seq in range(5 * 5):
    for i in range(5):
        for j in range(5):
            if board[i][j] == speak[seq]:
                board[i][j] = 0

    # 빙고 확인
    if check() >= 3:
        print(seq + 1)  # 0부터 시작했으므로 +1
        break
