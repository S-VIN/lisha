import random

# Переменные для генерации отчёта. Количество предложений и абзацев
count_of_sentences = 3
count_of_paragraphes = 3

# Открываем файл с таблицей. В качестве разделителя используются табы.
f = open('template.txt', 'r')

# Заводим список под строчки из таблицы.
raw_lines = list()

# Считываем строчки из файла и разбиваем их.
for line in f:
    raw_lines.append(line.split("	"))

# Список упорядоченный по столбцам (перевёрнутая таблица). Нужен для удобства вывода.
template = list()

# Переворачиваем таблицу.
for j in range(len(raw_lines[0])):
    column = list()
    for i in range(len(raw_lines)):
        column.append(raw_lines[i][j])
    template.append(column)

# Выводим в консоль случайное значение их столбца. 
for i in range(count_of_paragraphes):
    for j in range(count_of_sentences):
        for k in range(len(template)):
            print(random.choice(template[k]), end="")
    print()
    print()

