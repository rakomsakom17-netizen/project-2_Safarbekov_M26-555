import prompt

HELP_MESSAGE = (
    "<command> exit - выйти из программы\n"
    "<command> help - справочная информация"
)


def welcome():
    print("Первая попытка запустить проект!\n")
    print("***")
    print(HELP_MESSAGE)

    while True:
        command = prompt.string("Введите команду: ")
        if command == "exit":
            break
        elif command == "help":
            print(f"\n{HELP_MESSAGE}")