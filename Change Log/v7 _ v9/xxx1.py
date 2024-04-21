

--------------------------------------------------

Принимает ответами только цыфры эти: 1,2
Если он ввел "1" то программа выводит строку "Это 1".
Если он ввел "2" то программа выводит строку "Это 2".
Консольное окно не закрывается после выпонения и она ждет пока я не введу "q".
Если пользователь ввел "q" в любом месте где она спрашивает что-то, тогда завершить исполнение програмы.

--------------------------------------------------

while True:
    answer = input("Введите 1 или 2: ")
    if answer == "1":
        print("Это 1")
    elif answer == "2":
        print("Это 2")
    elif answer == "q":
        break
    else:
        print("Вы ввели неправильный ответ")
print("Программа завершена.")


--------------------------------------------------
надо чтоб она их не обрезала расширения файлов при переименовании. в этом и есть баг что она обрезает. надо баг устранить этот
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
                    new_path = os.path.join(file_path_2, array_2[i] + os.path.splitext(filename)[1])
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
                        new_path = os.path.join(file_path_2, array_2[i] + os.path.splitext(filename)[1])
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



