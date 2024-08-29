import sys
input = sys.stdin.readline

arr = [0] * 10000
n, k = map(int, input().split())
for _ in range(n):
    pos, al = input().split()
    pos = int(pos)
    # if al == "G":
    #     arr[pos] = 1
    # elif al == "H":
    #     arr[pos] = 2
    arr[pos] = 1 if al == "G" else 2

max_score = 0
for i in range(10000):
    max_score = max(max_score, sum(arr[i:i+k+1])) # 양 끝점 포함
print(max_score)