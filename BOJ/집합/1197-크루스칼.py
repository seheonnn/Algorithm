import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 재귀 제한 증가

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

V, E = map(int, input().split())
parents = [i for i in range(V + 1)]
# tree = [list(map(int, input().split())) for _ in range(E)] # Index Error
answer = 0

tree = []
for _ in range(E):
    node1, node2, grade = map(int, input().split())
    tree.append([grade, node1, node2])
tree.sort()  # 가중치 기준 정렬

# 최소 스패닝 트리 계산
for grade, node1, node2 in tree:
    if find(node1) != find(node2):
        union(node1, node2)
        answer += grade

print(answer)
