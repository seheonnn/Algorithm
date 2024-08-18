import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = input().strip()
num = 0

for i in range(len(n)):
    num = num * a + int(n[i])

digits = []
while True:
    if num < b:
        digits.append(num)
        break
    digits.append(num%b)
    num //= b

for i in digits[::-1]:
    print(i, end="")