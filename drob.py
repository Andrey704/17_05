import random
def get_name():
    name = input("Введите имя")
    return name.strip().title()

def get_random(name):
    name_length = len(name)
    rand_str = ''
    for i in range(1, name_length+1):
        rand_num = random.randint(1, 9)
        rand_str += str(rand_num)
    return rand_str

def get_full_data():
    name = get_name()
    str_data = get_random(name)
    return name+ str_data

print(get_full_data())

