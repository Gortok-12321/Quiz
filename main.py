import os


# функция которая пишет консольные команды
os.system("color 2")

point = 0

print("Welcome to Quiz")
print("как зовут ведущего программы поле чудес?")
print("1) Леонид Якубович",
      "2) Андрей Малахов",
      "3) Александр Петров",
      "4) Дмитрий Комаров")
user_input = input("Введи ответ: \n")
os.system("cls")

if user_input == "1":
    # правильный ответ
    print("верно")
    point = point + 1
    print("ваше количество баллов", point)

else:
    # неправильный ответ
    print("позор такое не знать")
    if point > 0:
        point = point - 1

    print("ваше количество балов ", point)

print("Под каким прозвищем известен Олег Абрамов?")
print("1)горшок",
      "2)Йоаким",
      "3)радио тапок")
user_input = input("Введи ответ: \n")
os.system("cls")
if user_input == "3":
    print("верно")
    point = point + 1
    print("ваше количество балов", point)
else:
    print("не верно")
    if point > 0:
        point = point - 1
    print("ваше количество балов", point)

print("На какую песню Олега Абрамова сделала кавер группа Сабатон?")
print("1)битва за москву",
      "2)смута",
      "3)цусима")
user_input = input("Введи ответ: \n")
os.system("cls")
if user_input == "1":
    print("верно")
    point = point + 1
    print("ваше количество балов", point)
else:
    print("не верно")
    if point > 0:
        point = point - 1
    print("ваше количество балов", point)

print("сколько лет Владимиру Владимировичу Путину?")
print("1) 35",
    "2) явно старше Иисуcа",
    "3) 61")
user_input = input("Введи ответ: \n")
os.system("cls")

if user_input == "2":
    print("а ты шаришь")
    point = point + 1
    print("ваше количество балов", point)
else:
    print("не верно")
    if point > 0:
        point = point - 1
    print("ваше количество балов", point)
# остановить программу
input("для выхода нажмите ENTER")
