import tkinter as tk
def root():
    root = tk.Tk()
    root.title("principal")
    root.geometry("400x400")

    label = tk.Label(root, text="AAAAAAAAAAAAA")
    label.pack()

    btns = tk.Button(root, text="nao clique")
    btns.pack()


a = tk.Tk()
a.state("zoomed")

btn = tk.Button(a, text="clica", command=root)
btn.pack()
a.mainloop()