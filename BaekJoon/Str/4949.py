# 균형 맞추기
while 1:
    string = input()
    if string == '.':
        break
    stack = []
    for i in string:
        if i not in '([])':
            continue
        if i in '([':
            stack.append(i)
        else:
            if not stack or (i == ']' and stack[-1] != '[') or (i == ')' and stack[-1] != '('):
                print("no")
                break
            stack.pop()
    else:
        if not stack:
            print("yes")
        else:
            print("no")