import os
import keyboard as key

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rooms = []

def input_cmd():
    os.system('cls')
    try: 
        cmd = int(input(
            'Приветствую!\n'\
            'Введите номер команды которую необходимо выполнить:\n'\
            '1. Добавить клиента    2. Посмотреть список клиентов   3. Посмотреть данные о клиенте\n'\
            '4. Удалить клиента     5. Изменить данные о клиенте    6. Построить диаграмму\n'\
            ''
            '                       0. Выход из программы\n'\
        ))
        return cmd 
    except ValueError:
        print('Вы ввели не число')

def set_client():
    os.system('cls')
    try:
        fio = input(
            'Чтобы подселиться в отель, нужно ввести некоторые данные.\n'\
            'Введите ФИО клиента. '
        )

        number_room = int(input(
            'Отлично.\n'\
            'Давайте теперь мы введем номер комнаты. '
        ))

        amount_days = int(input(
            'На сколько дней подселить клиента? '
        ))

        price_room_day = int(input(
            'Какая цена за сутки? '
        ))

        for_payment = amount_days*price_room_day

        if number_room <= 3 and number_room >= 1:
            if number_room in rooms:
                print('В данной комнате уже живут!')
                print('Нажмите на enter для продолжения...')
                key.wait('enter')
                return
            else:
                rooms.append(number_room)
        else:
            print('У нас нет такого количества комнат!')
            print('Нажмите на enter для продолжения...')
            key.wait('enter')
            return

        print(
            '-----------------------\n'\
            'Отлично!\n'\
            f'Клиент подселён в комнату №{number_room}\n\n'\
            '-----------------------'
        )

        try:
            file = open(f'clients/room{number_room}.txt', 'w+')
            file.write(
                '-----------------------\n'\
                f'ФИО: {fio}\n'\
                f'№ комнаты: {number_room}\n'\
                f'Количество дней: {amount_days}\n'\
                f'Цена за сутки: {price_room_day}\n'\
                f'Итого к оплате: {for_payment}\n'\
                '-----------------------'
            )
        finally:
            file.close()

        print('Нажмите на enter для продолжения...')
        key.wait('enter')

    except FileNotFoundError:
        print('Странно... Что-то пошло не так')

    except ValueError:
        print(
            'Вы ввели не число!\n'\
            'Придётся заполнять ещё раз'
        )
        print('Нажмите на enter для продолжения...')
        key.wait('enter')
    
def get_clients():
    os.system('cls')
    for i in range (len(os.listdir('clients/'))):
        file = open(f'clients/room{i+1}.txt', 'r')
        print(file.read())
        file.close()
    key.wait('enter')

def get_client():
    os.system('cls')
    try:
        num_room = int(input(
            'Введите номер комнаты о которой вы хотите узнать: '
        ))
        if num_room > 3 or num_room < 1:
            print('Такой комнаты не существует!')
            key.wait('enter')
            return
        else:
            try:
                file = open(f'clients/room{num_room}.txt', 'r')
                print(file.read())
            finally:
                file.close()
    except Exception:
        print('В этой комнате никто не живет!')
    except ValueError:
        print('Было введено не число!')
    key.wait('enter')

def remove_client():
    os.system('cls')
    try:
        num_room = int(input(
            'Введите номер комнаты из которой нужно удалить данные: '
        ))
        if num_room > 3 or num_room < 1:
            print('Такой комнаты не существует!')
            key.wait('enter')
            return
        else:
            os.remove(f'clients/room{num_room}.txt')
            rooms.remove(num_room)
            print('Успешное удаление из базы!')
            key.wait('enter')

    except FileNotFoundError:
        print('В этой комнате и так никто не живет!')
        key.wait('enter')

def edit_client():
    os.system('cls')
    try:
        num_room = int(input(
            'Введите номер комнаты из которой нужно изменить данные: '
        ))
        if num_room > 3 or num_room < 1:
            print('Такой комнаты не существует!')
            key.wait('enter')
            return
        else:
            try:
                file = open(f'clients/room{num_room}.txt', 'w+')
                fio = input(
                'Введите ФИО клиента. '
                )
                amount_days = int(input(
                'На сколько дней подселить клиента? '
                ))

                price_room_day = int(input(
                    'Какая цена за сутки? '
                ))

                for_payment = amount_days*price_room_day

                file.write(
                '-----------------------\n'\
                f'ФИО: {fio}\n'\
                f'№ комнаты: {num_room}\n'\
                f'Количество дней: {amount_days}\n'\
                f'Цена за сутки: {price_room_day}\n'\
                f'Итого к оплате: {for_payment}\n'\
                '-----------------------'
                )
                print('Готово!')
                key.wait('enter')
            finally:
                file.close()
    except ValueError:
        print('Вы ввели не число!')
        key.wait('enter')
    except FileNotFoundError:
        print('В этой комнате никто не живет!')
        key.wait('enter')


def get_for_payment():
    for_payment = []
    fio = []
    for i in rooms:
        file = open(f'clients/room{i}.txt', 'r')
        text = file.readlines()
        for_payment.append(int(text[5].split(': ')[1]))
        fio.append(text[1].split(': ')[1])
        file.close()
    return for_payment, fio

def to_build_diagram():
    for_payment = get_for_payment()[0]
    fio = get_for_payment()[1]
    plt.bar(fio, for_payment, hatch ='x', color='green')
    plt.show()