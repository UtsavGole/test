while True:
    user_prompt = input("Type add or show or edit or complete or quite: ")
    match user_prompt:
        case 'add':
            todo = input("Enter your todo for a day: ")+'\n'
            with open("App1/Day8/list.txt", "r") as file:
                todos = file.readlines()
            todos.append(todo)
            with open("App1/Day8/list.txt", "w") as file:
                file.writelines(todos)

        case 'show':
            with open("App1/Day8/list.txt", "r") as file:
                todos = file.readlines()
            new_todos = [item.strip() for item in todos]

            for index, item in enumerate(new_todos):
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            with open("App1/Day8/list.txt", "r") as file:
                todos = file.readlines()
            position = int(
                input("Enter the position of item you want to edit: "))
            position = position+1
            new_item = input("Enter the new item: ")
            todos[position] = new_item
            with open("App1/Day8/list.txt", "w") as file:
                file.writelines(todos)

        case 'complete':
            with open("App1/Day8/list.txt", "r") as file:
                todos = file.readlines()
            comp = int(input("Enter the position of item which is completed: "))
            todos.pop(comp-1)
            with open("App1/Day8/list.txt", "w") as file:
                file.writelines(todos)

        case 'quite':
            break
        case _:
            print("Wrong command!!!")
print("Programme is completed")
