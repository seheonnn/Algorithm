import sys
sys.setrecursionlimit(10000)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

root = None
while True:
    try:
        root = insert(root, int(sys.stdin.readline()))
    except:
        break