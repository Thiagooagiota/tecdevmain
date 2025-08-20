import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

label = tk.Label(root, text= "Atenção", font=("Arial", 50,), fg= '#ff0000')
label.pack()

root.mainloop()