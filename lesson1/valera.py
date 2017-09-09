a = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
c = input("Введите имя ")

def find_person(name):
    for el in a:
        if el == name:
            print("{} нашелся".format(name))
        else:
            print("{} не {}".format(el, name))


find_person(c)