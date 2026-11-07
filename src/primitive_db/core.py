VALID_TYPES = {"int", "str", "bool"}


def create_table(metadata, table_name, columns):
    if table_name in metadata:
        print(f'Ошибка: Таблица "{table_name}" уже существует.')
        return None

    parsed_columns = []
    has_id = False

    for col in columns:
        if ":" not in col:
            print(f"Некорректное значение '{col}'. Попробуйте снова.")
            return None

        col_name, col_type = col.split(":", 1)
        col_name = col_name.strip()
        col_type = col_type.strip()

        if col_type not in VALID_TYPES:
            print(f"Некорректное значение '{col_type}'. Попробуйте снова.")
            return None

        if col_name.lower() == "id":
            has_id = True
            parsed_columns.append(f"ID:{col_type}")
        else:
            parsed_columns.append(f"{col_name}:{col_type}")

    if not has_id:
        parsed_columns.insert(0, "ID:int")

    metadata[table_name] = parsed_columns
    print(f'Таблица "{table_name}" успешно создана со столбцами:\
 {", ".join(parsed_columns)}')
    return metadata


def drop_table(metadata, table_name): 
    if table_name not in metadata:
        print(f'Ошибка: Таблица "{table_name}" не существует.')
        return None

    del metadata[table_name]
    print(f'Таблица "{table_name}" успешно удалена.')
    return metadata


def list_tables(metadata):

    if not metadata:
        return
    for table_name in metadata:
        print(f"- {table_name}")