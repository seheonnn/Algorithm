# 팩토리얼 두 가지 버전
def factorial_iteration(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursion(n):
    if n <= 1:
        return 1
    return n * factorial_recursion(n-1)

print("반복적으로 구현", factorial_iteration(5))
print("재귀적으로 구현", factorial_recursion(5))