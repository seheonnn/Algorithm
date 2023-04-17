import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
result = abs(100-N)
if M:
    li = list(sys.stdin.readline().split())
else:
    li = []
# 작은 수에서 큰 수로 이동할 땐, 500000 까지 보면 되지만
# 반대로 큰 수에서 작은 수로 내려올 수 있으므로 1000000 까지 봐야함.
for num in range(1000001):
    for i in str(num):
        if i in li:
            break
    else:
        result = min(result, len(str(num)) + abs(num - N))
print(result)