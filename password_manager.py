#Display the main menu
def show_menu():
    print("=" * 20)
    print("   PASSWORD MANAGER")
    print("=" * 20)

    print("1. Show accounts")
    print("2. Add account")
    print("3. Find account")
    print("4. Delete account")
    print("5. Exit")

#Get user's menu choice
def get_choice():
    choice = input("Your choice: ")

    if choice in ["1", "2", "3", "4", "5"]:
        return choice
    
#Add a new account
def add_account():
    service = input("Enter your service: ")
    login = input("Enter your login: ")
    password = input("Enter your password: ")

    with open("accounts.txt", "a") as file:
        file.write(f"{service} | {login} | {password}\n")

#Display all saved accounts
def show_accounts():
    with open("accounts.txt", "r") as file:
        content = file.read()

        

        if not content:
            print("No accounts yet!")
        else:
            print(content)
        

#Search for an account by service name
def find_account():
    service = input("Enter service to find: ")

    with open("accounts.txt", "r") as file:
        found = False
        for line in file:
            if service in line:
                print(line)
                found = True
        
        if not found:
            print("Account not found!")
#Delete an account by service name
def delete_account():
    service = input("Select the account you want to delete: ")
    new_lines = []
    with open("accounts.txt", "r") as file:
        account = file.readlines()
        

        found = False
        for line in account:
            if service in line:
                found = True
            else:
                new_lines.append(line)

        if found:
            print("Account deleted!")

            with open("accounts.txt", "w") as file:
                file.writelines(new_lines)
        else:
            print("Account not found!")

           

#Main program loop
while True:
    show_menu()

    choice = get_choice()


    if choice == "1":
        show_accounts()
    elif choice == "2":
        add_account()
    elif choice == "3":
        find_account()
    elif choice == "4":
        delete_account()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter again.")
        continue
