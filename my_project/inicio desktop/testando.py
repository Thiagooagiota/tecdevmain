import tkinter as tk

root = tk.Tk()
root.state("zoomed")

btn1 = tk.Button(root, text="Opção 1")
btn1.place(relx=0.3, rely=0.9, anchor="center")  # 90% da altura da tela

btn2 = tk.Button(root, text="Opção 2")
btn2.place(relx=0.5, rely=0.9, anchor="center")

btn3 = tk.Button(root, text="Sair", command=root.quit)
btn3.place(relx=0.7, rely=0.9, anchor="center")

root.mainloop()