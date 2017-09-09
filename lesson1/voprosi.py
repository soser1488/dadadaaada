def ask_user():
    print("Как дела?")
    while True:
        a = input("Введите Пока и я отстану: ")
        kek = get_answer(a)



def get_answer(c):
    if c == "Пока":
        exit()
    else:
        return False

ask_user()