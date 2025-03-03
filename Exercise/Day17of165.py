import  FreeSimpleGUI as sq


app_title= "Convertor"
def convert_To_Meter(foot, inch):
    foot_to_meter =  float(foot)* 0.3045
    inch_to_meter =  float(inch) * 0.0254
    return foot_to_meter + inch_to_meter


feet_title = sq.Text("Enter feet:")
feet_box = sq.InputText(tooltip="Enter feet", key="feet")
inches_title = sq.Text("Enter inches:")
inches_box = sq.InputText(tooltip="Enter inches", key="inches")

convert_button = sq.Button("Convert")
result_label = sq.Text(key="result")


window = sq.Window(app_title,
                   layout=[[feet_title,feet_box],
                           [inches_title,inches_box],
                           [convert_button,result_label]])

"""
1 foot = 0.3045 meter
1 inch = 0.0254
"""
while True:
    event, values = window.read()
    print(f"Event: {event}")  # Print the event
    print(f"Values: {values}")  # Print the values dictionary
    if event == "Convert":
        feet = values["feet"]
        inches = values["inches"]
        meter_value = convert_To_Meter(feet,inches)
        window["result"].update(f"{meter_value} m")
    if event == sq.WIN_CLOSED:
        break

window.close()