import sys
input = sys.stdin.readline

n = int(input())
MAX_R = 100000
block = [0] * (2 * MAX_R + 1)
cntW = [0] * (2 * MAX_R + 1)
cntB = [0] * (2 * MAX_R + 1)

white, black, gray = 0, 0, 0
cur = MAX_R # 시작점

for _ in range(n):
    w, di = input().split()
    w = int(w)

    if di == "L":
        while w > 0:
            block[cur] = 1
            cntW[cur] += 1
            w -= 1
            if w:
                cur -= 1

    elif di == "R":
        while w > 0:
            block[cur] = 2
            cntB[cur] += 1
            w -= 1

            if w:
                cur += 1


for i in range(2 * MAX_R + 1):
    if cntW[i] >= 2 and cntB[i] >= 2:
        gray += 1
    elif block[i] == 1:
        white += 1
    elif block[i] == 2:
        black += 1

print(white, black, gray)