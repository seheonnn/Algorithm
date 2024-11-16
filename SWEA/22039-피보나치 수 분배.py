# 집합 B와 A의 합이 동일해야함
# 피보나치는 기본적으로 BBA BBA BBA 반복됨
def solve_partition_problem_optimized(n):
    if n % 3 == 1: # 하나 남으므로 불가능
        return "impossible"
    else:
        result = "BBA" * (n // 3) # BBA 반복
        if n % 3 == 2: # 두 개가 남는 경우 맨 앞의 1 1을 각각의 집합으로
            result = "BA" + result # 따라서 앞에 BA 붙이면 됨
        return result

T = int(input())
for _ in range(T):
    n = int(input())
    print(solve_partition_problem_optimized(n))
