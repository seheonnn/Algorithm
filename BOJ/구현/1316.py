# 그룹 단어 체커 - 1316

import sys
n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
  str = sys.stdin.readline()
  # str.find('a') 는 문자열에서 문자가 처음으로 등장하는 인덱스 반환
  # 각 문자가 처음으로 등장하는 인덱스를 기준으로 정렬했을 때 기존 배열과 차이가 없다면 그룹 단어임
  if list(str) == sorted(str, key=str.find):
    cnt += 1

print(cnt)