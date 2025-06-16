import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

visited = [0] * (n)
answer = []
answer_set = set()
def backtracking():
    if len(answer) == k:
        answer_set.add(''.join(map(str,answer)))
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            answer.append(arr[i])
            backtracking()
            answer.pop()
            visited[i] = 0

backtracking()
print(len(answer_set))