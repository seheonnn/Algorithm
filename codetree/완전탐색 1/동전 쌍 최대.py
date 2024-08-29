# 1 * 2 격자 하나
n = 5
arr = [[1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 1, 1, 0, 1],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0]]

max_cnt = 0
for i in range(n):
    for j in range(n - 1): # 둘 씩 짝을 지었을 때 범위 밖으로 나가면 안 됨
        max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1])

print(max_cnt)


# 1 * 2 격자 두 개
n = 5
arr = [[1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 1, 1, 0, 1],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0]]

max_cnt = 0
for i in range(n):
    for j in range(n - 1):
        for k in range(i + 1, n): # 두 격자는 서로 다른 행에 있어야 함
            for l in range(n - 1):
                max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1]
                                     + arr[k][l] + arr[k][l + 1])

print(max_cnt)