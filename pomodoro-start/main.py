#import all class from the module 
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  """
  reset all the parameters 
  """
  window.after_cancel(timer)
  canvas.itemconfig(timer_text="00:00")
  timer_label.config(text="Timer")
  check_label.config(text="")
  global reps
  reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  if reps % 2 != 0:
    #call the count down fonction
    count_down(work_sec)
    #change the label text for user to see what cycle he is in 
    timer_label.config(text="Working Time", fg=GREEN)
    #add one rep 
    reps += 1
  elif reps == 8:
    timer_label.config(text="Break", fg=RED)
    count_down(long_break_sec)
    reps += 1
  elif reps % 2 == 0:
    timer_label.config(text="Break", fg=PINK)
    count_down(short_break_sec)
    reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

  #get the minutes remaining
  count_min = math.floor(count / 60)

  #get the seconde remaining and make the affichage with 2 digits
  count_secondes = count % 60
  if count_secondes == 0:
    count_secondes = "00"
  elif count_secondes < 10:
    count_secondes = f"0{count_secondes}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_secondes}")

  #first arg = time in milisecond, function to call after 1000ms, *args
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    #add a mark every 2 sessions     
    marks = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      marks = "✓"
    check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

#create a window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


#put an image as background width and height as pixel 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#add the image into a variable to use it with canvas
tomato_img = PhotoImage(file="./pomodoro-start/tomato.png")

#put the image at center so 100 and 112 
canvas.create_image(100, 112, image=tomato_img)

#create text for the countdown
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 50))
#make apparing the canva
canvas.grid(column=1, row=1)

#create a label for the timer 
timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)


#create the start button, use commande to start timer
start_button = Button(text="Start", fg=RED, bg="white", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)



#create the reset button
reset_button = Button(text="Reset", fg=RED, bg="white", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=2)

#checkbox 
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)






#let the window open 
window.mainloop()