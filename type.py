from tkinter import *
import time
from datetime import datetime

root = Tk()
def start_timer():
    global t
    t = time.time()


def end_timer():
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
    label.configure(text = str(wps) + "wps")


entry = Entry(root, width = 200)
entry.grid(row=0, column =0)

start_btn = Button(root,text = "start timer", width = 7, height = 3, command=start_timer)
start_btn.grid(row=1,column=0)


end_btn = Button(root,text = "end", width = 7, height = 3, command=end_timer)
end_btn.grid(row=2,column=0)

label = Label(root, text = "1")
label.grid(row=3, column=0)

root.mainloop()