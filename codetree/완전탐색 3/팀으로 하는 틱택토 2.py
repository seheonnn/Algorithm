import sys

input = sys.stdin.readline

MAX_A = 3
MAX_X = 9

arr = [list(map(int, input().strip())) for _ in range(MAX_A)]

ans = 0

for i in range(1, MAX_X + 1):
    for j in range(i + 1, MAX_X + 1):
        win = False

        num_i = 0
        num_j = 0

        # 가로로 빙고가 만들어질 때
        for k in range(MAX_A):
            num_i = 0
            num_j = 0
            for l in range(MAX_A):
                if arr[k][l] == i:
                    num_i += 1
                if arr[k][l] == j:
                    num_j += 1
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

        # 세로로 빙고가 만들어질 때
        for k in range(MAX_A):
            num_i = 0
            num_j = 0
            for l in range(MAX_A):
                if arr[l][k] == i:
                    num_i += 1
                if arr[l][k] == j:
                    num_j += 1

            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

        # 왼쪽 위에서 오른쪽 아래를 잇는 대각선으로 빙고가 만들어질 때
        num_i = 0
        num_j = 0
        for k in range(MAX_A):
            if arr[k][k] == i:
                num_i += 1
            if arr[k][k] == j:
                num_j += 1
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True

        # 오른쪽 위에서 왼쪽 아래를 잇는 대각선으로 빙고가 만들어질 때
        num_i = 0
        num_j = 0
        for k in range(MAX_A):
            if arr[k][MAX_A - k - 1] == i:
                num_i += 1
            if arr[k][MAX_A - k - 1] == j:
                num_j += 1
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True

        if win:
            ans += 1
print(ans)