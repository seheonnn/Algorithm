def minimum_prefixes(words):
    # 1. 주어진 단어를 사전 순으로 정렬
    words.sort()

    prefixes = []

    for i in range(len(words)):
        word = words[i]
        # 현재 단어와 이웃한 단어 비교 (이웃 단어가 있는 경우에만)
        next_word = words[i + 1] if i + 1 < len(words) else ""
        prev_word = words[i - 1] if i - 1 >= 0 else ""

        # 최소 접두사를 찾기 위한 변수
        prefix_length = 1

        # 접두사 길이를 증가시키며 이웃한 단어의 접두사와 비교
        while prefix_length <= len(word):
            prefix = word[:prefix_length]
            # 이웃한 단어들과의 접두사 비교
            if not (next_word.startswith(prefix) or prev_word.startswith(prefix)):
                prefixes.append(prefix)
                break
            prefix_length += 1

    return prefixes


# 입력 예시
words = ["abdb", "acd", "bcd", "abc", "aba"]
result = minimum_prefixes(words)
print(result)
