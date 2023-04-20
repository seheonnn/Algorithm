# 회의실 배정 문제
import sys
N = int(sys.stdin.readline())
time = []
for _ in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))
time = sorted(time, key=lambda a: a[0]) # 회의 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 회의 종료 시간을 기준으로 다시 오름차순
last = 0 # 마지막 회의의 끝나는 시간을 저장
cnt = 0
for i, j in time:
    if i >= last:
        cnt += 1
        last = j
print(cnt)