import sys
input = sys.stdin.readline

n = input().strip()
num = 0

for i in range(len(n)):
    num = num * 2 + int(n[i])

num *= 17

digits = []
while True:
    if num < 2:
        digits.append(num)
        break
    digits.append(num%2)
    num //= 2

for i in digits[::-1]:
    print(i,end="")