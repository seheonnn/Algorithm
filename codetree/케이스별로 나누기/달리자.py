import sys
input = sys.stdin.readline

n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

tmp = 0
total = 0

for i in range(n):
    tmp += lst1[i] - lst2[i]
    total += abs(tmp)
print(total)