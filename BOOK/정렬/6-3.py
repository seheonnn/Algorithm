# 정렬 - 삽입 정렬 O(N^)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(array)

for i in range(1, n):
    for j in range(i, 0, -1): # 삽입 정렬은 역순으로
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]

        # else:
        #     break

print(array)