def solution(s):
    answer = True

    stack = []
    for c in s:
        if c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    if stack:
        return False

    return True