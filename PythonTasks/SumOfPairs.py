# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.


def sum_pairs(ints, s):
    seen = set()
    for x in ints:
        if s-x in seen:
            return [s-x, x]
        seen.add(x)



def main():
    dict = {
    8 : [1, 4, 8, 7, 3, 15],
    -6 : [1, -2, 3, 0, -6, 1],
    -7 : [20, -13, 40],
    2 : [1, 2, 3, 4, 1, 0],
    10 : [10, 5, 2, 3, 7, 5],
    }

    for key, value in dict.items():
        print(sum_pairs(value, key))


if __name__ == '__main__':
    main()
