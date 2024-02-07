import os
import shutil

def create_file():
    file_path = input("Введите путь к файлу: ")
    try:

        with open(file_path, 'w'):
            pass
        print(f"Файл '{file_path}' успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла '{file_path}': {e}")


def delete_file():
    file_path = input("Введите путь к файлу: ")
    try:
        os.remove(file_path)
        print(f"Файл '{file_path}' успешно удален.")
    except Exception as e:
        print(f"Ошибка при удалении файла '{file_path}': {e}")

def move_file():
    source = input("Введите исходный путь файла: ")
    destination = input("Введите путь назначения: ")
    try:
        shutil.move(source, destination)
        print(f"Файл '{source}' успешно перемещен в '{destination}'.")
    except Exception as e:
        print(f"Ошибка при перемещении файла '{source}': {e}")

def copy_file():
    source = input("Введите исходный путь файла: ")
    destination = input("Введите путь назначения: ")
    try:
        shutil.copy2(source, destination)
        print(f"Файл '{source}' успешно скопирован в '{destination}'.")
    except Exception as e:
        print(f"Ошибка при копировании файла '{source}': {e}")

def create_directory():
    directory_path = input("Введите путь к папке: ")
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Папка '{directory_path}' успешно создана.")
    except Exception as e:
        print(f"Ошибка при создании папки '{directory_path}': {e}")

def delete_directory():
    directory_path = input("Введите путь к папке: ")
    try:
        shutil.rmtree(directory_path)
        print(f"Папка '{directory_path}' успешно удалена.")
    except Exception as e:
        print(f"Ошибка при удалении папки '{directory_path}': {e}")

def display_menu():
    print("Меню файлового менеджера")
    print("1. Создать файл")
    print("2. Удалить файл")
    print("3. Переместить файл")
    print("4. Скопировать файл")
    print("5. Создать папку")
    print("6. Удалить папку")
    print("7. Выход")

def main():
    while True:
        display_menu()
        choice = input("Введите ваш выбор (1-7): ")
        if choice == '1':
            create_file()
        elif choice == '2':
            delete_file()
        elif choice == '3':
            move_file()
        elif choice == '4':
            copy_file()
        elif choice == '5':
            create_directory()
        elif choice == '6':
            delete_directory()
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

# Запуск программы
main()