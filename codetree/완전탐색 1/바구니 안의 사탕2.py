import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] * 101  # 바구니의 위치와 사탕 개수를 저장하는 리스트

for i in range(n):
    a, b = map(int, input().split())
    arr[b] += a  # 같은 위치에 있는 사탕 개수를 더해줌

max_sum = 0

for i in range(101):
    # 구간의 크기가 항상 2k+1은 아님
    left = max(0, i - k)
    right = min(100, i + k)
    current_sum = sum(arr[left:right+1])
    max_sum = max(max_sum, current_sum)

print(max_sum)
