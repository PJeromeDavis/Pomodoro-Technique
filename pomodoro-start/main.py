from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")
    checkpoint_label.config(text="")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    long_break = LONG_BREAK_MIN*60
    short_break = SHORT_BREAK_MIN*60


    if reps == 8:
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW)
        count_down(long_break)

    elif reps%2==0 and reps!=8:
        timer_label.config(text="Short Break", fg=GREEN, bg= YELLOW)
        count_down(short_break)

    else:
        timer_label.config(text="Timer", fg=GREEN, bg=YELLOW)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count/60)
    seconds = count%60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count>=0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += CHECKMARK
        checkpoint_label.config(text=mark)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW, highlightthickness=0)

canvas =Canvas(width=200,height=224, bg=YELLOW,highlightthickness=0)
image_png = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=image_png)
timer_text = canvas.create_text(102,125,text="00.00",fill="white", font=(FONT_NAME, 25,"bold"))
canvas.grid(column=1,row=1)






timer_label = Label(text= "Timer", font=(FONT_NAME, 30,"bold"), fg=GREEN ,bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset", command=reset_timer)
reset_button.grid(column=2,row=2)

checkpoint_label=Label(font=(FONT_NAME, 15,"bold"), fg=GREEN)
checkpoint_label.grid(column=1,row=2)


window.mainloop()