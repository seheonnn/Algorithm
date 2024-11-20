T = int(input())
for t in range(1, T + 1):
    s = list(input())
    i = 1
    while True:
        if s[:i] == s[i:i + len(s[:i])]:
            break
        else:
            i += 1
    print("#" + str(t), i)
