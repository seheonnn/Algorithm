# import sys
#
# input = sys.stdin.readline
#
# day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# x, y = map(int, input().split())
# days = 0
# for i in range(1, x):
#     days += month[i]
# days += y
# print(day[(days-1) % 7]) # 1일 뺴주기

import sys

input = sys.stdin.readline

day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
days = sum(month[:x]) + y
print(day[(days-1) % 7])