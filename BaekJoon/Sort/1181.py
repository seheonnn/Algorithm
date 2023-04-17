# 단어 정렬 (중복된 단어 제거)
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.
import sys

n = int(sys.stdin.readline())
li=[]
for _ in range(n): li.append(sys.stdin.readline().strip()) # strip()은 공백 제거
li = set(li)
li = list(li)

li.sort()
li.sort(key=len)
# 정렬 순서를 주의해야 되는데, 상위 조건 A와 하위 조건 B가 있으면
# 먼저 B로 정렬을 한 후에 A로 정렬을 해야 원하는 결과를 얻을 수 있다.

for s in li:
    print(s)
