# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

M, N = map(int, input().split())
for n in range(M, N+1):
    if n == 1: # 1은 소수가 아님
        continue
    for i in range(2, int(n**0.5) + 1): # 특정 수의 제곱근까지의 약수 확인
        if n % i ==0:
            break
    else:
        print(n)