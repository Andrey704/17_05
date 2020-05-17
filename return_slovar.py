import random
persons = {'names': [], 'surnames':[]}

def create_person(name, surname):
    """ Возвращает словарь с информацией о человеке"""
    persons['names'].append(name)
    persons['surnames'].append(surname)
    return persons

user_size = int(input("Сколько пользователей вы хотите занести?"))
for user in range(user_size):
    name = input("Введите имя пользователя")
    surname = input("Фамилию пользователя")
    create_person(name=name, surname=surname)

# keys = list(persons.keys())
# for slovo in keys:
#     rand = random.choice(keys)
#     print(persons[rand])
#     keys.remove(slovo)
# print(keys)
funny_words = ['хороший', 'веселый']

def speech_funny(slovar):
    for i in range(len(slovar['names'])):
        rand_word = random.choice(funny_words)
        greet = rand_word + " " + slovar['names'][i] + " " + slovar['surnames'][i]
        print(greet)
speech_funny(persons)


