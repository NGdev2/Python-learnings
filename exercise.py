knowledge = 0.5

understand = lambda k: k + 0.04


def read_documentation():
    for i in range(11):
        reading_process = i * 10
        if reading_process == 50:
            print('A Half of documentation has already been read')
        elif reading_process == 100:
            global knowledge
            knowledge = understand(knowledge)
            print('Congratulations! Documentation has already successfully reading. '
                  f'You\'r knowledge increased on 1% and equal = {round(knowledge*100), 2} percents')


def exercise(necessary_knowledge):
    if read_documentation():
        print('documentation read successfully')
    if necessary_knowledge > knowledge+0.2:
        complexity = 'Hard'
    elif necessary_knowledge > knowledge+0.05:
        complexity = 'Standard'
    else:
        complexity = 'Easy'

    if complexity == 'Hard' or complexity == 'Standard':
        print('Task not easy. Don\'t worry and keep calm!')
        while knowledge < necessary_knowledge:
            read_documentation()
            print('We are on the road to success')
    else:
        print('complexity is too easy')
    return True


print(exercise(0.61))
