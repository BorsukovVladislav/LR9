#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    # Source Dictionary
    school = {
        '1а': 26,
        '1б': 28,
        '2а': 29,
        '2б': 23,
        '6а': 19,
        '7а': 22,
        '9а': 20,
        '10а': 18,
    }

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "change":
            while True:
                k = input("Введите номер класса: ")
                n = input("Введите количество учащихся: ")
                if k in school:
                    school[k] = n
                    break
                else:
                    print("Такого класса нет")
            print(school)

        elif command == "add":
            while True:
                k = input("Введите номер нового класса: ")
                n = input("Введите количество учащихся: ")
                if k in school:
                    print("Этот номер класса занят")
                else:
                    school[k] = n
                break
            print(school)

        elif command == "delete":
            while True:
                k = input("Введите номер расформированного класса: ")
                if k in school:
                    school.pop(k)
                    break
                else:
                    print("Такого класса нет")
            print(school)

        elif command == "count":
            s = 0
            for i in school:
                s += int(school.get(i))
            print(s)

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
