with open('text.txt', 'wt', encoding='utf-8') as inFile:
    num = int(input())
    line = ('1/' + str(num) + ' = ' + str(1/num))
    print(line)
    inFile.write(line)
#выполняет критические функции. если ввели данные после которых произойдет ошибка, чтоб нежелательные изменения и данные
# не были записаны и пользователь не имел доступ к данным, закрывает после выполнения или ошибки текстовый