import sys

input = sys.stdin.readline

n = int(input().strip())
s = input().strip()
r = n

for i in range(1, n + 1):  # 부분 문자열의 길이
    found_duplicate = False
    for j in range(n - i + 1):  # 길이 i인 부분 문자열을 선택
        current_substring = s[j:j + i]
        # 선택된 부분 문자열을 이후에 다시 등장하는지 확인
        for k in range(j + 1, n - i + 1):
            if current_substring == s[k:k + i]:
                found_duplicate = True
                break
        if found_duplicate:
            break

    if not found_duplicate:  # 중복이 없는 최소 길이를 찾으면 종료
        r = i
        break

print(r)