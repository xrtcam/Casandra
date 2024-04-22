import os
import shutil

file_path_1 = "D:\\repx\\cam"
file_path_2 = "D:\\Logic\\Camera\\111"
file_path_3 = "D:\\repx"
file_1 = "res\\xxx_1.txt"
file_2 = "res\\xxx_2.txt"

array_1 = []
with open('xvx_1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        array_1.append(line.strip())

array_2 = []
with open('xvx_2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        array_2.append(line.strip())

for i in range(len(array_1)):
    foldername_found = False
    for foldername, subfolders, filenames in os.walk(file_path_1):
        if array_1[i] in foldername:
            # нашли папку с нужной подстрокой
            foldername_found = True
            new_path = os.path.join(file_path_2, array_2[i])
            shutil.move(foldername, new_path)
            with open(file_1, "a") as f:
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
                with open(file_1, "a") as f:
                    f.write(f"OK - {array_1[i]} - {array_2[i]}\n")
                break
    if not foldername_found:
        # папка с нужной подстрокой не найдена ни в одной директории
        with open(file_2, "a") as f:
            f.write(f"Не найдено - {array_1[i]} - {array_2[i]}\n")