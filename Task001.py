# Напишите программу, удаляющую из текста все слова содержащие "абв".

my_text = 'Эта программа будетабв будет удалять всеабв абв все слова содержащие в себе три буквы а б в'


def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


my_text = del_some_words(my_text)
print(my_text)
