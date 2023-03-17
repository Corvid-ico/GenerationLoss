#GenerationRawViewer.py
import os
from tkinter import *
from PIL import Image, ImageTk

def LoopViewer(directory):
	for filename in os.listdir(directory):
		if filename.endswith('.jpeg'):
			file_path = os.path.join(directory, filename)
			view_image(file_path, filename)

def view_image(file_path, filename):
    root = Tk()
    root.title(f"Image Generation: {filename}")

    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.pack()

    quit_button = Button(root, text="Quit", command=root.destroy)

    quit_button.pack()
    
    root.mainloop()