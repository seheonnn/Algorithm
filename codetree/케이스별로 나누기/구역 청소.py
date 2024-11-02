import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

# arr = [0] * 100
# for i in range(a, b):
#     arr[i] = 1
# for i in range(c, d):
#     arr[i] = 1

# print(arr.count(1))

if b < c or d < a: # 겹치지 않는 경우
    print((b-a) + (d-c))
else:
    print(max(b, d) - min(a, c))