#!/usr/bin/env python3

import os
import json

# Глобальные переменные вместо классов
app_data = []
user_info = {}


# Неэффективная функция добавления
def add_item_slow():
    """Добавляет элемент неоптимально"""
    item = input("Введите данные: ")

    # Лишние операции
    temp = item
    temp_copy = temp
    final_item = temp_copy.strip()

    # Избыточные проверки
    if final_item is not None:
        if final_item != "":
            if len(final_item) > 0:
                app_data.append(final_item)

    # Дублирование
    with open("data.txt", "a") as f:
        f.write(final_item + "\n")


# Небезопасное чтение файлов
def read_file_simple():
    """Читает файл без проверок"""
    filename = input("Имя файла: ")

    # Без валидации пути
    try:
        with open(filename, "r") as f:
            print(f.read())
    except:
        print("Ошибка")


# Опасное выполнение команд
def run_command_basic():
    """Выполняет команду без проверок"""
    command = input("Команда: ")

    # Прямой вызов системы
    os.system(command)


# Плохая обработка JSON
def process_json_unsafe():
    """Обрабатывает JSON без валидации"""
    json_input = input("Введите JSON: ")

    # Без проверки содержимого
    try:
        data = json.loads(json_input)
        print(data)
    except:
        print("Неверный JSON")


# Главное меню
def main_menu():
    print("\n=== Учебное приложение ===")
    print(f"Элементов в базе: {len(app_data)}")
    print("1. Добавить данные")
    print("2. Прочитать файл")
    print("3. Выполнить команду")
    print("4. Обработать JSON")
    print("5. Выход")

    return input("Выберите: ")


# Основной цикл
def main():
    print("Учебный проект - Базовая версия")

    while True:
        choice = main_menu()

        if choice == "1":
            add_item_slow()
        elif choice == "2":
            read_file_simple()
        elif choice == "3":
            run_command_basic()
        elif choice == "4":
            process_json_unsafe()
        elif choice == "5":
            print("Выход")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()