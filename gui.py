import functions
import FreeSimpleGUI as sq

label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter Todo")
add_button = sq.Button("Add")
exit_button = sq.Button("exit")
window = sq.Window('My To-Do App', layout=[[label],[input_box,add_button],[exit_button]])

window.read()
window.close()