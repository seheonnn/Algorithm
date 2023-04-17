# 랜선 자르기 - 이분 탐색
k, n = map(int, input().split())
# list 입력 받기
lan = [int(input())for _ in range(k)]
start, end = 1, max(lan)

def lan_cnt(n):
    count = 0
    for i in lan:
        count += i // n
    return count

def binary_search(start, end, n):
    if start > end:
        return end
    mid = (start + end) // 2
    length = lan_cnt(mid)
    # mid 길이로 만들 수 있는 랜선의 개수가 n보다 크면 mid+1, 작으면 mid-1
    if length >= n:
        return binary_search(mid+1, end, n)
    else:
        return binary_search(start, mid-1, n)
print(binary_search(start, end, n))