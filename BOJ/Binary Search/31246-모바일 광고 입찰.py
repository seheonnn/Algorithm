import sys
input = sys.stdin.readline

n, k = map(int, input().split())
budgets = [list(map(int, input().split())) for _ in range(n)]

# X의 범위가 0 ~ 10**9로 정해져 있으므로 이진 탐색으로 찾을 수 있음
start = 0
end = 10 ** 9
result = end

while start <= end:
    mid = (start + end) // 2 # mid == X, X가 커져야 낙찰 가능 개수가 증가함
    cnt = 0

    for a, b in budgets:
        if a + mid >= b: # A + X >= B라면 낙찰 (이진 탐색의 중심값)
            cnt += 1

    if cnt >= k:
        result = mid # 현재 X로 목표 낙찰 지면 개수인 k개 이상을 받을 수 있으므로 저장
        end = mid - 1 # 더 작은 X로 실행하기 위해 end 값을 줄임
    else:
        start = mid + 1 # 목표 개수에 도달하지 못했으므로 더 큰 X로 시도하기 위해 start값을 올림


print(result)


# 방법 2
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
diff = []
for _ in range(n):
    a, b = map(int, input().split())
    diff.append(b - a)

diff.sort() # b - a의 차이를 오름차순으로 정렬
# b - a > 0 : MOLOCO가 차이만큼 금액을 올려야 낙찰 가능
# b - a <= 0 : MOLOCO 낙찰 가능

# k개를 낙찰 받기 위해 필요한 X = diff[k-1]
# [-2, 0, 3, 5, 10, 20] 일 때 k = 3으로 3개 낙찰이 목표라면 X는 3임
result = max(0, diff[k - 1]) # diff[K-1]이 음수라면, MOLOCO는 이미 낙찰받은 상태임
print(result)