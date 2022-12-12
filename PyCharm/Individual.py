#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте.
            name = input("Фамилия и инициалы студента: ")
            group = int(input("Номер группы: "))
            marks = list(map(int, input("Пять оценок студента: ").split()))

            # Вычислить средний балл из 5 оценок.
            sm = 0
            for mark in marks:
                sm += mark
            sm /= 5

            # Создать словарь.
            student = {
                'name': name,
                'group': group,
                'marks': marks,
            }

            # Добавить словарь в список, если средний балл больше 4.
            if sm > 4:
                students.append(student)

            # Отсортировать список по номеру группы.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('group', ''))

        elif command == 'list':
            if len(students) > 0:
                # Заголовок таблицы.
                line = '+-{}-+-{}-+-{}-+'.format(
                    '-' * 4,
                    '-' * 30,
                    '-' * 14,
                )
                print(line)
                print(
                    '| {:^4} | {:^30} | {:^14} |'.format(
                        "№",
                        "Ф.И.О.",
                        "Номер группы",
                    )
                )
                print(line)

                # Вывод данных о студентах с баллом выше 4.
                for idx, student in enumerate(students, 1):
                    print(
                        '| {:>4} | {:<30} | {:<14} |'.format(
                            idx,
                            student.get('name', ''),
                            student.get('group', ''),
                        )
                    )
                print(line)

            else:
                print("Студенты со средней оценкой больше 4 не найдены.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
