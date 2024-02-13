def collatiz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1

collatiz_number = int(input('Enter a Number: '))

while collatiz_number != 1:
    collatiz_number = collatiz(collatiz_number)
    print(collatiz_number)