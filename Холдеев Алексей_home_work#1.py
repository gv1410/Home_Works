# Домашнее задание №1.
# Исполнитель: Холдеев Алексей


text = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'

characters = len(text)

text_inversion = text[::-1]

new_text = text.replace('Лондоне', 'Стамбуле')

def number():
    str_value_nd = 'нд'
    str_value_am = 'ам'
    str_value_o = 'о'
    number_of_value_nd = text.count(str_value_nd)
    number_of_value_am = text.count(str_value_am)
    number_of_value_o = text.count(str_value_o)
    print(f'Количество вхождений значения \'{str_value_nd}\' = ' + str(number_of_value_nd) + f', значения \'{str_value_am}\' = ' + str(number_of_value_am) + f', значения \'{str_value_o}\' = ' + str(number_of_value_o) + '\n')

print(f'Количество символов - {characters}\n')
print(f'Инверсная строка будет выглядеть так: {text_inversion} \n')
print('Каждое слово в предложении с большой буквы выглядит так: ' + text.title() + '\n')
print('Весь текст написаный прописными буквами выглядит так: ' + text.upper() + '\n')
number() # Функция возвращает количество вхождений значений ("НД", "ам", "о")
print('Свои упражнения: \n' + '\t' + new_text + '\n' + '\t' + str(new_text.split(','))) #Замена слова "Лондоне" на "Стамбуле" в исходной строке, разбиение строки по символу запятой
print('Исходная строка: ' + text)
print('Исходная строка: ' + text)