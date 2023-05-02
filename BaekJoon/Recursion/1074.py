# https://ggasoon2.tistory.com/11
import sys
N, r, c = map(int ,sys.stdin.readline().split())

def solution(N, r, c):
    if N == 0:
        return 0
    return 2*(r%2) + (c%2) + 4*solution(N-1, int(r/2), int(c/2))

print(solution(N, r, c))