# import sys
# input = sys.stdin.readline
#
# arr = list(map(int, input().split()))
#
# r = sys.maxsize
# for _ in range(360):
#     for i in range(6):
#         for j in range(i+1,6):
#             tmp = arr.copy()
#             sum1 = arr[i] + arr[j]
#             tmp.remove(arr[i])
#             tmp.remove(arr[j])
#             for k in range(4):
#                 for l in range(k+1, 4):
#                     tmp2 = tmp.copy()
#                     sum2 = tmp[k] + tmp[l]
#                     tmp2.remove(tmp[k])
#                     tmp2.remove(tmp[l])
#                     sum3 = tmp2[0] + tmp2[1]
#
#                     max_sum = max(sum1, sum2, sum3)
#                     min_sum = min(sum1, sum2, sum3)
#
#                     r = min(r, abs(max_sum - min_sum))
# print(r)

import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = 6
arr = list(map(int, input().split()))

# 첫 번째 팀원을 만들어줍니다.
min_diff = INT_MAX
for i in range(n):
    for j in range(i + 1, n):

        # 두 번째 팀원을 만들어줍니다.
        for k in range(n):
            for l in range(k + 1, n):
                # 첫 번째 팀원과 두 번째 팀원이 겹치는지 여부를 확인합니다.
                if k == i or k == j or l == i or l == j:
                    continue

                # 세 번째 팀원의 합은 전체에서 첫 번째 팀원과 두 번째 팀원의 합을 빼주면 됩니다.
                sum1 = arr[i] + arr[j]
                sum2 = arr[k] + arr[l]
                sum3 = sum(arr) - sum1 - sum2

                # 세 팀의 차이 중 최댓값을 계산합니다.
                # 팀 합이 최대인 값과 최소인 값의 차이를 구하는 것이기 때문에 차이 중 최댓값 구
                ret = abs(sum1 - sum2)
                ret = max(ret, abs(sum2 - sum3))
                ret = max(ret, abs(sum3 - sum1))

                # 최소 차이를 갱신합니다.
                min_diff = min(min_diff, ret)

print(min_diff)
