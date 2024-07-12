# 구현 - 단어 뒤집기 2 (스택)

import sys

str = sys.stdin.readline().strip()
stack = []
result = ""
check = False # 현재 괄호 안에 있는지
for i in str:
    if i == "<":
        while stack:
            result += stack.pop()
        check = True
        result += i # < 먼저 결과에 추가
    elif i == ">":
        check = False
        result += i # 괄호 밖임을 표시하고 > 를 결과에 추가
    elif i == " " and not check: # 괄호 밖인 공백이라면
        while stack: # 스택 값들 모두 반대로 출력
            result += stack.pop()
        result += " "
    else: # 문자인 경우
        if check: # 괄호 안 이면 결과에 그대로 추가
            result += i
        else: # 괄호 밖이면 뒤집기 위해 스택에 추가
            stack.append(i)
while stack:
    result += stack.pop()

print(result)
