def add(num1, num2):
    """Return num1 plus num2. One stop Programming is cool"""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2."""
    return num1 - num2


def mul(num1, num2):
    """Returnd num1 times num2."""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divided by num2."""
    try:
         return num1 / num2
    except ZeroDivisionError:
        print('Handled by zero. Returning zero')
        return 0


def runOperation(operation, num1, num2):
    """Determines the operation to run based on the
    operation argument which should be in as an
    int
    """
    # Determine operation
    if (operation == 1 or operation == '+'):
        print(add(num1, num2))
    elif (operation == 2 or operation == '-'):
        print(sub(num1, num2))
    elif (operation == 3 or operation == '*'):
        print(mul(num1, num2))
    elif (operation == 4 or operation == '/'):
        print(div(num1, num2))
    else:
        print('i do not understand')


def main():
    user_continue = True;
    while user_continue:
            validInput = False
            while not validInput:
                try:
                    num1 = int(input("What is number 1?"))
                    num2 = int(input("What is number 2?"))
                    operation = int(input("what do you want to do？ 1. add, 2. subtract, 3. multiple, or 4. divide. "
                                          "Enter number: "))
                    validInput = True
                except ValueError:
                    print("invalid input try again.")
                except:
                    print("Unknown error")
                    # return  # exit
            runOperation(operation, num1, num2)
            # Ask User to continue
            user_yn= input("would you like to run another calculation? (y for yes or any other to exit")
            if (user_yn != 'y'):
                user_continue = False
                break
            else:
                continue


main()

if __name__ == "__main__":
    main()