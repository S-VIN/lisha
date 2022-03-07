# Форма генерации: GGGG-NN-YY (GGGG - группа сокращение, NN - номер группы, YY - год поступления)

# Создаём список групп из введеной строки. Сразу парсим сроку в список.
groups = input('Type the string with groups. Space is split character.\n').split()

# Вводим год поступления
# Преобразуем в int, чтобы раньше упасть, если ввод неправильный.
year = int(input('Type the year.\n'))

# Для каждого сокращения вводим количество групп. Тоже сразу парсим его.
# Преобразуем в int, чтобы раньше упасть, если ввод неправильный.
number_of_classes = list()
for item in groups:
    number_of_classes.append(int(input('Type the number of groups ' + item + ' group. \n')))

# Выводим перебор по группам. Добавляем год поступления в конце.
for i in range(len(groups)):
    for j in range(int(number_of_classes[i])):
        group_string = groups[i] + '-' + str(j + 1) + '-' + str(year)
        print(group_string)