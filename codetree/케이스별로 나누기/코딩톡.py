import sys

input = sys.stdin.readline

n, m, p = map(int, input().split())
arr = []

for _ in range(m):
    c, u = input().split()  # c : 메시지 보낸이, u : 해당 메시지 읽지 않은 사람 수
    arr.append((c, int(u)))

for i in range(n):
    person = chr(ord('A') + i)
    read = False

    for c, u in arr:
        if u >= arr[p - 1][1] and c == person:  # p번째 메시지보다 읽지 않은 사람이 많으면 p번째 메시지는 읽었다는 의미
            read = True

    if arr[p - 1][1] == 0:  # 모두 읽은 경우
        print()
    elif read == False:
        print(person, end=" ")
