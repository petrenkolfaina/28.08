import os.path

def create():
    with open("tasks.txt", "w") as file:
        file.write("Buy a mirrow\n")
        file.write("Clean the bedroom\n")

def add_task():
    with open("tasks.txt", "a") as file:
        new_task= input("Введіть нове завдання: \n")
        file.write(new_task)

def look():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            print(file.read())
    else:
        print("Файла не існує\n")
        print("Хочете додати, натисніть-1\n")
        print("Хочете повернутися-2\n")
        choice1 = int(input("Ваш вибір: "))
        if choice1 == 1:
            create()
            add_task()
        elif choice1 == 2:
            return

def delete():
    if os.path.exists("tasks.txt"):
        os.remove("tasks.txt")
    else:
        print("Файл не існує")


while True:
    print("1-Додати нові завдання")
    print("2-Відобразити існуючий список")
    print("3-Видалити файл")
    print("4-Вихід")
    choice2 = int(input("Ваш вибір - "))
    if choice2 == 1:
        add_task()
    elif choice2 == 2:
        look()
    elif choice2 == 3:
        delete()
    elif choice2 == 4:
        break
    else:
        print("Error")