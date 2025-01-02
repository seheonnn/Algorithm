# 참고 : https://edder773.tistory.com/210
import sys
input = sys.stdin.readline

# 조건 1 : 맵 밖으로 나가면 동작 X
# 조건 2 : 주사위는 윗면 1, 동쪽 3인 상태로 놓여있음
# 조건 3 : 가장 처음 주사위에는 모든 면이 0
# 조건 4 : 주사위를 굴렸을 때 이동한 칸의 수가 0이면 주사위 바닥면에 있는 수가 칸에 복사됨
# 조건 5 : 0이 아니면 칸에 쓰인 수가 주사위 바닥면에 복사되면서 칸에 쓰인 수는 0이 됨

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice_move = list(map(int, input().split()))
dice = [0] * 6 # 조건 3
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

# 처음 주사위 형식은 [1, 2, 3, 4, 5, 6] 조건 2
def roll(move): # 굴리기
    if move == 1: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif move == 2: # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif move == 3: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif move == 4: # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

for i in dice_move:
    nx, ny = x + dx[i-1], y + dy[i-1]
    if nx < 0 or n <= nx or ny < 0 or m <= ny: # 조건 1
        continue

    x, y = nx, ny
    roll(i)
    if board[x][y] == 0: # 조건 4
        board[x][y] = dice[5] # dice[5] : 주사위 바닥면
    elif board[x][y] != 0: # 조건 5
        dice[5] = board[x][y]
        board[x][y] = 0

    print(dice[0])