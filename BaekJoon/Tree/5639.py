import sys
sys.setrecursionlimit(10**9)
num = []
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
postOrder(0, len(num) - 1)
