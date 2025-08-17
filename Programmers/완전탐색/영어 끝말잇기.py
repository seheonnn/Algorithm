# def solution(n, words):
#     len_words = len(words)
#     used = []
#
#     for i in range(len_words):
#         if words[i] in used:
#             return [(i % n) + 1, (i // n) + 1]
#
#         used.append(words[i])
#
#         if i > 0 and words[i - 1][-1] != words[i][0]:
#             return [(i % n) + 1, (i // n) + 1]
#
#     return [0, 0]

def solution(n, words):
    used = set()
    used.add(words[0])
    for i in range(1, len(words)):
        prev = words[i - 1]
        cur = words[i]

        if cur in used or prev[-1] != cur[0]:
            return [(i % n) + 1, (i // n) + 1]

        used.add(words[i])

    return [0, 0]