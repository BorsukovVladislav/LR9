#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список для всех студентов.
    students = []

    # Вывод справки.
    print("Список команд:")
    print("add - добавить студента")
    print("list - вывести список студентов")
    print("filter list - список студентов со средним баллом больше 4")
    print("exit - завершить работу с программой")

    # Бесконечный цикл запроса команд.
    while True:
        # Запрос команды из терминала.
        command = input(">>> ").lower()

        # Выполнение действия в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запрос данных о студенте.
            name = input("Фамилия и инициалы студента: ")
            group = int(input("Номер группы: "))
            marks = list(map(int, input("Пять оценок студента: ").split()))

            if len(marks) != 5:
                print("Неверное количество оценок", file=sys.stderr)
                continue

            # Создание словаря.
            student = {
                'name': name,
                'group': group,
                'marks': marks,
            }

            # Добавление словаря в список со всеми студентами.
            students.append(student)

            # Сортировка списка по номеру группы.
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

                # Вывод данных о всех студентах.
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
                print("Список студентов пустой.")

        elif command == "filter list":
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

                # Вывод данных о студентах со средним баллом больше 4.
                for idx, student in enumerate(students, 1):
                    if sum(student.get('marks')) / 5 > 4:
                        print(
                            '| {:>4} | {:<30} | {:<14} |'.format(
                                idx,
                                student.get('name', ''),
                                student.get('group', ''),
                            )
                        )
                        print(line)

            else:
                print("Список студентов пустой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
