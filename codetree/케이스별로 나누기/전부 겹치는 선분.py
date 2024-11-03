import sys
input = sys.stdin.readline

n = int(input().strip())
# arr = [0] * 101
# for _ in range(n):
#     a, b = map(int, input().split())
#     for i in range(a, b+1):
#         arr[i] += 1

# print("Yes" if n in arr else "No")

max_a = 0 # 시작점 중 최댓값
min_b = sys.maxsize # 끝점 중 최소값
for _ in range(n):
    a, b = map(int, input().split())
    max_a = max(max_a, a)
    min_b = min(min_b, b)
print("Yes" if min_b >= max_a else "No") # 어느 한 선분이라도 시작점이 다른 선분의 끝점보다 큰 값이라면 전부 겹칠 수 없음
