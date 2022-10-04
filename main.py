print('задание по Технологии Программирования')


class Contact:
    # это все люди с их уникальными id и их данными
    everybody = {}
    # это словарик, где ключом является фамилия, а значениями-люди, которые имеют эту фамилию
    all_names1 = {}
    # это словарик, где ключом является имя, а значениями-люди, которые имеют это имя
    all_names2 = {}
    # это словарик, где ключом является фамилия имя, а значениями-люди, которые имеют эту фамилию и имя
    all_names12 = {}
    # это словарик, где ключом является имя отчество, а значениями-люди, которые имеют эти имя отчество
    all_names23 = {}
    # это словарик со всеми телефонами
    all_phones = {}
    # это словарик со всеми емайлами
    all_emails = {}
    # это словарик для тех, у кого нет емайла
    no_emails = []
    # это словарик для тех, у кого нет телефона
    no_phones = []
    id = 0

    def __init__(self, name, phone, email):
        Contact.everybody[Contact.id] = [name, phone, email]
        Contact.id += 1
        self.name = name
        n = name.split()
        if n[0] in Contact.all_names1.keys():
            Contact.all_names1[n[0]].append(Contact.id)
        else:
            Contact.all_names1[n[0]] = [Contact.id]
        if len(n) > 1:
            if n[1] in Contact.all_names2.keys():
                Contact.all_names2[n[1]].append(Contact.id)
            else:
                Contact.all_names2[n[1]] = [Contact.id]

            if n[0] + ' ' + n[1] in Contact.all_names12.keys():
                Contact.all_names12[n[0] + ' ' + n[1]].append(Contact.id)
            else:
                Contact.all_names12[n[0] + ' ' + n[1]] = [Contact.id]

        if len(n) > 2:
            if n[1] + ' ' + n[2] in Contact.all_names23.keys():
                Contact.all_names23[n[1] + ' ' + n[2]].append(Contact.id)
            else:
                Contact.all_names23[n[1] + ' ' + n[2]] = [Contact.id]
        if phone != '':
            if phone in Contact.all_phones.keys():
                Contact.all_phones[phone].append(Contact.id)
            else:
                Contact.all_phones[phone] = [Contact.id]
        else:
            Contact.no_phones.append(Contact.id)
        if email != '':
            if email in Contact.all_emails.keys():
                Contact.all_emails[email].append(Contact.id)
            else:
                Contact.all_emails[email] = [Contact.id]
        else:
            Contact.no_emails.append(Contact.id)

    def change(self, id, new_account):
        old_name = Contact.everybody[id][0]
        old_phone = Contact.everybody[id][1]
        old_email = Contact.everybody[id][2]
        new_name_list = new_account[0].split()
        new_phone = new_account[1]
        new_email = new_account[2]
        old_name_list = old_name.split()
        Contact.everybody[id] = new_account
        if old_phone != new_phone:
            if old_phone == '':
                if id in Contact.no_phones:
                    Contact.no_phones.remove(id)
            if new_phone in Contact.all_phones.keys():
                Contact.all_phones[new_phone].append(id)
            elif new_phone!='':
                Contact.all_phones[new_phone]=[id]
            else:
                Contact.no_phones.append(id)
        if old_email != new_email:
            if old_email == '':
                if id in Contact.no_emails:
                    Contact.no_emails.remove(id)
            if new_email in Contact.all_emails.keys():
                Contact.all_emails[new_email].append(id)
            elif new_email!='':
                Contact.all_emails[new_email]=[id]
            else:
                Contact.no_emails.append(id)
        if old_name_list[0] != new_name_list[0]:
            # если поменяли фамилию
            if id in Contact.all_names1[old_name_list[0]]:
                Contact.all_names1[old_name_list[0]].remove(id)
            if new_name_list[0] in Contact.all_names1.keys():
                Contact.all_names1[new_name_list[0]].append(id)
            else:
                Contact.all_names1[new_name_list[0]]=[id]
            # если поменяли имя
            if len(old_name_list) > 2:
                if id in Contact.all_names2[old_name_list[1]]:
                    Contact.all_names2[old_name_list[1]].remove(id)
            if len(new_name_list) > 2:
                if new_name_list[1] in Contact.all_names2.keys():
                    Contact.all_names2[new_name_list[1]].append(id)
                else:
                    Contact.all_names2[new_name_list[1]]=[id]
            # другие общие изменения
            if len(old_name_list) > 1 and id in Contact.all_names12[old_name_list[0] + ' ' + old_name_list[1]]:
                Contact.all_names12[old_name_list[0] + ' ' + old_name_list[1]].remove(id)
            if len(new_name_list) > 1:
                if new_name_list[0] + ' ' + new_name_list[1] in Contact.all_names12.keys():
                    Contact.all_names12[new_name_list[0] + ' ' + new_name_list[1]].append(id)
                else:
                    Contact.all_names12[new_name_list[0] + ' ' + new_name_list[1]]=[id]
            if len(old_name_list) > 2 and id in Contact.all_names23[old_name_list[1] + ' ' + old_name_list[2]]:
                Contact.all_names23[old_name_list[1] + ' ' + old_name_list[2]].remove(id)
            if len(new_name_list) > 2:
                if new_name_list[1] + ' ' + new_name_list[2] in Contact.all_names23.keys():
                    Contact.all_names23[new_name_list[1] + ' ' + new_name_list[2]].append(id)
                else:
                    Contact.all_names23[new_name_list[1] + ' ' + new_name_list[2]]=[id]


