def remove_duplicate_ids(obj):
    print(obj['1'])


def main():
    a = {
    "432": ["A", "A", "B", "D"],
    "53": ["L", "G", "B", "C"],
    "236": ["L", "A", "X", "G", "H", "X"],
    "11": ["P", "R", "S", "D"],
}

    keys = list(a.keys())
    keys.sort(key=int)
    result = {}
    num = 1
    for x in keys:
        temp = a[x]
        out = temp
        for y in keys[num:]:
            temp2 = a[y]
            out = [item for item in out if item not in temp2]
        num+=1
        result.update({x : list(dict.fromkeys(out))})
    print(result)
    # print({keys[x]: list( set(a[keys[3]]) - set(a[keys[2]]))})


main()
