import tkinter as tk
root = tk.Tk()

def click1(event):
    x, y = event.x, event.y
    print(x, y)

root.bind('<Button-1>', click1)
root.mainloop()