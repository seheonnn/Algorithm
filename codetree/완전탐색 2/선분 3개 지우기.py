import sys

input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    a, b = map(int, input().split())
    graph.append((a, b))

r = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            overlap = False
            arr = [0] * (101)

            for x in range(n):
                if x == i or x == j or x == k:
                    continue

                for y in range(graph[x][0], graph[x][1] + 1):
                    arr[y] += 1
            for x in range(101):
                if arr[x] > 1:
                    overlap = True
            if overlap == False:
                r += 1
print(r)

