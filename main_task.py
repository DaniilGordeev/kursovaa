import equation
import integral
import os

def input_cmd():
    os.system('cls')
    try: 
        cmd = int(input(
            'Приветствую!\n'\
            'Введите номер команды которую необходимо выполнить:\n'\
            '1. Рассчитать интеграл    2. Решить уравнение \n'  \
            '         0. Выход из программы\n'\
        ))
        return cmd 
    except ValueError:
        print('Вы ввели не число')


while True:
    cmd = input_cmd() 
    if cmd == 0:
        exit()
    elif cmd == 1:
        integral.main()
    elif cmd == 2:
        equation.main()
    else:
        print('Такой команды не существует!')