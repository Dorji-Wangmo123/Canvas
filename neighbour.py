import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Colorful House")
window.geometry("600x500")

# Create canvas
canvas = tk.Canvas(window, width=600, height=500, bg="skyblue")
canvas.pack()

# -------------------------
# GRASS
# -------------------------
canvas.create_rectangle(
    0, 400, 600, 500,
    fill="green",
    outline="green"
)

# -------------------------
# HOUSE BASE
# -------------------------
canvas.create_rectangle(
    150, 220, 450, 400,
    fill="lightpink",
    outline="black",
    width=3
)

# -------------------------
# ROOF
# -------------------------
canvas.create_polygon(
    120, 220,
    300, 100,
    480, 220,
    fill="red",
    outline="darkred",
    width=4
)

# -------------------------
# LEFT WINDOW
# -------------------------
canvas.create_rectangle(
    185, 260, 250, 325,
    fill="lightblue",
    outline="blue",
    width=3
)

# Window cross
canvas.create_line(
    217, 260, 217, 325,
    fill="blue",
    width=2
)

canvas.create_line(
    185, 292, 250, 292,
    fill="blue",
    width=2
)

# -------------------------
# RIGHT WINDOW
# -------------------------
canvas.create_rectangle(
    350, 260, 415, 325,
    fill="lightgreen",
    outline="darkgreen",
    width=3
)

# Window cross
canvas.create_line(
    382, 260, 382, 325,
    fill="darkgreen",
    width=2
)

canvas.create_line(
    350, 292, 415, 292,
    fill="darkgreen",
    width=2
)

# -------------------------
# DOOR
# -------------------------
canvas.create_rectangle(
    270, 315, 330, 400,
    fill="brown",
    outline="black",
    width=3
)

# Door handle
canvas.create_oval(
    315, 355, 323, 363,
    fill="yellow",
    outline="black"
)

# -------------------------
# CHIMNEY
# -------------------------
canvas.create_rectangle(
    375, 135, 410, 200,
    fill="gray",
    outline="black",
    width=3
)

# Run the program
window.mainloop()