import string
import random
import time


def isShaekspear(sentence):
    score = 0
    sheaksper = "methinks it is like a weasel"
    for x, y in zip(sentence, sheaksper):
        if x == y:
            score+=1
    return score

def sentenceCreator(*args):
    alhabet = 'abcdefghijklmnopqrstuvwxyz '
    return ''.join(random.choice(alhabet) for x in range(28))

def main():
    start = time.time()
    a = 0
    while a < 10:
        sentence = sentenceCreator()
        #if isShaekspear(sentence) > 14:
        if isShaekspear(sentence) > a:
             a = isShaekspear(sentence)

    end = time.time()
            # print("Run number {} with score: {}".format(x, isShaekspear(sentence)))
    print("End of loop. The biggest was: {} Time: {}\r".format(a, end-start))

if __name__ == '__main__':
    main()