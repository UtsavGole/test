def fileRead():
    with open('App1\Day8\list2.txt', 'r')as file:
        todos = file.readlines()
    return todos


def fileWrite(todos):
    with open("App1\Day8\list2.txt", "w") as file:
        file.writelines(todos)

def addingTodos():
    todos = fileRead()
    todo = input("Enter your todo for a day: ")+'\n'
    
    todos.append(todo)
    fileWrite(todos)



def showingTodos():
    todos = fileRead()
    new_todos =[item.strip() for item in todos]
    for index, item in enumerate(new_todos):
        row = f"{index+1}-{item}"
        print(row)


def editingTodos():
    todos = fileRead()
    position = int(input("Enter the position of item: "))
    position = position-1
    new_todo = input("Enter the new todo: ")
    todos[position] = new_todo
    fileWrite(todos)


def completeTodos():
    todos = fileRead()
    comp = int(input("Enter the position of completed item: "))
    comp = comp-1
    todos.pop(comp)
    fileWrite(todos)


while True:
    user_prompt = input("Type add or show or edit or complete or quite: ")
    match user_prompt:
        case 'add':
            addingTodos()

        case 'show':
            showingTodos()

        case 'edit':
            editingTodos()

        case 'complete':
            completeTodos()

        case 'quite':
            break
print("Programme is completed")
