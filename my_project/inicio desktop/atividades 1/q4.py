import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

btn = tk.Button(root, text="clique aqui")
btn.pack(pady=20)
btn2 = tk.Button(root, text="clique aqui")
btn2.pack(pady=20)
btn3 = tk.Button(root, text="clique aqui")
btn3.pack(pady=20)

root.mainloop()