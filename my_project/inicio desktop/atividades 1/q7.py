import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

btn = tk.Button(root, text="somar")
btn.pack(pady=20)
btn2 = tk.Button(root, text="subtrair")
btn2.pack(pady=20)


root.mainloop()