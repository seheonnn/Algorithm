import sys
n = int(sys.stdin.readline())

factorial = 1
for i in range(2, n+1):
    factorial *= i
zero_cnt = 0
while factorial % 10 == 0:
    zero_cnt += 1
    factorial //= 10

print(zero_cnt)