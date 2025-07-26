import sys

input = sys.stdin.readline

n, x = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(100):
    person = i % n
    volume = x + i
    if volume > lst[person]:
        print(person + 1)
        break