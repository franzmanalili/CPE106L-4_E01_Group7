import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    root = tk.Tk()
    root.withdraw()  

  
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    
    if file_path:
        print(f"Selected file: {file_path}")
        display_file_contents(file_path)
    else:
        print("No file selected")

def display_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of the file {file_path}:\n{content}")
            show_content_in_messagebox(file_path, content)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def show_content_in_messagebox(file_path, content):
    root = tk.Tk()
    root.withdraw()  
    messagebox.showinfo(f"Content of {file_path}", content)

if __name__ == "__main__":
    select_file()