T = int(input())
for t in range(1, T + 1):
    s, k = input().split()
    s = list(s)
    k = int(k)

    for _ in range(k):
        if s.index('o') == 0 or s.index('o') == 1: # 가능성 있는 컵이 여러 개면 왼쪽 위치이므로 가운데일 때도 왼쪽이랑 바꿈
            s[0], s[1] = s[1], s[0]
        if s.index('o') == 2:
            s[1], s[2] = s[2], s[1]
    print('#' + str(t),s.index('o'))

# 3
# .o. 1
# o.. 1
# ..o 0
