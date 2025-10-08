import sys

input = sys.stdin.readline

def check(s):
    stack = []
    match = {')':'(', ']':'['}
    for c in s:
        if c in '([':
            stack.append(c)
        elif c in '])':
            if not stack or stack[-1] != match[c]:
                return False
            stack.pop()
    return not stack

while True:
    s = input().rstrip()

    if s == ".":
        break

    answer = "yes" if check(s) else "no"
    print(answer)
