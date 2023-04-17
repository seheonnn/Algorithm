# 집합 S에 대한 연산 수행
import sys
M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    X = sys.stdin.readline().split()
    if len(X) == 1:
        if X[0] == "all":
            S = set([i for i in range(1, 21)]) # add를 사용하는 경우 시간 초과 발생
        else:
            S = set()
    else:
        func = X[0]
        x = int(X[1])
        if func == "add":
            if x not in S:
                S.add(x)
        elif func == "remove":
            if x in S:
                S.discard(x) # remove는 존재하지 않는 수를 제거하려 하면 오류 발생
        elif func == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)