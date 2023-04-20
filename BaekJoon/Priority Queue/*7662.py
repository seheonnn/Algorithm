# 우선순위큐
# 큐 두 개 사용하는 이유
# -> 모든 데이터를 하나의 힙에 저장하면 최대값, 최소값 삭제할 때마다 힙을 재정렬해야 함. 이는 매우 비효율적
# 따라서 최대값을 삭제하는 용도, 최소값을 삭제하는 용도로 별도의 힙을 구성.
import heapq
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    visited = [False] * k
    for i in range(k):
        operation, n = sys.stdin.readline().split()
        n = int(n)

        if operation == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = True # True 면 아직 삭제 되지 않은 상태
        else: # operation == 'D'
            if n == -1: # 삭제 연산시 key 값을 기준으로 해당 노드가 max_heap 에서 삭제된 노드인지 먼저 확인
                # 이미 max_heap에 의해 삭제된 노드인 경우 삭제되지 않은 노드가 나올 때까지 계속 pop 하고 삭제 대상 노드가 나오면 삭제
                while min_heap and not visited[min_heap[0][1]]: # visited 가 False인 경우 -> 삭제된 상태
                    heapq.heappop(min_heap) # max_heap에 의해 이미 삭제된 노드는 pop
                if min_heap:
                    visited[min_heap[0][1]] = False # visited 가 True 였으므로 False로 바꾸고
                    heapq.heappop(min_heap) # pop
            elif n == 1:
                while max_heap and not visited[max_heap[0][1]]: # 이미 min_heap에 의해 삭제된 노드는 pop
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

        # print(min_heap)
        # print(max_heap)
        # print(visited)
# 모든 연산이 끝난 후에도 쓰레기 노드가 들어있을 수 있으므로, 모두 비우고 각 heap의 첫 번째 원소 값을 출력.
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')