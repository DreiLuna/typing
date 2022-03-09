from tkinter import *
import time
from datetime import datetime

root = Tk()
global is_start
is_start = 1
#!keyboard POGGERS
def key_pressed(event):
    global is_start
    print(is_start)
    if is_start == 1:

        start_timer()
    elif is_start == 2:
        end_timer()
        is_start = 0
    is_start = is_start + 1


root.bind("<KeyPress-Return>",key_pressed)

label = Label(root, text = "")
label.grid(row=3, column=0)

def start_timer():
    global t
    global start_l
    t = time.time()
    start_l = Label(root, text="START")
    start_l.grid(row=4, column=0)
    global label
    label.grid_forget()

#coder

def end_timer():
    global label
    global start_l
    global is_start
    te = time.time()
    words = entry.get()
    word_list = words.split()
    number_of_words = len(word_list)
    print(number_of_words)
    tt = te - t
    print(tt)
    mins = tt / 60
    wpm = number_of_words / mins
    wps = number_of_words / tt

    start_l.grid_forget()
    label = Label(root, text = "")
    label.grid(row=3, column=0)
    label.configure(text = str(wpm) + "wpm")



entry = Entry(root, width = 200)
entry.grid(row=0, column =0)

start_btn = Button(root,text = "start timer", width = 7, height = 3, command=start_timer)
start_btn.grid(row=1,column=0)


end_btn = Button(root,text = "end", width = 7, height = 3, command=end_timer)
end_btn.grid(row=2,column=0)



root.mainloop()