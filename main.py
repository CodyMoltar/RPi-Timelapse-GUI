import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import random
import picamera

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
app.attributes("-fullscreen", True)
app.configure(bg="#008667")

pixelVirtual = tk.PhotoImage(width=1, height=1)

camera = picamera.PiCamera()

def CameraON():
    camera.shutter_speed = int(shutterspeed_input.get())
    camera.iso = int(iso_input.get())
    camera.preview_fullscreen=False
    camera.preview_window=(47,49, 1316, 984)
    camera.resolution=(640,480)
    camera.start_preview()
    
def CameraOFF():
    camera.stop_preview()
    
def EXIT():
    app.destroy
    camera.stop_preview()
    camera.close()
    quit()

def show_photo():
    photo = Image.open("photos/" + random.choice(images))
    test = ImageTk.PhotoImage(photo.resize((GUI_image_size["width"], GUI_image_size["height"]), Image.ANTIALIAS))
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=45, y=45)
    
#####################
#
#   SET UP 2 FRAMES
#

image_frame = tk.Frame(
    app,
    width=1321,
    height=990,
    bg="white",
    bd=3
)

interface_frame = tk.Frame(
    app,
    width=464,
    height=990,
    bg="white",
    bd=3
)

image_frame.place(x=45, y=45)
interface_frame.place(x=1411, y=45)

#####################
#
#   CAMERA SETTINGS
#

camera_settings_frame = tk.Frame(
    interface_frame,
    bg="white"
)

camera_settings_frame.place(x=0, y=0, relwidth=1)


shutterspeed_label = tk.Label(
    camera_settings_frame,
    text="shutter speed (ms)",
    width=20,
    height=5,
    bg="white",
    fg=colors["ziic-green"]
)

shutterspeed_input = tk.Entry(
    camera_settings_frame
)

shutterspeed_input.insert(0, '5000')

iso_label = tk.Label(
    camera_settings_frame,
    text="ISO",
    width=20,
    height=5,
    bg="white",
    fg=colors["ziic-green"]
)

iso_input = tk.Entry(
    camera_settings_frame,
    width=20
)

iso_input.insert(0, '100')

quit_app_button = tk.Button(
    camera_settings_frame,
    text="Quit",
    width=20,
    height=3,
    bg="white",
    fg=colors["ziic-green"],
    command=EXIT
)

start_preview = tk.Button(
    camera_settings_frame,
    text="start camera preview",
    width=20,
    height=3,
    bg=colors["ziic-green"],
    fg="white",
    command=CameraON
)

shutterspeed_label.grid(row=0, column=0)
shutterspeed_input.grid(row=0, column=1)
iso_label.grid(row=1, column=0)
iso_input.grid(row=1, column=1)
start_preview.grid(row=5, column=1)
quit_app_button.grid(row=10, column=0)


app.mainloop()
