import copy

spam = [1, 2, 3]
print(id(spam))

cheese = copy.copy(spam)
cheese[0] = 392

print(cheese)
print(spam)