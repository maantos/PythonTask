def isValidSubsequence(array, sequence):
    indexArray = 0
    indexSequence = 0

    for a in array:
        if a == sequence[indexSequence]:
            indexSequence+=1
    return indexSequence == len(sequence)


def main():
    a=  [5, 1, 22, 25, 6, -1, 8, 10]
    s = [5, 1, 22, 25, 6, -1, 8, 10, 10]
    print(isValidSubsequence(a,s))


main()
