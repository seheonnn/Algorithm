import sys
input = sys.stdin.readline

n, b = map(int, input().split())
digits = []

while True:
    if n < b:
        digits.append(n)
        break

    digits.append(n % b)
    n //= b

for i in digits[::-1]:
    print(i,end="")