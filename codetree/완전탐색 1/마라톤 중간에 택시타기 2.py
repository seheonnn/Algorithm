import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

min_sum = sys.maxsize

for i in range(1, n-1): # 1번 체크포인트와 N번 체크포인트는 건너뛸 수 없음
    temp = lst.copy() # 리스트 깊은 복사!!!
    temp.pop(i) # i 번째 요소 삭제
    s = 0
    for j in range(1, len(temp)):
        s += abs(temp[j][0] - temp[j-1][0]) + abs(temp[j][1] - temp[j-1][1])

    min_sum = min(min_sum, s)

print(min_sum)