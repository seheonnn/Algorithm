import sys
input = sys.stdin.readline

num_of_days = [0, 31,28,31,30,31,30,31,31,30,31,30,31] # 월별 날짜 수
m1, d1, m2, d2 = map(int, input().split())
month, days = m1, d1
cnt = 1

while True:
    if month == m2 and days == d2:
        break

    cnt += 1
    days += 1

    if days > num_of_days[month]:
        month += 1
        days = 1 # 일은 1일이 되므로 1로 초기화

print(cnt)