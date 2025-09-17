def solution(bandage, health, attacks):
    prev = 0
    cur = health
    for time, damage in attacks:
        gap = time - prev - 1
        if gap > 0:
            heal = (gap * bandage[1]) + (gap // bandage[0]) * bandage[2]
            cur = min(health, cur + heal)

        cur -= damage
        if cur <= 0:
            return -1

        prev = time

    return cur