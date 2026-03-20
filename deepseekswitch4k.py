import tkinter as tk

def draw_nintendo_switch(canvas):
    # Dimensions and positions (centered roughly)
    width, height = 600, 400
    center_x = width // 2
    center_y = height // 2

    # Main body (tablet) - a rounded rectangle approximated by two rectangles and two circles
    body_width = 300
    body_height = 160
    body_x1 = center_x - body_width // 2
    body_y1 = center_y - body_height // 2
    body_x2 = center_x + body_width // 2
    body_y2 = center_y + body_height // 2
    corner_radius = 30

    # Draw left and right circles for rounded ends
    canvas.create_oval(body_x1, body_y1, body_x1 + corner_radius*2, body_y2, fill="#2d2d2d", outline="#1a1a1a", width=2)
    canvas.create_oval(body_x2 - corner_radius*2, body_y1, body_x2, body_y2, fill="#2d2d2d", outline="#1a1a1a", width=2)

    # Draw the middle rectangle (connects the two circles)
    canvas.create_rectangle(body_x1 + corner_radius, body_y1, body_x2 - corner_radius, body_y2,
                            fill="#2d2d2d", outline="#1a1a1a", width=2)

    # Screen (black rectangle with a slight highlight)
    screen_width = 180
    screen_height = 100
    screen_x1 = center_x - screen_width // 2
    screen_y1 = center_y - screen_height // 2
    screen_x2 = center_x + screen_width // 2
    screen_y2 = center_y + screen_height // 2
    canvas.create_rectangle(screen_x1, screen_y1, screen_x2, screen_y2,
                            fill="#111111", outline="#00aaff", width=3)
    # Screen glare (small white oval)
    canvas.create_oval(screen_x1 + 10, screen_y1 + 10, screen_x1 + 40, screen_y1 + 30,
                       fill="#ffffff", outline="", stipple="gray50")  # semi‑transparent effect

    # Left Joy‑Con (blue)
    lc_width = 50
    lc_height = 140
    lc_x1 = body_x1 - lc_width + 5  # slightly overlapping for seamless look
    lc_y1 = center_y - lc_height // 2
    lc_x2 = body_x1 + 5
    lc_y2 = center_y + lc_height // 2
    canvas.create_rectangle(lc_x1, lc_y1, lc_x2, lc_y2,
                            fill="#0066cc", outline="#003366", width=3)

    # Left joystick (circle)
    joy_l_x = lc_x1 + lc_width // 2 - 5
    joy_l_y = lc_y1 + 30
    canvas.create_oval(joy_l_x - 10, joy_l_y - 10, joy_l_x + 10, joy_l_y + 10,
                       fill="#444444", outline="#222222", width=2)
    # Joystick inner dot
    canvas.create_oval(joy_l_x - 3, joy_l_y - 3, joy_l_x + 3, joy_l_y + 3,
                       fill="#222222", outline="")

    # Directional buttons (plus‑shaped)
    # Up
    btn_up_x = joy_l_x
    btn_up_y = lc_y2 - 50
    canvas.create_rectangle(btn_up_x - 8, btn_up_y - 12, btn_up_x + 8, btn_up_y - 4,
                            fill="#aaaaaa", outline="#666666", width=1)
    # Down
    canvas.create_rectangle(btn_up_x - 8, btn_up_y + 4, btn_up_x + 8, btn_up_y + 12,
                            fill="#aaaaaa", outline="#666666", width=1)
    # Left
    canvas.create_rectangle(btn_up_x - 12, btn_up_y - 8, btn_up_x - 4, btn_up_y + 8,
                            fill="#aaaaaa", outline="#666666", width=1)
    # Right
    canvas.create_rectangle(btn_up_x + 4, btn_up_y - 8, btn_up_x + 12, btn_up_y + 8,
                            fill="#aaaaaa", outline="#666666", width=1)

    # Right Joy‑Con (red)
    rc_width = 50
    rc_height = 140
    rc_x1 = body_x2 - 5
    rc_y1 = center_y - rc_height // 2
    rc_x2 = body_x2 + rc_width - 5
    rc_y2 = center_y + rc_height // 2
    canvas.create_rectangle(rc_x1, rc_y1, rc_x2, rc_y2,
                            fill="#cc3300", outline="#662200", width=3)

    # Right joystick
    joy_r_x = rc_x2 - rc_width // 2 + 5
    joy_r_y = rc_y1 + 30
    canvas.create_oval(joy_r_x - 10, joy_r_y - 10, joy_r_x + 10, joy_r_y + 10,
                       fill="#444444", outline="#222222", width=2)
    canvas.create_oval(joy_r_x - 3, joy_r_y - 3, joy_r_x + 3, joy_r_y + 3,
                       fill="#222222", outline="")

    # Action buttons (A, B, X, Y) represented by small circles
    # We'll place them in a diamond pattern
    btn_a_x = joy_r_x
    btn_a_y = rc_y2 - 50
    offset = 12
    # A (bottom)
    canvas.create_oval(btn_a_x - 6, btn_a_y + offset - 6, btn_a_x + 6, btn_a_y + offset + 6,
                       fill="#dddddd", outline="#888888", width=1)
    # B (right)
    canvas.create_oval(btn_a_x + offset - 6, btn_a_y - 6, btn_a_x + offset + 6, btn_a_y + 6,
                       fill="#dddddd", outline="#888888", width=1)
    # X (top)
    canvas.create_oval(btn_a_x - 6, btn_a_y - offset - 6, btn_a_x + 6, btn_a_y - offset + 6,
                       fill="#dddddd", outline="#888888", width=1)
    # Y (left)
    canvas.create_oval(btn_a_x - offset - 6, btn_a_y - 6, btn_a_x - offset + 6, btn_a_y + 6,
                       fill="#dddddd", outline="#888888", width=1)

    # Home button (small circle on right Joy‑Con)
    home_x = rc_x1 + 12
    home_y = rc_y1 + 80
    canvas.create_oval(home_x - 5, home_y - 5, home_x + 5, home_y + 5,
                       fill="#222222", outline="#888888", width=1)

    # Plus and minus buttons
    # Minus on left Joy‑Con
    minus_x = lc_x2 - 15
    minus_y = lc_y1 + 80
    canvas.create_rectangle(minus_x - 8, minus_y - 3, minus_x + 8, minus_y + 3,
                            fill="#aaaaaa", outline="#666666", width=1)
    # Plus on right Joy‑Con
    plus_x = rc_x1 + 15
    plus_y = rc_y1 + 80
    canvas.create_rectangle(plus_x - 3, plus_y - 8, plus_x + 3, plus_y + 8,
                            fill="#aaaaaa", outline="#666666", width=1)
    canvas.create_rectangle(plus_x - 8, plus_y - 3, plus_x + 8, plus_y + 3,
                            fill="#aaaaaa", outline="#666666", width=1)

    # Optional: small speaker grille on the body (a few lines)
    for i in range(3):
        canvas.create_line(body_x1 + 40 + i*10, body_y2 - 20,
                           body_x1 + 60 + i*10, body_y2 - 10,
                           fill="#888888", width=2)

def main():
    root = tk.Tk()
    root.title("Nintendo Switch - Tkinter Drawing")
    root.geometry("600x400")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=600, height=400, bg="#f0f0f0", highlightthickness=0)
    canvas.pack()

    draw_nintendo_switch(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()