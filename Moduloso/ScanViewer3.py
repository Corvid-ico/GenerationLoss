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

    def update_image():
        file_path = entry.get()
        if file_path:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            label.configure(image=photo)
            label.image = photo

    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.pack()

    entry = Entry(root)
    entry.pack()

    update_button = Button(root, text="Update", command=update_image)
    update_button.pack()

    quit_button = Button(root, text="Quit", command=root.destroy)
    quit_button.pack()

    root.mainloop()
