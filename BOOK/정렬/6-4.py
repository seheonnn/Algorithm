# 정렬 - 퀵 정렬 O(N log N)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(array)

def quick_sort(start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # left 와 right 가 엇갈리면 작은 값과 피벗을 swap
            array[right], array[pivot] = array[pivot], array[right]
        else: # left 와 right 가 엇갈리지 않았다면 작은 값과 큰 값 swap
            array[left], array[right] = array[right], array[left]

    quick_sort(start, right-1)
    quick_sort(right+1, end)

quick_sort(0, n - 1)
print(array)