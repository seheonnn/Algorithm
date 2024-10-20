import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
MAX = 40
for A in range(1, MAX+1):
    for B in range(A, MAX+1):
        for C in range(B, MAX+1):
            for D in range(C, MAX+1):
                tmp = [A, B, C, D, A+B, B+C, C+D, D+A, A+C, B+D, A+B+C, A+B+D, A+C+D, B+C+D, A+B+C+D]
                if sorted(tmp) == sorted(arr):
                    print(A, B, C, D)