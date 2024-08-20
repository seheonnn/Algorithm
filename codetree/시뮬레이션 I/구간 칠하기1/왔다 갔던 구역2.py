import sys
input = sys.stdin.readline

n = int(input())
MAX_R = 200
block = [0] * (MAX_R+1)
OFFSET = 100
cur = 0

for _ in range(n):
    weight, direct = input().split()
    weight = int(weight)
    if direct == "L":
        l = cur - weight
        r = cur
        cur -= weight
        for i in range(l+OFFSET, r+OFFSET):
            block[i] += 1
    elif direct == "R":
        l = cur
        r = cur + weight
        cur += weight
        for i in range(l+OFFSET, r+OFFSET):
            block[i] += 1

r = [i for i in block if i >= 2]
print(len(r))
