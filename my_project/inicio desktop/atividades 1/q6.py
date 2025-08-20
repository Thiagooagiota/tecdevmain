import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

label = tk.Label(root, text= "teu nome")
label.pack()
entrada = tk.Entry(root)
entrada.pack()

root.mainloop()