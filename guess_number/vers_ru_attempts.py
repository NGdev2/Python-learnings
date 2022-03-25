import random
answer = None


def randoms(min, max):
    return random.randint(min, max)


rnd = randoms(1, 50)


for i in range(6):
    answer = int(input('Угадайте число от 1 до 50\n'))
    if answer == rnd:
        print('Congratulations. You Win!!!')
        break
    else:
        if answer > rnd:
            print(f'Загаданное число меньше, у вас осталось {5-i} попыток')
        else:
            print(f'Загаданное число больше, у вас осталось {5-i} попыток')