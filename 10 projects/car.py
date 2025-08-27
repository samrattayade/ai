import tkinter as tk, random, os
from PIL import Image, ImageTk  # For better image handling

root = tk.Tk()
root.title("Car Dodging Game"); root.resizable(False, False)

W, H = 400, 500
c = tk.Canvas(root, width=W, height=H, bg="gray"); c.pack()

# Load car image (player + obstacle)
car_img = None
if os.path.exists("car.png"):
    img = Image.open("car.png").resize((40, 60))  # Resize to fit lane
    car_img = ImageTk.PhotoImage(img)
else:
    raise FileNotFoundError("car.png not found in the same folder!")

# Game variables
obstacles, speed = [], 5
score, game_over = 0, False
retry_btn = car = score_text = None

def move_left(e=None):
    if game_over: return
    x1,_,x2,_ = c.bbox(car)
    if x1 > 0: c.move(car, -20, 0)

def move_right(e=None):
    if game_over: return
    x1,_,x2,_ = c.bbox(car)
    if x2 < W: c.move(car, 20, 0)

def create_obstacle():
    if game_over: return
    x = random.choice([100, 200, 300])
    o = c.create_image(x, -30, image=car_img)  # Same image for obstacles
    obstacles.append(o)
    root.after(1500, create_obstacle)

def move_obstacles():
    global score, game_over
    if game_over: return
    for o in list(obstacles):
        c.move(o, 0, speed)
        ox1, oy1, ox2, oy2 = c.bbox(o)
        cx1, cy1, cx2, cy2 = c.bbox(car)
        if cx1 < ox2 and cx2 > ox1 and cy1 < oy2 and cy2 > oy1:
            end_game(); return
        if oy2 >= H:
            obstacles.remove(o); c.delete(o)
            score += 1; c.itemconfig(score_text, text=f"Score: {score}")
    root.after(50, move_obstacles)

def end_game():
    global game_over, retry_btn
    game_over = True
    c.create_text(W//2, H//2, text="GAME OVER", font=("Arial", 20), fill="yellow")
    retry_btn = tk.Button(root, text="Retry", font=("Arial", 14), command=reset_game)
    retry_btn.place(x=W//2 - 40, y=H//2 + 30)

def reset_game():
    global car, obstacles, score, game_over, score_text, retry_btn
    c.delete("all"); obstacles.clear(); score = 0; game_over = False
    if retry_btn: retry_btn.destroy()
    for y in range(0, H, 40): c.create_line(W//2, y, W//2, y+20, fill="white", width=3)
    car = c.create_image(W//2, H-50, image=car_img)  # Player car
    score_text = c.create_text(50, 20, text=f"Score: {score}", font=("Arial", 14), fill="white")
    create_obstacle(); move_obstacles()

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

reset_game()
root.mainloop()
