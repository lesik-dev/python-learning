#Display the main menu
def show_menu():
   print("=" * 20)
   print("     TO-DO LIST")
   print("=" * 20)

   print("\n1. Show tasks")
   print("2. Add task")
   print("3. Delete task")
   print("4. Exit")
#Get user's menu choice
def get_choice():
   choice = input("Choose option: ")

   return choice
#Add a new task
def add_task():
   task = input("Enter your task: ")

   tasks.append(task)
#Display all tasks
def show_tasks():
   if len(tasks) == 0:
      print("No tasks yet!")
   else:
      for index,task in enumerate(tasks, start=1):
         print(index, task)

# Delete selected task
def delete_task():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        try:
         show_tasks()
         number = int(input("Which task do you want to delete?: "))
         if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted!")
         else:
            print("Please enter a valid number!")
        except ValueError:
            print("Please enter a valid number!")

      



tasks = []
while True:
   show_menu()
   choice = get_choice()

   

   if choice == "1":
      show_tasks()
   elif choice == "2":
     add_task()
   elif choice == "3":
      delete_task()
   elif choice == "4":
      print("Goodbye!")
      break
   else:
      print("Invalid option!")
      continue
