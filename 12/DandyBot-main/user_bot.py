# Сначала мы в setup (запускается один раз из-за first_setup) наполняем command_list командами
# Потом мы в тиках по одному обрабатываем пул комманд

# Список с командами
command_list = list()

first_setup = True


# Добавляем команду в список команд
# Комманда - лист, [направление, число шагов по направлению]
def go(direction, number):
    command_list.append([direction, number])
    return


def go_and_take(direction, number):
    for i in range(number):
        go(direction, 1)
        go("take", 1)
        

# Функция запускается один раз и наполняет командами пул
def setup():
    global first_setup
    if not first_setup:
        return
    first_setup = False
    
    # first level
    go("right", 30)
    go("left", 7)
    go_and_take("right", 6)
    go_and_take("down", 4)
    
    # second level
    go("right", 1)
    go_and_take("up", 10)
    go_and_take("right", 4)
    go_and_take("down", 8)
    go_and_take("right", 4)
    go_and_take("up", 9)
    go_and_take("right", 4)
    go_and_take("down", 9)
    go_and_take("right", 4)
    go_and_take("up", 9)
    go_and_take("right", 4)
    go_and_take("down", 9)
    go_and_take("right", 4)
    go_and_take("up", 9)
    go_and_take("right", 4)

    # third level
    go("left", 2)
    go("take", 1)
    go("up", 7)
    go("take", 1)
    go("down", 7)
    go("right", 7)
    go("take", 1)
    go("up", 9)
    go("right", 5)
    go_and_take("up", 2)
    go_and_take("right", 1)
    go_and_take("down", 1)
    go("down", 1)

    go("right", 5)
    go("down", 9)
    go("take", 1)
    go("right", 7)
    go("take", 1)
    go("up", 7)
    go("take", 1)

    go("left", 6)
    go("up", 8)
    go("right", 6)
    go("take", 1)
    go("up", 7)
    go("take", 1)
    go("left", 7)
    go("take", 1)
    go("down", 7)

    go("left", 18)
    go("take", 1)
    go("up", 7)
    go("take", 1)
    go("right", 7)
    go("take", 1)

    # fourth level
    go("right", 7)
    go("take", 1)
    go("down", 3)
    go("right", 11)

    go("up", 3)
    go("take", 1)
    go("right", 7)
    go("take", 1)
    go("down", 7)
    go("take", 1)
    go("left", 7)
    go("take", 1)
    go("right", 3)

    go("down", 8)
    go("left", 3)
    go("take", 1)
    go("right", 7)
    go("take", 1)
    go("down", 7)
    go("take", 1)
    go("left", 7)
    go("take", 1)
    go("up", 3)
    
    go("left", 11)
    go("down", 3)
    go("take", 1)
    go("left", 7)
    go("take", 1)
    go("up", 7)
    go("take", 1)
    go("right", 7)
    go("take", 1)
    go("left", 3)
    
    go("up", 3)
    go("right", 5)
    go("down", 4)
    go("take", 1)
    go_and_take("right", 7)
    go("up", 10)
    go("take", 1)
    go_and_take("left", 9)


# Исполняем команду
def command_process(check, x, y):
    # Проверяем, что в пуле есть команды
    if len(command_list) == 0:
        return "pass"

    # Проверяем, что мы можем исполнить команду. Иногда боты мешают пройти.
    if command_list[0][0] == "right" and check("player", x + 1, y): 
        return "pass"
    if command_list[0][0] == "left" and check("player", x - 1, y): 
        return "pass"
    if command_list[0][0] == "up" and check("player", x, y - 1): 
        return "pass"
    if command_list[0][0] == "down" and check("player", x, y + 1): 
        return "pass"

    # Перед исполнением удаляем команду
    if  command_list[0][1] == 0:
        command_list.pop(0)
        if len(command_list) == 0:
            return "pass"
   
    command_list[0][1] -= 1

    return command_list[0][0] 


# Запускаемая функция
def script(check, x, y):
    setup()
    return command_process(check, x, y)