# 구현 - 분수 찾기
import sys

x = int(sys.stdin.readline())
line = 1

while x > line:
    x -= line
    line += 1

# print(x)
# print(line)

if line % 2 == 0:
    a = x
    b = line - x + 1
elif line % 2 == 1:
    a = line - x + 1
    b = x

print(f"{a}/{b}")