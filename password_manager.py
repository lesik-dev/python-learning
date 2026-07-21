def show_menu():
    print("=" * 20)
    print("   PASSWORD MANAGER")
    print("=" * 20)

    print("1. Show accounts")
    print("2. Add account")
    print("3. Find account")
    print("4. Delete account")
    print("5. Exit")

def get_choice():
    choice = input("Your choice: ")

    if choice in ["1", "2", "3", "4", "5"]:
        return choice
    
def add_account():
    service = input("Enter your service: ")
    login = input("Enter your login: ")
    password = input("Enter your password: ")

    with open("accounts.txt", "a") as file:
        file.write(f"{service} | {login} | {password}\n")

           


while True:
    show_menu()

    choice = get_choice()


    if choice == "1":
        print("1")
    elif choice == "2":
        add_account()
    elif choice == "3":
        print("3")
    elif choice == "4":
        print("4")
    elif choice == "5":
        print("5")
    else:
        print("Invalid choice! Please enter again.")
        continue