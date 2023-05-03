import sys
sys.setrecursionlimit(10**9)
num = []

# 전위 순회
def preOrder(start, end):
    if start > end:
        return
    # root 찾기
    root = num[start]
    idx = start + 1
    while idx <= end:
        if num[idx] > root:
            break
        idx += 1
    print(root)
    preOrder(start + 1, idx - 1)
    preOrder(idx, end)
# 중위 순회
def inOrder(start, end):
    if start > end:
        return
    # root 찾기
    root = num[start]
    idx = start + 1
    while idx <= end:
        if num[idx] > root:
            break
        idx += 1
    inOrder(start + 1, idx - 1)
    print(root)
    inOrder(idx, end)
# 후위 순회
def postOrder(start, end):
    if start > end:
        return
    root = num[start]
    idx = start + 1
    while idx <= end:
        if num[idx] > root:
            break
        idx += 1
    postOrder(start + 1, idx - 1)
    postOrder(idx, end)
    print(root)

while True:
    try:
        num.append(int(sys.stdin.readline()))
    except:
        break

# print("전위")
# preOrder(0, len(num) - 1)
# print("중위")
# inOrder(0, len(num) - 1)
print("후위")
postOrder(0, len(num) - 1)
