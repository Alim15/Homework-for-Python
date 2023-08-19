
def initialization():
    with open('phonebook.txt', 'a', encoding ='utf-8') as data:
        data.write('Лобачевский Николай Иванович\n')
        data.write('Курчатов Игорь Васильевич\n')
        data.write('Ломоносов Михаил Васильевич\n')


def add_information(str):
    name=input("Введите имя:")
    surname=input("Введите фамилию:")
    phonenumber=input("Введите номер телефона")
    while not phonenumber.isdigit():
        phonenumber = input("Введите номер телефона")
    str=f'{name} {surname} {phonenumber} \n'
    with open('phonebook.txt', 'w+', encoding='utf-8') as data:
        data.write(str)




def find_information(str):
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if str.lower() in line.lower().split():
                print(line, end='')

def delete_information(str):
    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        for line in data:
            if str.lower() in line.lower().split():
                data.writelines('')




while True:
    que=input('\nadd , find , stop, delete : ')
    if que.lower()=='stop':
        break
    if que.lower() == 'find':
        str=input("Что ищем?")
        find_information(str)
    if que.lower() == 'add':
        add_information(str)
    if que.lower() == 'delete':
        str = input("Что ищем?")
        delete_information(str)



