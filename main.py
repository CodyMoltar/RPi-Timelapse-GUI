import tkinter as tk
from PIL import Image, ImageTk
import random

GUI_image_size = {
    "width": 1320,
    "height": 990
}

images = ["1.jpg", "2.jpg", "3.jpg"]

colors = {
    "ziic-green": "#008667"
}

app = tk.Tk()

app.geometry("1920x1080")
app.configure(bg="#008667")


def show_photo():
    photo = Image.open("photos/" + random.choice(images))
    test = ImageTk.PhotoImage(photo.resize((GUI_image_size["width"], GUI_image_size["height"]), Image.ANTIALIAS))
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=45, y=45)

quit_app_button = tk.Button(
    text="Quit",
    width=25,
    height=5,
    bg=colors["ziic-green"],
    fg="white",
    command=app.destroy
)

update_photo_button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg=colors["ziic-green"],
    fg="white",
    command=show_photo
)

quit_app_button.place(x=1440, y=45)
update_photo_button.place(x=1440, y=110)



app.mainloop()

