#GenerationRawViewer.py
import os
import time
from tkinter import *
from PIL import Image, ImageTk

AddedButt=0

def LoopViewer(directory):
    loadedButton = False
    root = Tk()
    root.title("Image Viewer")
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".jpeg"):
                file_path = os.path.join(directory, filename)
                image = Image.open(file_path)
            
                photo = ImageTk.PhotoImage(image)
            
                label = Label(root, image=photo)
                label.pack()
            
                if (not loadedButton):
                    quit_button = Button(root, text="Quit", command=root.destroy)
                    quit_button.pack()
                    loadedButton = not loadedButton
            
                root.update()
                time.sleep(2)
                label.destroy()
                root.mainloop()
        root.destroy()
    except:
        return