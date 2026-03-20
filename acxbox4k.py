import tkinter as tk
import math

def rounded_rect_polygon(canvas, x1, y1, x2, y2, r, steps=20, **kwargs):
    """
    Draw a rounded rectangle on the canvas by creating a polygon.
    x1, y1 : top-left corner
    x2, y2 : bottom-right corner
    r      : corner radius
    steps  : number of steps per quarter circle (higher = smoother)
    """
    points = []
    # Helper to add points along a quarter circle
    def add_arc_points(cx, cy, start_angle, end_angle):
        for i in range(steps + 1):
            angle = start_angle + (end_angle - start_angle) * i / steps
            x = cx + r * math.cos(math.radians(angle))
            y = cy + r * math.sin(math.radians(angle))
            points.append((x, y))

    # Top edge (left to right, excluding corners)
    points.append((x1 + r, y1))
    points.append((x2 - r, y1))
    # Top-right corner (angle 0 → -90, i.e. 0 to 270 in degrees)
    add_arc_points(x2 - r, y1 + r, 0, -90)
    # Right edge (top to bottom, excluding corners)
    points.append((x2, y1 + r))
    points.append((x2, y2 - r))
    # Bottom-right corner (angle -90 → -180)
    add_arc_points(x2 - r, y2 - r, -90, -180)
    # Bottom edge (right to left, excluding corners)
    points.append((x2 - r, y2))
    points.append((x1 + r, y2))
    # Bottom-left corner (angle 180 → 90)
    add_arc_points(x1 + r, y2 - r, 180, 90)
    # Left edge (bottom to top, excluding corners)
    points.append((x1, y2 - r))
    points.append((x1, y1 + r))
    # Top-left corner (angle 90 → 0)
    add_arc_points(x1 + r, y1 + r, 90, 0)

    # Flatten the list of tuples into a single list of coordinates
    flat_points = [coord for point in points for coord in point]
    return canvas.create_polygon(flat_points, smooth=True, **kwargs)

# ----------------------------------------------------------------------
# Main Tkinter window
root = tk.Tk()
root.title("Xbox Controller Drawing")
canvas = tk.Canvas(root, width=800, height=500, bg='lightgray')
canvas.pack()

# ------------------ Controller Body ------------------
# Dark gray rounded rectangle (main body)
body = rounded_rect_polygon(
    canvas, 100, 50, 700, 450, 50,
    fill='#2C2C2C', outline='black', width=2
)

# ------------------ Joysticks ------------------
# Left joystick (base + inner detail)
canvas.create_oval(210, 160, 290, 240, fill='#4A4A4A', outline='black', width=2)
canvas.create_oval(230, 180, 270, 220, fill='#2C2C2C', outline='black')
# Right joystick
canvas.create_oval(510, 160, 590, 240, fill='#4A4A4A', outline='black', width=2)
canvas.create_oval(530, 180, 570, 220, fill='#2C2C2C', outline='black')

# ------------------ D-pad (left side) ------------------
# Base circle
canvas.create_oval(170, 260, 230, 320, fill='#4A4A4A', outline='black', width=2)
# Cross shape (two rectangles)
canvas.create_rectangle(185, 270, 215, 310, fill='black', outline='black')   # vertical
canvas.create_rectangle(175, 280, 225, 300, fill='black', outline='black')   # horizontal

# ------------------ Action Buttons (right side) ------------------
# Diamond layout centered at (600, 300)
btn_r = 22
# A (bottom)
canvas.create_oval(600-btn_r, 340-btn_r, 600+btn_r, 340+btn_r, fill='green', outline='black', width=2)
canvas.create_text(600, 340, text='A', fill='white', font=('Arial', 14, 'bold'))
# B (right)
canvas.create_oval(640-btn_r, 300-btn_r, 640+btn_r, 300+btn_r, fill='red', outline='black', width=2)
canvas.create_text(640, 300, text='B', fill='white', font=('Arial', 14, 'bold'))
# X (left)
canvas.create_oval(560-btn_r, 300-btn_r, 560+btn_r, 300+btn_r, fill='blue', outline='black', width=2)
canvas.create_text(560, 300, text='X', fill='white', font=('Arial', 14, 'bold'))
# Y (top)
canvas.create_oval(600-btn_r, 260-btn_r, 600+btn_r, 260+btn_r, fill='yellow', outline='black', width=2)
canvas.create_text(600, 260, text='Y', fill='black', font=('Arial', 14, 'bold'))

# ------------------ Start & Select ------------------
# Select (left of center)
canvas.create_oval(370, 290, 394, 314, fill='#4A4A4A', outline='black', width=2)
canvas.create_text(382, 302, text='SELECT', fill='white', font=('Arial', 8))
# Start (right of center)
canvas.create_oval(406, 290, 430, 314, fill='#4A4A4A', outline='black', width=2)
canvas.create_text(418, 302, text='START', fill='white', font=('Arial', 8))

# ------------------ Xbox Logo ------------------
canvas.create_oval(375, 120, 425, 170, fill='#4A4A4A', outline='black', width=2)
canvas.create_text(400, 145, text='XBOX', fill='white', font=('Arial', 10, 'bold'))

# ------------------ Bumpers (LB / RB) ------------------
# Left bumper
canvas.create_rectangle(150, 70, 250, 90, fill='#4A4A4A', outline='black', width=2)
canvas.create_text(200, 80, text='LB', fill='white', font=('Arial', 10))
# Right bumper
canvas.create_rectangle(550, 70, 650, 90, fill='#4A4A4A', outline='black', width=2)
canvas.create_text(600, 80, text='RB', fill='white', font=('Arial', 10))

# ------------------ Minor Highlights (optional) ------------------
# Add a small reflection on the body (just for fun)
canvas.create_oval(150, 80, 300, 150, fill='', outline='', width=0)  # invisible, but you could add a highlight

root.mainloop()