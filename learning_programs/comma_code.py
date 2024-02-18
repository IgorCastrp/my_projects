def comma_code(food):
    foods = ''
    for i, item in enumerate(food):
        if i == len(food) - 2:
            foods += item + ' and '
        elif i == len(food) - 1:
            foods += item
        else:
            foods += item + ', '
    return foods




food = ['beef', 'tomato', 'banana', 'hamburger', 'apple', 'rice']
test = comma_code(food)
print(test)


