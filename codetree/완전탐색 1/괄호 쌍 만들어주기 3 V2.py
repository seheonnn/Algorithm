import sys
input = sys.stdin.readline

lst = input()
n = len(lst)
cnt = 0
for i in range(n):
    if lst[i] == "(":
        for j in range(i+1, n):
            if lst[j] == ")":
                cnt += 1

print(cnt)