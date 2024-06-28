from collections import deque

# 큐 구현 - deque 라이브러리
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # queue.popleft() : 큐의 앞에서 원소 제거 / queue.pop() : 큐의 뒤에서 원소 제거
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse() # 큐 역순으로
print(queue)
