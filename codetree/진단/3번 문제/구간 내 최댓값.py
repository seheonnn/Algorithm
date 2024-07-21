import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

sum = 0
m = -sys.maxsize
for i in range(r1-1, r2):
    for j in range(c1-1, c2):
        if m <= graph[i][j]:
            m = graph[i][j]

print(m)