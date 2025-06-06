import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def lca(parents, visited, a, b):
    while True: # a의 조상 모두 표시
        visited[a] = True
        if a == parents[a]: # root
            break
        a = parents[a] # a의 조상으로 올라감

    while not visited[b]:
        b = parents[b]
    return b


tc = int(input())
for _ in range(tc):
    n = int(input().strip())
    parents = [i for i in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        parents[b] = a
    a, b = map(int, input().split())
    print(lca(parents, visited, a, b))
