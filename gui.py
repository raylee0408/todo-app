import functions
import FreeSimpleGUI as sq

label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter Todo",key="todo")
add_button = sq.Button("Add")
list_box = sq.Listbox(values=functions.get_todos(),key="todos",
                      enable_events=True, size=[45,10])
edit_button = sq.Button("Edit")
complete_button = sq.Button("Complete")
exit_button = sq.Button("exit")


window = sq.Window('My To-Do App',
                   layout=[[label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica",20))

while True:
    event,values= window.read()
    print(1,event)
    print(2, values)
    print(3, values["todo"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")  #only 1 value, so use value, not values

        case "todos":  # click event "todos" when click the list and show on the top
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case sq.WIN_CLOSED:
            break

window.close()