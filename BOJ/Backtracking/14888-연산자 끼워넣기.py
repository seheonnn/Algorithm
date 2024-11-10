import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
op = list(map(int,input().split())) # 연산 리스트

maximum = -sys.maxsize
minimum = sys.maxsize

def backtrack(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        backtrack(depth + 1, total + lst[depth], plus - 1, minus, multiply, divide)
    if minus:
        backtrack(depth + 1, total - lst[depth], plus, minus - 1, multiply, divide)
    if multiply:
        backtrack(depth + 1, total * lst[depth], plus, minus, multiply - 1, divide)
    if divide:
        backtrack(depth + 1, int(total / lst[depth]), plus, minus, multiply, divide - 1) # total // lst[depth]는 틀린값 나옴

backtrack(1, lst[0],op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)