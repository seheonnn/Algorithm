import sys
input = sys.stdin.readline

lst = input()
cnt = 0
for i in range(len(lst)):
    if lst[i] == '(':
        for j in range(i+1, len(lst)):
            if lst[j] == ')':
                cnt += 1
print(cnt)
