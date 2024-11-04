import sys
input = sys.stdin.readline

x1, x2, x3, x4 = map(int, input().split())
# arr = [0]*101
# for i in range(x1, x2+1):
#     arr[i] += 1
# for i in range(x3, x4+1):
#     arr[i] += 1
# if 2 in arr:
#     print("intersecting")
# else:
#     print("nonintersecting")

if x2 < x3 or x4 < x1:
    print("nonintersecting")
else:
    print("intersecting")