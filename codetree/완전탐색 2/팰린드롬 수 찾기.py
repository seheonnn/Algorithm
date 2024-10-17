import sys
input = sys.stdin.readline

x, y = map(int, input().split())

cnt = 0
for i in range(x, y+1):
    n = str(i)
    if n == n[::-1]: # 반대로 출력
        cnt += 1
print(cnt)