import sys


def collatiz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1

while True:
    try:
        collatiz_number = int(input('Enter a number or 0 to exit: '))
        if collatiz_number == 0:
            sys.exit()
    except ValueError:
        print('Type a valid number')

    while collatiz_number != 1:
        collatiz_number = collatiz(collatiz_number)
        print(collatiz_number)

