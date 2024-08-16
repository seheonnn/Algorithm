import sys
input = sys.stdin.readline

m1, d1, m2, d2 = map(int, input().split())
c = input().strip()
num_of_days = [0, 31,29,31,30,31,30,31,31,30,31,30,31]
week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

s1 = sum(num_of_days[:m1]) + d1
s2 = sum(num_of_days[:m2]) + d2

target = week.index(c)
cnt = 0
cur = 1
for i in range(s1, s2+1):
    if cur == target:
        cnt += 1
    cur = (cur + 1) % 7

print(cnt)