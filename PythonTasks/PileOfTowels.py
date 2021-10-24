def sort_the_pile(pile_of_towels, weekly_used_towels):
    usedTowels = []
    for x in weekly_used_towels:
        for i in range(x):
            u = pile_of_towels.pop()
            usedTowels.append(u)
        usedTowels.sort(reverse=True)
        pile_of_towels.extend(usedTowels)
        usedTowels.clear()
    return pile_of_towels


def main():
    pile_of_towels = ["blue", "red", "blue", "red", "blue"]
    weekly_used_towels = [2, 1, 4, 2]
    print(sort_the_pile(pile_of_towels, weekly_used_towels))

if __name__ == '__main__':
    main()