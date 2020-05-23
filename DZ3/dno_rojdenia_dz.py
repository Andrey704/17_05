file = 'pi_million_digits_dz.txt'

pi_string = ''

with open(file) as f:
    lines = f.readlines()
for line in lines:
    pi_string += line


birthday = input("Введите данные рождения день и месяц в формате DDMM")
if birthday in pi_string:
    print("Клево вы в чичле ПИ")
    #print(pi_string.count(birthday))
    Index_of_B = pi_string.index(birthday)
    print('Ваше День Рождения в чиле Пи находиться на ' + str( Index_of_B ) + ' индексе')

else:
    print("вы не были избраны")