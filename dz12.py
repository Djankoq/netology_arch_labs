import os
import stat

def print_filesystem_info(path):
    print(f"\nИнформация о файловой системе для пути: {path}")
    try:
        stats = os.statvfs(path)

        print(f"Размер блока: {stats.f_bsize} байт")
        print(f"Фрагментный размер: {stats.f_frsize} байт")
        print(f"Общее количество блоков: {stats.f_blocks}")
        print(f"Свободных блоков: {stats.f_bfree}")
        print(f"Доступных блоков для непривилегированных процессов: {stats.f_bavail}")
        print(f"Общее количество inode: {stats.f_files}")
        print(f"Свободных inode: {stats.f_ffree}")
        print(f"Максимальная длина имени файла: {stats.f_namemax}")
    except AttributeError:
        print("Функция statvfs не поддерживается в этой ОС.")

def print_file_info(file_path):
    print(f"\nИнформация о файле: {file_path}")
    try:
        info = os.stat(file_path)

        print(f"Inode: {info.st_ino}")
        mode = info.st_mode
        print(f"Тип файла: {file_type(mode)}")
        print(f"Атрибуты файла (st_mode): {oct(mode)}")

        print(f"Размер файла: {info.st_size} байт")
        print(f"Последний доступ: {info.st_atime}")
        print(f"Последнее изменение: {info.st_mtime}")
        print(f"Последняя мета-изменение (ctime): {info.st_ctime}")
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")

def file_type(mode):
    if stat.S_ISDIR(mode):
        return "Каталог"
    elif stat.S_ISREG(mode):
        return "Обычный файл"
    elif stat.S_ISLNK(mode):
        return "Символическая ссылка"
    elif stat.S_ISCHR(mode):
        return "Символьное устройство"
    elif stat.S_ISBLK(mode):
        return "Блочное устройство"
    elif stat.S_ISFIFO(mode):
        return "FIFO (именованный канал)"
    elif stat.S_ISSOCK(mode):
        return "Сокет"
    else:
        return "Неизвестный тип"

if __name__ == "__main__":
    path = "/"
    print_filesystem_info(path)

    file_path = input("\nВведите путь к файлу для анализа: ")
    print_file_info(file_path)