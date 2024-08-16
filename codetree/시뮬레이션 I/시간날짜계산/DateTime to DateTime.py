import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

day, hour, mins = 11, 11, 11
cnt = 0

while True:
    # 시간초과 방지
    if (day > a) or (day == a and hour > b) or (day == a and hour == b and mins > c):
        print(-1)
        break

    if day == a and hour == b and mins == c:
        print(cnt)
        break

    cnt += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0 # 시간은 0초가 되므로 0으로 초기화

    if hour == 24:
        day += 1
        hour = 0
