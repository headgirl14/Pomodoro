from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 15
reps = 0
checkbox = ""
stop_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def start_again():
    window.after_cancel(stop_timer)
    checkbox = None
    timer = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
    timer.grid(column=2, row=1)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    reps += 1
    if reps %2 !=0:
        count_down(work_sec)
        timer.config(text="Work",fg=PINK)
    elif reps %2 ==0:
        count_down(short_break)
        timer.config(text="Break", fg=RED)
    elif reps % 8 ==0:
        count_down(long_break)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def create_checkbox():
    global checkbox
    checkbox += "🗸"
    check = Label(text =checkbox, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 26, "bold"))
    check.grid(column=2, row=4)

def count_down(count):
    global stop_timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        stop_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps %2 ==0:
            create_checkbox()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#timer wigit
timer = Label(text="Timer", font=(FONT_NAME, 32,"bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

#start and reset buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=1, row=3)

reset = Button(text="Reset", highlightthickness=0, command=start_again)
reset.grid(column=3, row=3)

window.mainloop()
