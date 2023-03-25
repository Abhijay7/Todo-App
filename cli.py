import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_act = input("Type add, show, edit, complete or exit: ")

    if user_act.startswith("add"):
        todo = user_act[4:]
            
        todos = functions.get_todos()
        todos.append(todo + '\n')
            
        functions.write_todos(todos)

    elif user_act.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    
    elif user_act.startswith("edit"):
        try:
            number = int(user_act[5:])
            number -= 1
            
            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            print("Here is how it will be", todos)
        
            functions.write_todos(todos) 
   
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_act.startswith("complete"):
        try:

            number = int(user_act[9:])
            
            todos = functions.get_todos()

            index = number - 1
            todo_to_rem = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"todo: {todo_to_rem} was removed from the list."
            print(message)

        except IndexError:
            print("No item with that number.")
            continue

    elif user_act.startswith("exit"):
        break

    else:
        print("Invalid command!!!")
    
print("bye")
