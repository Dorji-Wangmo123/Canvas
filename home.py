import tkinter as tk
root = tk.Tk()
root.title("My house")

canvas = tk.Canvas(root, width=600, height=450, bg="skyblue")
canvas.pack()

canvas.create_rectangle(150,200,450,400, fill="lightyellow")
canvas.create_polygon(120,200,300,80,480,200, fill="brown")
canvas.create_rectangle(190,240,260,310, fill="lightblue")
canvas.create_rectangle(340,240,410,310, fill="lightblue")
canvas.create_rectangle(270,310,330,400, fill="brown")

root.mainloop()