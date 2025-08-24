def solution(input_string):
    answer = set()
    exist = set()
    prev = None
    for c in input_string:
        if c != prev:
            if c in exist:
                answer.add(c)
            else:
                exist.add(c)
            prev = c

    return ''.join(sorted(answer)) if answer else 'N'