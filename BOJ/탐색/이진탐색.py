arr = [3, 2, 1, 4, 6, 7, 9, 8]

def binary(target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]: # target이 더 작은 경우 좌측 탐색
        return binary(target, left, mid - 1)
    elif arr[mid] < target: # target이 더 큰 경우 우측 탐색
        return binary(target, mid + 1, right)

arr.sort()
print(binary(1, 0, len(arr) - 1))