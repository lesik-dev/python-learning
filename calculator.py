def show_menu():
    print("\n=== Калькулятор ===")
    print("1 - Додавання")
    print("2 - Віднімання")
    print("3 - Множення")
    print("4 - Ділення")
    print("0 - Вихід")


def get_numbers():
    a = float(input("Введи перше число: "))
    b = float(input("Введи друге число: "))
    return a, b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Помилка! На нуль ділити не можна."
    return a / b


while True:
    show_menu()

    choice = input("Обери операцію: ")

    if choice == "0":
        print("До побачення!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Неправильний вибір!")
        continue

    a, b = get_numbers()

    if choice == "1":
        print("Результат:", add(a, b))
    elif choice == "2":
        print("Результат:", subtract(a, b))
    elif choice == "3":
        print("Результат:", multiply(a, b))
    elif choice == "4":
        print("Результат:", divide(a, b))