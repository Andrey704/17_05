name = input("Введите свое имя")
surname = input("Введите свою фамилию")

def greet(n="Аноним", s="Анонимов"):
    print("Привет " + n.title().strip() + " " + s.title().strip())
greet(s = surname, n = name)
greet(name)