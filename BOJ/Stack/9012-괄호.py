import sys

input = sys.stdin.readline

def check(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()

    return not stack

n = int(input())
for _ in range(n):
    s = input().rstrip()
    answer = "YES" if check(s) else "NO"
    print(answer)
