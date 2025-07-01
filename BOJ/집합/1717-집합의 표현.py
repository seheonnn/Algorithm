import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [x for x in range(n + 1)]


def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a


def check(a, b):
    return find(a) == find(b)


for i in range(m):
    com, a, b = map(int, input().split())
    if com == 0:
        union(a, b)
    else:
        if check(a, b):
            print("YES")
        else:
            print("NO")
