def greet(name, otch, surname):
    """
    функция, которая приветствует пользовате
    :name -  строка, в которой представлена имя
    """
    if otch:
        print(name + otch + surname)
    else:
        print(name+surname)


greet('semen', 'semenich','semenov' )
greet('semen', '','semenov' )
name = input("имя")
otchestvo = input("отчество")
surname = input(" фамилия")

help(greet)

greet(name, otchestvo, surname)