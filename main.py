print('задание по Технологии Программирования')
class Contact:
    everybody = {}
    all_names1 = {}
    all_names2 = {}
    all_names12 = {}
    all_names23 = {}
    all_phones = {}
    all_emails = {}
    no_emails = []
    no_phones = []
    id = 1

    def __init__(self, name, phone, email):
        Contact.everybody[Contact.id] = [name, phone, email]
        Contact.id += 1
        self.name = name
        n = name.split()
        if n[0] in Contact.all_names1.keys():
            Contact.all_names1[n[0]].append([name, phone, email])
        else:
            Contact.all_names1[n[0]] = [[name, phone, email]]
        if len(n) > 1:
            if n[1] in Contact.all_names2.keys():
                Contact.all_names2[n[1]].append([name, phone, email])
            else:
                Contact.all_names2[n[1]] = [[name, phone, email]]

            if n[0] + ' ' + n[1] in Contact.all_names12.keys():
                Contact.all_names12[n[0] + ' ' + n[1]].append([name, phone, email])
            else:
                Contact.all_names12[n[0] + ' ' + n[1]] = [[name, phone, email]]

        if len(n) > 2:
            if n[1] + ' ' + n[2] in Contact.all_names23.keys():
                Contact.all_names23[n[1] + ' ' + n[2]].append([name, phone, email])
            else:
                Contact.all_names23[n[1] + ' ' + n[2]] = [[name, phone, email]]
        if phone != '':
            if phone in Contact.all_phones.keys():
                Contact.all_phones[phone].append([name, phone, email])
            else:
                Contact.all_phones[phone] = [[name, phone, email]]
        else:
            Contact.no_phones.append([name, phone, email])
        if email != '':
            if email in Contact.all_emails.keys():
                Contact.all_emails[email].append([name, phone, email])
            else:
                Contact.all_emails[email] = [[name, phone, email]]
        else:
            Contact.no_emails.append([name, phone, email])

    def change(self, id, new_account):
        old_name = Contact.everybody[id][0]
        old_phone = Contact.everybody[id][1]
        email = Contact.everybody[id][2]
        new_phone = new_account[1]
        new_email = new_account[2]
        old_name = old_name.split()




import codecs

# file = input('Введите имя файла')
file = 'Contacts.txt'
k = 0
f = codecs.open(file, "r", "utf_8_sig")
for x in f:
    x = x[:-2:]
    pd = x.split(',')
    user = Contact(pd[0], pd[1][1::], pd[2])
f.close()

print(Contact.change(user, 3, 90909), '00')

print('Чтобы выполнить команду выберите 1- найти по номеру телефона, 2- найти по email, 3- найти по имени,'
      '4- найти по фамилии, 5- найти по Фамилия Имя, 6- найти по Имя Отчество, 7- редактирование профиля,'
      '8- найти всех без номера телефона, 9- найти всех без email')
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
elif task == 8:
    print(Contact.no_phones)
elif task == 9:
    print(Contact.no_emails)
if task == 7:
    print(Contact.everybody)
    task_id = input('Введите id изменяемого профиля')
    task_after = list(input('Введите желаемые значения для данного профиля').split())
    task_before = Contact.everybody[task_id]
    task2 = ['Иванов Иван Иванович', ' +79999999995', ' ivanov@ma.il']
print(Contact.everybody)
