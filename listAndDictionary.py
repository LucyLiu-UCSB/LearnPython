import time
import random

import tryexcept

loopMax = random.randint(10, 50)
print("Request for" + str(loopMax) + " maths received...Beginning mathing sequence...")

operations = ['+']  # Define a new list

operations.append('-')  # a list has a append function- add a new value to the list
operations.append('+')
operations.append('*')

print("Operation count " + str(len(operations)))
print("Computer will maths using the following operations " + str(operations))

print('\n\n')

for index in range(loopMax):  # index begins from 0
    num1 = random.randint(-99, 99)
    num2 = random.randint(-99, 99)

    print("Mathing with " + str(num1) + " add " + str(num2))

    sleepTime = 0

    print("IN FOR LOOP:")
    """"Loop using the "in keyword"""
    for operation in operations:
        print('operation = ' + operation)
        tryexcept.runOperation(operation, num1, num2)
        print()  # just make a new line

    print('\n')
    print("INDEX FOR LOOP")
    """Loop using an index counter"""
    for i in range(len(operations)):
        print("i = " + str(i))
        print('operation = ' + operations[i])
        tryexcept.runOperation(operations[i], num1, num2)
        print()

    time.sleep(sleepTime)
    print('\n--------------------\n')

time.sleep(2)

wordsAndThingsDict = {}  # Define an empty dictionary

wordsAndThingsDict['Apple'] = 'Red thing that tastes good. '
wordsAndThingsDict['Orange'] = "Makes great juice"
wordsAndThingsDict[3] = "The number 3"
wordsAndThingsDict["A list"] = ['Oh', 'boy!', 'A list in a dictionary!']
wordsAndThingsDict['Inception'] = {"Nested" : 'When one dictionary is a VALUE in a dictionary'}


print(str(wordsAndThingsDict))
print()

print("Loop")

for key in wordsAndThingsDict:
    print("Key: " + str(key))
    print("Value " + str(wordsAndThingsDict[key]))
    print()