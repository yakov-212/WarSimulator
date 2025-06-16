import tkinter as tk
from tkinter import ttk

def draw(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2),fill="black")

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4
    
    brush_size = max(0,min(brush_size, 50))


window = tk.Tk()
window.title("Event Binding")
window.geometry("600x500")

canvas = tk.Canvas(window,bg = "white")
canvas.pack()
brush_size = 2
canvas.bind("<Motion>",draw)
canvas.bind("<MouseWheel>",brush_size_adjust)

window.mainloop()