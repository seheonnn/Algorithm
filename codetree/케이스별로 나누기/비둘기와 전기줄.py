import sys
input = sys.stdin.readline

n = int(input())
arr = [-1] * (11)
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    if arr[a] == -1: # 아직 안 정해진 상태라면 그냥 반영
        arr[a] = b
    elif arr[a] != b: # 기존과 다르다면 건넌거임
        cnt += 1
        arr[a] = b
print(cnt)