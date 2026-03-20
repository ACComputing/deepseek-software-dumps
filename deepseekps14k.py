import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("PlayStation 1 Console (Outside View)")
root.geometry("600x300")
root.resizable(False, False)
root.configure(bg="gray20")

# Create a canvas to draw the console
canvas = tk.Canvas(root, width=600, height=300, bg="gray20", highlightthickness=0)
canvas.pack()

# Main body of the console (a rounded rectangle)
# Coordinates: x1, y1, x2, y2, radius=20
body = canvas.create_rectangle(50, 50, 550, 250, fill="#4a4a4a", outline="#2a2a2a", width=3)

# Add a subtle gradient effect by drawing a highlight line
canvas.create_line(55, 55, 545, 55, fill="#7a7a7a", width=2)

# Disc tray area (left side) - a light gray rectangle with a circular indentation
tray = canvas.create_rectangle(80, 80, 280, 200, fill="#3a3a3a", outline="#1a1a1a", width=2)

# CD disc representation (circle)
cd = canvas.create_oval(120, 100, 240, 180, fill="#2a2a2a", outline="#cccccc", width=2)

# Inner circle of the CD
cd_hole = canvas.create_oval(165, 145, 195, 175, fill="#1a1a1a", outline="#aaaaaa", width=1)

# "PlayStation" logo on the disc tray (using text)
logo = canvas.create_text(180, 220, text="PlayStation", fill="#c0c0c0", font=("Arial", 14, "bold"))

# Power button (right side)
power_btn = canvas.create_rectangle(420, 120, 460, 150, fill="#2a2a2a", outline="#888888", width=2)
power_text = canvas.create_text(440, 135, text="POWER", fill="white", font=("Arial", 8, "bold"))

# Reset button (below power)
reset_btn = canvas.create_rectangle(420, 160, 460, 190, fill="#2a2a2a", outline="#888888", width=2)
reset_text = canvas.create_text(440, 175, text="RESET", fill="white", font=("Arial", 8, "bold"))

# Open button (optional, sometimes on original)
open_btn = canvas.create_rectangle(420, 200, 460, 230, fill="#2a2a2a", outline="#888888", width=2)
open_text = canvas.create_text(440, 215, text="OPEN", fill="white", font=("Arial", 8, "bold"))

# Controller ports (bottom front) - two small rectangles
port1 = canvas.create_rectangle(320, 220, 360, 240, fill="#1a1a1a", outline="#888888", width=1)
port2 = canvas.create_rectangle(370, 220, 410, 240, fill="#1a1a1a", outline="#888888", width=1)

# Port labels
canvas.create_text(340, 250, text="1", fill="white", font=("Arial", 8))
canvas.create_text(390, 250, text="2", fill="white", font=("Arial", 8))

# Memory card slots (just small dots)
canvas.create_oval(335, 228, 340, 233, fill="red", outline="")
canvas.create_oval(385, 228, 390, 233, fill="red", outline="")

# Some extra details: screw heads or vents
canvas.create_oval(70, 130, 80, 140, fill="#2a2a2a", outline="#888888")
canvas.create_oval(520, 130, 530, 140, fill="#2a2a2a", outline="#888888")

# Start the tkinter main loop
root.mainloop()