import codecs

file = input('Введите имя файла')
k = 0
f = codecs.open(file, "r", "utf_8_sig")
for x in f:
    x = x[:-2:]
    pd = x.split(',')
    user = Contact(pd[0], pd[1][1::], pd[2])
f.close()
print('Выполняем поиск? + если да, - если нет')
while input() != '-':
    print('Чтобы выполнить команду выберите 1- найти по номеру телефона, 2- найти по email, 3- найти по имени,'
          '4- найти по фамилии, 5- найти по Фамилия Имя, 6- найти по Имя Отчество, 7- редактирование профиля,'
          '8- найти всех без номера телефона, 9- найти всех без email. Если хотите увидеть всех пользователей,'
          'введите 123'
          'Программа будет выполнять поиск до тех пор, пока вы не выберете -')
    task = int(input())
    if task == 1:
        print('Введите номер телефона')
        task_phone = input()
        print('По вашему запросу нашлось: ', *Contact.all_phones[task_phone])
    elif task == 2:
        print('Введите email')
        task_email = input()
        print('По вашему запросу нашлось: ', *Contact.all_emails[task_email])
    elif task == 3:
        print('Введите имя пользователя')
        task_name = input()
        print('По вашему запросу нашлось: ', *Contact.all_names2[task_name])
    elif task == 4:
        print('Введите фамилию пользователя')
        task_name = input()
        print('По вашему запросу нашлось: ', *Contact.all_names1[task_name])
    elif task == 5:
        print('Введите фамилию и имя пользователя')
        task_name = input()
        print('По вашему запросу нашлось: ', *Contact.all_names12[task_name])
    elif task == 6:
        print('Введите имя и отчество пользователя')
        task_name = input()
        print('По вашему запросу нашлось: ', *Contact.all_names23[task_name])
    elif task == 8:
        print(Contact.no_phones)
    elif task == 9:
        print(Contact.no_emails)
    elif task == 123:
        # выводим всех пользователей в консоль
        print(Contact.everybody)
    if task == 7:
        print(Contact.everybody)
        task_id = int(input('Введите id изменяемого профиля'))
        task_after = list(input('Введите желаемые значения для данного профиля').split())
        Contact.change(user, task_id, task_after)
    print('Выполняем поиск? + если да, - если нет')
print('До следующего раза!')
