from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro", fg=PINK)
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 0:
        count_down(5)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    # lift_window()

def lift_window():
    if reps == 1 or reps == 2 or 3 or 4 or 5 or 6 or 7 or 8:
        window.lift()


    # elif reps % 2 == 1:
    #     count_down(work_sec)
    #     reps += 1

    # elif reps == 0:
    #     count_down(5)
    #     reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer



    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        window.wm_attributes("-topmost", 1)
        window.wm_attributes("-topmost", 0)
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=500)
window.config(padx=100, pady=50, bg=YELLOW)
# window.eval('tk::PlaceWindow . center')
# window.wm_attributes("-topmost", 0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_png)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 24 ), fill="white")
canvas.grid(column=1, row=1)

# count_down(5)

# Labels
title_label = Label(text="Pomodoro", font=(FONT_NAME, 40), fg=PINK, bg=YELLOW)
title_label.grid(column=1, row=0)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

# Buttons
start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)


window.mainloop()  # constantly checking whether something happened
