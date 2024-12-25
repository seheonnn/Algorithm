import sys
input = sys.stdin.readline

k = int(input())
n = (2 ** k) - 1 # 총 노드의 개수

tree_num = [0] * (n + 1)
cnt = 1

# 중위 순회 순서
a = [0] + list(map(int, input().split()))

def inOrder(x):
    global cnt
    if x > n:
        return

    inOrder(x * 2) # x * 2 : 왼쪽 자식 노드의 인덱스
    tree_num[x] = a[cnt]
    cnt += 1
    inOrder(x * 2 + 1) # x * 2 + 1 : 오른쪽 자식 노드의 인덱스

inOrder(1)
for i in range(1, k + 1):
    for j in range(2 ** (i - 1), 2 ** i):
        print(tree_num[j], end=" ")
    print()