import math
def point_in_circle(x, y):
    temp = math.sqrt(pow(x,2)+pow(y,2))
    if temp > 0:
        return temp
    return "aa"

def main():
    print(point_in_circle(0.5,0.5))
    print(point_in_circle(0.5,0.5))

if __name__ == '__main__':
    main()