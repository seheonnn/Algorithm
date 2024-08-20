import sys
input = sys.stdin.readline

MAX_R = 100
block = [0] * (2 * MAX_R + 1)
white, black = 0, 0

cur = MAX_R
n = int(input())
for _ in range(n):
    w, di = input().split()
    w = int(w)

    if di == "L":
        while w > 0:
            block[cur] = 1
            w -= 1
            if w:
                cur -= 1

    elif di == "R":
        while w > 0:
            block[cur] = 2
            w -= 1
            if w:
                cur += 1
for i in range(2 * MAX_R + 1):
    if block[i] == 1:
        white += 1
    elif block[i] == 2:
        black += 1
print(white, black)