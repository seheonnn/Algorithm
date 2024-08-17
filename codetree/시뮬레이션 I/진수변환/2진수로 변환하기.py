import sys

input = sys.stdin.readline

n = int(input())
digits = []

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

for i in digits[::-1]: # digits[::-1] -> reverse
    print(i, end="")
