# 증가 수열을 이용하여 트리를 만드는 방법
# 1. 첫 번째 정수는 트리의 루트 노드입니다.
# 2. 다음에 등장하는 연속된 수의 집합은 루트의 자식을 나타냅니다. 이 집합에 포함되는 수의 첫 번째 수는 항상 루트 노드+1보다 큽니다.
# 3. 그다음부터는 모든 연속된 수의 집합은 아직 자식이 없는 노드의 자식이 됩니다. 그러한 노드가 여러 가지인 경우에는 가장 작은 수를 가지는 노드의 자식이 됩니다.
# 4. 집합은 수가 연속하지 않는 곳에서 구분됩니다.
# 두 노드의 부모가 다르지만, 두 부모가 형제일 때, 두 노드를 사촌이라고 합니다.

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
par = [0] * (n + 1)

r = 0
tar = 0
arr = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    if arr[i] == k:
        tar = i # k 의 index

# n개의 원소로 트리 만들기
par_idx = 0
for i in range(2, n + 1):
    # 두 원소가 연속하지 않으면 부모 노드의 index 1 증가(연속하지 않으면 서로 다른 부모임)
    if arr[i] > arr[i - 1] + 1: # 1 | 3 4 5 | 8 9 -> 5 다음 8이므로 서로 다른 부모, 만약 6이 있었다면 5랑 같은 부모임
        par_idx += 1
    par[i] = par_idx # i 노드의 부모 노드의 index는 par_idx임

for i in range(1, n+1):
    # 부모 노드는 다르면서 부모의 부모가 같은 경우
    if not par[par[i]] or not par[par[tar]]: # 부모의 부모 노드가 없으면 continue
        continue
    if par[i] != par[tar] and par[par[i]] == par[par[tar]]: # 부모 노드는 다르면서 부모의 부모 노드는 같은 경우
        r += 1

print(r)
