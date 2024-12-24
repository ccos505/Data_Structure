house = {
    1: 9,
    2: 9,
    3: 9,
    4: 1,
    5: 3,
    6: 8,
    7: 2,
    8: 7,
    9: 1,
    10: 1,
    11: 8,
    12: 9,
    13: 1,
    14: 9999
}


def find_house(house):
    sorted_house = sorted(
        house.items(), key=lambda x: (x[1], x[0]), reverse=True)
    ans = 0
    keep_track = []
    for s in sorted_house:
        i, money = s[0], s[1]
        T = True
        for k in keep_track:
            if (i <= k+1) and (i >= k-1):
                T = False
                break
        if T:
            ans += money
            keep_track.append(i)
    return ans, sorted(keep_track)


print(find_house(house))


# ----------------------- #


list_house = [j for _, j in house.items()]
print(list_house)


def find_house_recursive(house):
    if not house:
        return 0
    first = house[0] + find_house_recursive(house[2:])
    second = find_house_recursive(house[1:])
    return max(first, second)


print(find_house_recursive(list_house))
