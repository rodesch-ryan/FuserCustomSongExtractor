'''
Author: Artyom-V2X
Version: 2
License: Open-Source
'''

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import zipfile
os.environ['PATH'] += os.pathsep + r"C:\Program Files\WinRAR"

def extract_archive(archive_path, output_directory):
    global label_text
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # Extract the main archive
    try:
        if zipfile.is_zipfile(archive_path):
            with zipfile.ZipFile(archive_path, 'r') as zipped:
                zipped.extractall(output_directory)
        else:
            os.system(f"rar x -r -y \"{archive_path}\" \"{output_directory}\"")
        label_text = f"Archives successfully extracted!"
        success_label.config(text=label_text)
    except:
        label_text = "Unsupported archive format or file is not an archive."
        success_label.config(text=label_text)

def extractToCustoms(dir):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    extract_archive(dir, application_path+r"\Fuser\Content\Paks\custom_songs")
    try:
        os.remove(application_path+r"\Fuser\Content\Paks\customSongsUnlocked_P.pak")
        os.remove(application_path+r"\Fuser\Content\Paks\customSongsUnlocked_P.sig")
    except:
        pass

def upload_action(event=None):
    global label_text
    filenames = filedialog.askopenfilenames(filetypes=[("Archives", "*.*")])
    for filename in filenames:
        try:
            extractToCustoms(filename)
        except Exception as e:
           messagebox.showinfo("Error", f"General error with {filename}, see verbose output in CMD")
           print(e)
    success_label.config(text=label_text)

# Create the root window
root = tk.Tk()
root.title('Arty\'s Custom Song Loader')
root.geometry("400x100")

# Create a button that will call the upload_action function when clicked
upload_btn = tk.Button(root, text='Upload Files', command=upload_action)
upload_btn.pack(padx=10,pady=10,expand=True)
label_text = "Input Pack Archives"
success_label = tk.Label(text=label_text)
success_label.pack(padx=10,pady=10)

# Start the Tkinter event loop
root.mainloop()
