from tkinter import *
import math

Pink = "#e2979c"
Red = "#e7305b"
Green = "#9bdeac"
Yellow = '#f7f5dd'
Font = "Courier"
work_min = 25
short_break = 5
long_break = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1

    work_sec = work_min * 60
    short_break_sec = short_break * 60
    long_break_sec = long_break * 60

    if reps % 8 ==0:
        count_down(long_break_sec)
        title.config(text="Break", fg=Red)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=Pink)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=Green)

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

window =Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=Yellow)

title = Label(text="Timer", fg=Green, font=(Font, 50))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=Yellow, highlightthickness=0)
tomato_img = PhotoImage(file="vector-graphics-tomato-soup-tomato-juice-pizza-png-favpng-fDy6tFn8JhpvLdPmjhdTAcmZH.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(Font, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_marks= Label(fg=Green, bg=Yellow)
check_marks.grid(column=1, row=3)

window.mainloop()
