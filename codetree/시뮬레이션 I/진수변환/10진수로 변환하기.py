import sys
input = sys.stdin.readline

n = input()
num = 0

for i in range(len(n)):
    num = num * 2 + int(n[i])
print(num)