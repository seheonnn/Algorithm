import sys
sys.setrecursionlimit(10**9)
tree = {} # 노드가 문자열이므로 딕셔너리로 트리 구성

n = int(input())
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)

# 전위 순회
def preOrder(node):
    if node == ".":
        return
    print(node, end="")
    preOrder(tree[node][0])
    preOrder(tree[node][1])

# 중위 순회
def inOrder(node):
    if node == ".":
        return
    inOrder(tree[node][0])
    print(node, end="")
    inOrder(tree[node][1])

# 후위 순회
def postOrder(node):
    if node == ".":
        return
    postOrder(tree[node][0])
    postOrder(tree[node][1])
    print(node, end="")

preOrder("A")
print()
inOrder("A")
print()
postOrder("A")