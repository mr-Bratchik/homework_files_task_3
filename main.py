# Читаем текст из файла и сохраняем его в словарь
def text_list(file_paths):
    text_files = {}
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            text = file.read()
            text_files[file_path] = text
    return text_files


# Считаем количество строк в файле
def string_count(file_path):
    count = 0
    with open(file_path) as f:
        for line in f:
            count += 1
    return count


# Создаем словарь с количеством строк в файлах
def file_dict(file_paths):
    f_dict = {}
    for file_path in file_paths:
        f_dict[file_path] = string_count(file_path)
    return f_dict


# Сортируем словарь по увеличению количества строк в значении
def sorted_file_dict(f_dict):
    sorted_f_dict = {}
    for file_path, counts in sorted(f_dict.items(), key=lambda item: item[1]):
        sorted_f_dict[file_path] = counts
    return sorted_f_dict


# Записываем файлы в новый файл согласно условию
def write_text(other_path, sorted_f_dict, text_files):
    with open(other_path, 'w') as file:
        for name_file, counts in sorted_f_dict.items():
            file.write(f'{name_file}\n {counts}\n{text_files[name_file]}\n')


file_paths = ['1.txt', '2.txt', '3.txt']
other_path = 'final_file.txt'
text_files = text_list(file_paths)
write_text(other_path, sorted_file_dict(file_dict(file_paths)), text_files)
