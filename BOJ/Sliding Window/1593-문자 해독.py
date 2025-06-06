import sys

input = sys.stdin.readline


def char_index(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')  # 'A'~'Z' → 0~25
    else:
        return ord(c) - ord('a') + 26  # 'a'~'z' → 26~51


g, s = map(int, input().split())

str1 = input().strip()
str2 = input().strip()

lst1 = [0] * 52  # 대문자 + 소문자
lst2 = [0] * 52

for x in str1:
    lst1[char_index(x)] += 1

# 초기 윈도우
for i in range(g):
    lst2[char_index(str2[i])] += 1

r = 0
# index : 아스키 코드, value : 각 알파벳이 현재 윈도우에 몇 번 등장했는지 저장
# 두 리스트가 같다는 것은 → 각 알파벳의 등장 횟수가 모두 같다는 의미
# 즉, W의 순열(anagram)이 현재 슬라이딩 윈도우에 존재한다
if lst1 == lst2:
    r += 1

for i in range(g, s):
    lst2[char_index(str2[i])] += 1
    lst2[char_index(str2[i - g])] -= 1

    if lst1 == lst2:
        r += 1

print(r)
