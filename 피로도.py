def solution(k, dungeons):
    dungeons.sort(key=lambda x: x[1])

    count = 0
    for dungeon in dungeons:
        min_fatigue, consume_fatigue = dungeon

        if k >= min_fatigue:
            k -= consume_fatigue
            count += 1
        else:
            break

    return count