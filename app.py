import tkinter as tk
import random as rd
import logging as lg

logger = lg.getLogger()

window = tk.Tk()

window_width = 400
window_height = 300

window.geometry(str(window_width)+"x"+str(window_height))

label = tk.Label(window, text="TEST")
button = tk.Button(window, text="START", command=exit)

label.pack()
button.place(x=125, y= 200, width=150, height=50)

window.mainloop()