import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(lambda x : int(x) - 1, input().split()))

parents = [0] * n
for i in range(n): # 집합 초기화
    parents[i] = i

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])

    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# def union(a, b):
#     a = find(a)
#     b = find(b)
#
#     if a != b: # 서로 부모가 다르다면
#         parents[b] = a

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)
graph_parents = find(plan[0])
for i in range(1, m):
    if graph_parents != find(plan[i]):
        print("NO")
        sys.exit()
print("YES")