# Задание 6.

# Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор».

from chardet import detect

resurs_string = ['сетевое программирование', 'сокет', 'декоратор']

with open('text.txt', 'w') as file:
    for i in resurs_string:
        file.write(f'{i}; ')

def convert():
    with open('text.txt', 'rb') as file_obj:
        cont_bytes = file_obj.read()
    detected = detect(cont_bytes)
    print(detect)
    encoding = detected['encoding']
    cont_text = cont_bytes.decode(encoding)
    with open('text.txt', 'w', encoding='UTF-8') as file_obj:
        file_obj.write(cont_text)
convert()

with open('text.txt', 'r', encoding='UTF-8') as file:
    for i in file:
        print(i)
