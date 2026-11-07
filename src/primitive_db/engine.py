import shlex

from primitive_db.core import create_table, drop_table, list_tables
from primitive_db.utils import load_metadata, save_metadata

DB_META_FILE = "db_meta.json"


def print_help():
    """Prints the help message for the current mode."""
    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")

    print("\nОбщие команды:")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n")


def run():
    print_help()
    while True:
        metadata = load_metadata(DB_META_FILE)

        try:
            user_input = input(">>>Введите команду: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break

        if not user_input:
            continue

        try:
            args = shlex.split(user_input)
        except ValueError as err:
            print(f"Ошибка разбора команды: {err}")
            continue

        command = args[0]
        cmd_args = args[1:]

        match command:
            case "exit":
                break

            case "help":
                print_help()

            case "create_table":
                if not cmd_args:
                    print("Ошибка: Укажите имя таблицы.")
                    continue
                table_name = cmd_args[0]
                columns = cmd_args[1:]
                new_meta = create_table(metadata, table_name, columns)
                if new_meta is not None:
                    save_metadata(DB_META_FILE, new_meta)

            case "drop_table":
                if not cmd_args:
                    print("Ошибка: Укажите имя таблицы.")
                    continue
                table_name = cmd_args[0]
                new_meta = drop_table(metadata, table_name)
                if new_meta is not None:
                    save_metadata(DB_META_FILE, new_meta)

            case "list_tables":
                list_tables(metadata)

            case _:
                print(f"Функции '{command}' нет. Попробуйте снова.")