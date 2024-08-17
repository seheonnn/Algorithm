import sys
input = sys.stdin.readline

num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
w = 0

m1, d1, m2, d2 = map(int, input().split())

sum1 = sum(num_of_days[:m1]) + d1 # 1월 1일부터 현재까지의 날짜 수
sum2 = sum(num_of_days[:m2]) + d2
diff = sum2-sum1

print(week[(1 + diff)%7]) # 음수도 %(mod)연산 가능
