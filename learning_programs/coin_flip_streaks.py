import random

number_streaks = 0

for experiment_number in range(10):

    coin_flip_list = []
    tail_head = ["T", "H"]

    for i in range(100):
        letter = random.choice(tail_head)
        coin_flip_list.append(letter)

    count_t = 0
    count_h = 0

    for letter in coin_flip_list:
        if letter == "T":
            count_t += 1
            count_h = 0
        else:
            count_h += 1
            count_t = 0
    if count_h or count_t == 6:
        number_streaks += 1
    print(coin_flip_list)
print(number_streaks)
