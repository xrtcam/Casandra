


--------------------------------------------------
Нужно изменить эту программу и добавить функционал так, чтобы она при запуске открывала терминал или консольное окно, и спрашивала пользователя какое действие будем выполнять.

Такие вопросы она задаёт пользователю:
"1. Search, Move"
"2. Search, Move, Rename"

Принимает ответами только цыфры эти: 1,2

Если он ввел "1" то программа ищет то что она тут ищет как ты видешь по коду, и переносит без переименования того что перенесла.

Если он ввел "2" то программа выполняет то что она и так сейчас выполняет. Тоесть ищет переносит и переименовывает.

--------------------------------------------------

import os
import shutil

file_path_1 = "D:\\repx\\img"
file_path_2 = "D:\\Logic\\111"
file_path_3 = "D:\\repx"
file_1 = "xxx_1.txt"
file_2 = "xxx_2.txt"

array_1 = []
array_2 = []

with open("xvx.txt", "r", encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(" - ")
        array_1.append(parts[0])
        array_2.append(parts[1])

for i in range(len(array_1)):
    foldername_found = False
    for foldername, subfolders, filenames in os.walk(file_path_1):
        if array_1[i] in foldername:
            # нашли папку с нужной подстрокой
            foldername_found = True
            new_path = os.path.join(file_path_2, array_2[i])
            shutil.move(foldername, new_path)
            with open(file_1, "a", encoding='utf-8') as f:
                f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
            break
    if not foldername_found:
        # папка с нужной подстрокой не найдена в первой директории, ищем вторую
        for foldername, subfolders, filenames in os.walk(file_path_3):
            if array_1[i] in foldername:
                # нашли папку с нужной подстрокой
                foldername_found = True
                new_path = os.path.join(file_path_2, array_2[i])
                shutil.move(foldername, new_path)
                with open(file_1, "a", encoding='utf-8') as f:
                    f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
                break
    if not foldername_found:
        # папка с нужной подстрокой не найдена ни в одной директории, ищем файлы
        for foldername, subfolders, filenames in os.walk(file_path_1):
            for filename in filenames:
                if array_1[i] in filename:
                    # нашли файл с нужной подстрокой в первой директории
                    foldername_found = True
                    new_path = os.path.join(file_path_2, array_2[i])
                    shutil.move(os.path.join(foldername, filename), new_path)
                    with open(file_1, "a", encoding='utf-8') as f:
                        f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
                    break
            if foldername_found:
                break
        if not foldername_found:
            # файл с нужной подстрокой не найден в первой директории, ищем вторую
            for foldername, subfolders, filenames in os.walk(file_path_3):
                for filename in filenames:
                    if array_1[i] in filename:
                        # нашли файл с нужной подстрокой во второй директории
                        foldername_found = True
                        new_path = os.path.join(file_path_2, array_2[i])
                        shutil.move(os.path.join(foldername, filename), new_path)
                        with open(file_1, "a", encoding='utf-8') as f:
                            f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
                        break
                if foldername_found:
                    break
    if not foldername_found:
        # папка или файл с нужной подстрокой не найдена ни в одной директории
        with open(file_2, "a", encoding='utf-8') as f:
            f.write(f"Не найдено - {array_1[i]} - {array_2[i]}\n")

--------------------------------------------------
Измененный код, учитывающий добавленный функционал:
--------------------------------------------------

import os
import shutil
import subprocess

file_path_1 = "D:\\repx\\img"
file_path_2 = "D:\\Logic\\111"
file_path_3 = "D:\\repx"
file_1 = "xxx_1.txt"
file_2 = "xxx_2.txt"

def main():
    while True:
        action = input("Введите действие (1 - Search, Move / 2 - Search, Move, Rename): ")
        if action == "1":
            search_and_move()
            break
        elif action == "2":
            search_and_move_with_rename()
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

def search_and_move():
    array_1 = []
    array_2 = []

    with open("xvx.txt", "r", encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(" - ")
            array_1.append(parts[0])
            array_2.append(parts[1])

    for i in range(len(array_1)):
        foldername_found = False
        for foldername, subfolders, filenames in os.walk(file_path_1):
            if array_1[i] in foldername:
                # нашли папку с нужной подстрокой
                foldername_found = True
                new_path = os.path.join(file_path_2, array_2[i])
                shutil.move(foldername, new_path)
                with open(file_1, "a", encoding='utf-8') as f:
                    f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
                break
        if not foldername_found:
            # папка с нужной подстрокой не найдена в первой директории, ищем вторую
            for foldername, subfolders, filenames in os.walk(file_path_3):
                if array_1[i] in foldername:
                    # нашли папку с нужной подстрокой
                    foldername_found = True
                    new_path = os.path.join(file_path_2, array_2[i])
                    shutil.move(foldername, new_path)
                    with open(file_1, "a", encoding='utf-8') as f:
                        f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
                    break
        if not foldername_found:
            # папка с нужной подстрокой не найдена ни в одной директории, ищем файлы
            for foldername, subfolders, filenames in os.walk(file_path_1):
                for filename in filenames:
                    if array_1[i] in filename:
                        # нашли файл с нужной подстрокой в первой директории
                        foldername_found = True
                        new_path = os.path.join(file_path_2, array_2[i])
                        shutil.move(os.path.join(foldername, filename), new_path)
                        with open(file_1, "a", encoding='utf-8') as f:
                            f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
                        break
                if foldername_found:
                    break
            if not foldername_found:
                # файл с нужной подстрокой не найден в первой директории, ищем вторую
                for foldername, subfolders, filenames in os.walk(file_path_3):
                    for filename in filenames:
                        if array_1[i] in filename:
                            # нашли файл с нужной подстрокой во второй директории
                            foldername_found = True
                            new_path = os.path.join(file_path_2, array_2[i])
                            shutil.move(os.path.join(foldername, filename), new_path)
                            with open(file_1, "a", encoding='utf-8') as f:
                                f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
                            break
                    if foldername_found:
                        break
        if not foldername_found:
            # папка или файл с нужной подстрокой не найдена ни в одной директории
            with open(file_2, "a", encoding='utf-8') as f:
                f.write(f"Не найдено - {array_1[i]} - {array_2[i]}\n")

def search_and_move_with_rename():
    array_1 = []
    array_2 = []
    array_3 = []

    with open("xvx.txt", "r", encoding='utf-8') as file:
        for line in file:
            parts = l
--------------------------------------------------



