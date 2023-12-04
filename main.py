import tkinter
import customtkinter
from tkinter import filedialog
import re

def openFile():
    fileInput = filedialog.askopenfile()
    if fileInput:
        selected_file_label.confg(text="Selected File: {fileInput}")

   

def pdf_Run():
    readFile = re.search(r'\d{2}-\d{2}-\d{4}')


root = tkinter.Tk()
root.geometry("780x360")
root.title("PDF reader")
customtkinter.set_appearance_mode("Dark")

button = customtkinter.CTkButton(master=root, text="Open file", command=openFile)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

run_PDF = customtkinter.CTkButton(root, text="Run PDF", command=pdf_Run)
run_PDF.pack(padx=20, pady=20)

selected_file_label = tkinter.Label(root, text="Selected File")
selected_file_label.pack()

root.mainloop()