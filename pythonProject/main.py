# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%d - %b - %Y %H:%M:%S")
print("it is ", now)
while True:
    user_action = input("Enter show, add, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todo = int(user_action[5:]) - 1

            todos = functions.get_todos()

            if todo > len(todos):
                print("This item does not exist. try again.")
                continue

            replace_text = input("Enter new todo item: ") + "\n"
            todos[todo] = replace_text

            functions.write_todos(todos)

            print("Item is replaced!")

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1

            todos = functions.get_todos()

            if len(todos) == 0:
                print("Hey, nothing in the list yet!")
                break
            else:
                print(f"{number + 1}. {todos[number].title()}")
                confirm = input("Do you want to complete this item? Y/N: ")

                if confirm.capitalize() != "N":
                    todos.pop(number)

                    functions.write_todos(todos)

                    print("Item is completed!")
        except IndexError:
            print("Item does not exist.")
            continue
        except ValueError:
            print("Complete what? enter complete followed by a number")
            continue

    elif user_action.startswith("exit"):
        print("Ok, See ya!")
        break

    else:
        print("Invalid command")
