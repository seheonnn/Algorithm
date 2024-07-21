import itertools
import sys
input = sys.stdin.readline

n = int(input())

lst = [i for i in range(1, n + 1)]
result = itertools.permutations(lst)
r = sorted(result, reverse=True)
for lst in r:
    for num in lst:
        print(num, end=" ")
    print()