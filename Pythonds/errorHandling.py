
def f():
    var = input("Insert a number: ")
    div = input("Input a divider:")
    try:
        suma = int(var) / int(div)
        print("Sum is: {}".format(suma))
#If we leave except its gonna catch all type of exceptions, but we can also specify the type of exception
    except ZeroDivisionError:
        print("Your not allowed to dived by zero. NO NO Lets try again....")
        f()
    except:
        print("You are hurting me://")

def main():
    f()

if __name__ == '__main__':
    main()


