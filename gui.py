import tkinter as tk

def attack_gui(moveset: list):
    moveset += [''] * (4 - len(moveset))
    root = tk.Tk()
    def first_move():
        global val
        val = 0
        root.destroy()

    def second_move():
        global val
        val = 1
        root.destroy()

    def third_move():
        global val
        val = 2
        root.destroy()

    def fourth_move():
        global val
        val = 3
        root.destroy()
        
    frame = tk.Frame(root)
    frame.pack()

    attack = tk.Button(frame,
                    text=moveset[0],
                    width=25,
                    height=3,
                    command=first_move)
    attack.pack()
    change = tk.Button(frame,
                    text=moveset[1],
                    width=25,
                    height=3,
                    command=second_move)
    change.pack()
    items = tk.Button(frame,
                    text=moveset[2],
                    width=25,
                    height=3,
                    command=third_move)
    items.pack()

    run = tk.Button(frame,
                    text=moveset[3],
                    width=25,
                    height=3,
                    command=fourth_move)
    run.pack()
    root.mainloop()
    return val