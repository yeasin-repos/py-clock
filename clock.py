import datetime
import tkinter as tk
from tkinter import ttk

def update_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    lbl_hr.config(text=hr)
    lbl_min.config(text=min)
    lbl_sec.config(text=sec)
    lbl_am.config(text=am)
    clock.after(1000, update_time)

def update_date():
    time = datetime.datetime.now()
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    lbl_date.config(text=date)
    lbl_mon.config(text=month)
    lbl_yr.config(text=year)
    lbl_day.config(text=day.title())
    clock.after(1000, update_date)

clock = tk.Tk()
clock.title('Digital Clock')
clock.geometry('1000x500')
clock.config(bg='#232D3F')

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Time New Roman', 30, 'bold'), bg='#232D3F', fg='white')
style.configure('TButton', font=('Time New Roman', 20, 'bold'), bg='#232D3F', fg='white')

frame_time = ttk.Frame(clock)
frame_time.pack(pady=50)

lbl_hr = ttk.Label(frame_time, text='00')
lbl_hr.grid(row=0, column=0, padx=(30, 0))

lbl_min = ttk.Label(frame_time, text='00')
lbl_min.grid(row=0, column=1, padx=(30, 0))

lbl_sec = ttk.Label(frame_time, text='00')
lbl_sec.grid(row=0, column=2, padx=(30, 0))

lbl_am = ttk.Label(frame_time, text='AM')
lbl_am.grid(row=0, column=3, padx=(30, 0))

ttk.Button(frame_time, text='Time', command=update_time).grid(row=1, columnspan=4, pady=(30, 0))

frame_date = ttk.Frame(clock)
frame_date.pack(pady=50)

lbl_date = ttk.Label(frame_date, text='00')
lbl_date.grid(row=0, column=0, padx=(30, 0))

lbl_mon = ttk.Label(frame_date, text='00')
lbl_mon.grid(row=0, column=1, padx=(30, 0))

lbl_yr = ttk.Label(frame_date, text='00')
lbl_yr.grid(row=0, column=2, padx=(30, 0))

lbl_day = ttk.Label(frame_date, text='Sun')
lbl_day.grid(row=0, column=3, padx=(30, 0))

ttk.Button(frame_date, text='Date', command=update_date).grid(row=1, columnspan=4, pady=(30, 0))

clock.after(1000, update_time)
clock.after(1000, update_date)

clock.mainloop()