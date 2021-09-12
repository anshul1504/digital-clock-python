from tkinter import *
import time
t=Tk()
w=380
h=80
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))
t.resizable(0,0)
t.title("Digital Clock")
t.configure(bg="light blue")

def times():
    current_time=time.strftime("%I:%M:%S:%p")
    clock_lb1 = Label(bg="black",fg="red",text=current_time,font=("",50))
    clock_lb1.after(200,times)
    clock_lb1.grid(row=0,column=1)
    
times()

t.mainloop()    