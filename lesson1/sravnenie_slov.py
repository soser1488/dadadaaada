c = input('Введите слово')
d = input('Введите слово')
def jopa(a, b):
    if a == b:
        return 1
    elif a != b:
        if b == 'learn':
            return 3
        else:
            return 2



print(jopa(c, d))