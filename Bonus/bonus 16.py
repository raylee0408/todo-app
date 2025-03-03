import FreeSimpleGUI as sq
from zip_creator import make_archive

label1 = sq.Text("Select files to compress: ")
input1 = sq.Input()
choose_button1 =sq.FilesBrowse("Choose" , key="files")

label2 = sq.Text("Select destination folder:")
input2 = sq.Input()
choose_button2 = sq.FolderBrowse("Choose", key="folder")  #if you dont have key, python will use label(Choose) as a key

compress_button = sq.Button("Compress")
output_label = sq.Text(key= "output", text_color="green")

window = sq.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button,output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")  #Generate a list of filepath
    folder = values["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="Compression completed!")


"""
Compress {0: 'C:/NZPD/PLC/QC Major & Minors  Weights 20022025.csv;C:/NZPD/PLC/QC Major & Minors Weights 10022025.csv', 
          'Choose': 'C:/NZPD/PLC/QC Major & Minors  Weights 20022025.csv;C:/NZPD/PLC/QC Major & Minors Weights 10022025.csv', 
          1: 'C:/Users/RayLee/Desktop', 
          'Choose0': 'C:/Users/RayLee/Desktop'}
"""

window.read()
window.close()