# Задание 4.

# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).

lst = ['разработка', 'администрирование', 'protocol', 'standard']
i = 0
while i < len(lst):
    lst[i]=lst[i].encode('UTF-8')
    i+=1
print(lst)
i=0
while i < len(lst):
    lst[i]= bytes.decode(lst[i],'UTF-8')
    i+=1
print(lst)
