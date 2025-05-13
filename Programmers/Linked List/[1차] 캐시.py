from collections import deque


def solution(cacheSize, cities):
    r = 0
    cache = deque()
    for city in cities:
        city = city.lower()

        if city in cache:
            r += 1
            cache.remove(city)
            cache.append(city)
        else:
            r += 5
            if cacheSize > 0:
                if len(cache) >= cacheSize:
                    cache.popleft()
                cache.append(city)

    return r