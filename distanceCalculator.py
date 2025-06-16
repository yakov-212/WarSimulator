import tkinter as tk
import ttkbootstrap as ttk
window = ttk.Window()
window.geometry("800x500")
window.title('distanceCalculator')
def convert():
    mile_input = entry_int.get()
    km_output = round(mile_input *1.61,2)
    output_string.set(km_output)
def unrounded_convert():
    mile_input = entry_int.get()
    km_output = mile_input *1.61
    output_string.set(km_output)

input_frame = ttk.Frame(window)
entry_int = ttk.IntVar()
entry = ttk.Entry(input_frame,textvariable=entry_int)
button = ttk.Button(input_frame,text="convert round",command= convert)
button2 = ttk.Button(input_frame,text="convert unrounded",command= unrounded_convert)

output_string = ttk.StringVar()
output_label = ttk.Label(window,text="output",textvariable=output_string)
not_round_output = ttk.Label(window,textvariable=output_string)


entry.pack(side="left",padx=10)
button.pack(side="left",padx=10)
button2.pack(side="left",padx=10)
input_frame.pack(pady=20)
output_label.pack()
window.mainloop()
