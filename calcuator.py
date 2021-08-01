ic_path =r'C:\\Users\Асус\OneDrive\Рабочий стол\pyth_aply\icons\ic.png'
res = ''
count1 = -1
count2 = -1
act = '.'

def add_number0():
    global count1
    global count2
    res = '0'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number1():
    global count1
    global count2
    res = '1'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number2():
    global count1
    global count2
    res = '2'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number3():
    global count1
    global count2
    res = '3'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number4():
    global count1
    global count2
    res = '4'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number5():
    global count1
    global count2
    res = '5'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number6():
    global count1
    global count2
    res = '6'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number7():
    global count1
    global count2
    res = '7'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number8():
    global count1
    global count2
    res = '8'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def add_number9():
    global count1
    global count2
    res = '9'
    label['text'] = label['text'] + res
    if(act == '.'):
        count1 = int(label['text'])
    else:
        count2 = int(label['text'])

def ce():
    label['text'] = ''

def c():
    global count1
    global count2
    global act
    count1 = 0
    count2 = 0
    act = '.'
    label['text'] = ''

def delete():
    global count1
    global count2
    if act == '.':
        count1 = int(count1 / 10)
    else:
        count2 = int(count2 / 10)
    label['text'] = int(int(label['text']) / 10)

def plus():
    global act
    act = '+'
    label['text'] = ''

def minus():
    global act
    act = '-'
    label['text'] = ''

def mult():
    global act
    act = '*'
    label['text'] = ''

def dell():
    global act
    act = '/'
    label['text'] = ''

def cor():
    global count1
    res = math.sqrt(count1)
    count1 = res
    label['text'] = res

def step():
    global count1
    res = count1 * count1
    count1 = res
    label['text'] = res

def onedx():
    global count1
    res = 1 / count1
    count1 = res
    label['text'] = res

def proc():
    global count1
    global count2
    if(act == '*'):
        count2 = count2 / 100
    elif act == '+':
        count2 = count1 * (count2 / 100)
    res = count2
    label['text'] = res

def eq():
    global count1
    global count2
    global act
    if act == '+':
        res = int(count1) + int(count2)
    elif act == '-':
        res = int(count1) - int(count2)
    elif act == '*':
        res = int(count1) * int(count2)
    elif act == '/':
        res = int(count1) / int(count2)
    count1 = res
    label['text'] = res
    act = '.'

def pl_min():
    global count1
    global count2
    if(act == '.'):
        count1 = count1 * -1
        label['text'] = count1
    else:
        count2 = count2 * -1
        label['text'] = count2

def fl():
    global count2
    label['text'] = int(label['text'])
    count2 = int(count2)
    



import tkinter as tk
from tkinter.constants import *
import math

w = tk.Tk()
icon = tk.PhotoImage(file=ic_path)
w.iconphoto(False, icon)
w.config(bg='black')
w.title('калькулятор')
w.geometry('420x735+1020+180')
w.resizable(False, False)

label = tk.Label(w,
                 text=str(res),
                 bg= 'black',
                 fg= 'white',
                 font = ('Arial', 25),
                 justify= RIGHT,
                 width=22,
                 height= 3
                )
btn0= tk.Button(w, 
                text='0',                                
                command=add_number0,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn1= tk.Button(w, 
                text='1',                                
                command=add_number1,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn2= tk.Button(w, 
                text='2',                                
                command=add_number2,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn3= tk.Button(w, 
                text='3',                                
                command=add_number3,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn4= tk.Button(w, 
                text='4',                                
                command=add_number4,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn5= tk.Button(w, 
                text='5',                                
                command=add_number5,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn6= tk.Button(w, 
                text='6',                                
                command=add_number6,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn7= tk.Button(w, 
                text='7',                                
                command=add_number7,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn8= tk.Button(w, 
                text='8',                                
                command=add_number8,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn9= tk.Button(w, 
                text='9',                                
                command=add_number9,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_pl= tk.Button(w, 
                text='+',                                
                command=plus,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_min= tk.Button(w, 
                text='-',                                
                command=minus,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_mult= tk.Button(w, 
                text='*',                                
                command=mult,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_del= tk.Button(w, 
                text='/',                                
                command=dell,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_cor= tk.Button(w, 
                text='√',                                
                command=cor,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_step= tk.Button(w, 
                text='x*x',                                
                command=step,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_1dx= tk.Button(w, 
                text='1/x',                                
                command=onedx,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_proc= tk.Button(w, 
                text='%',                                
                command=proc,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_CE= tk.Button(w, 
                text='CE',                                
                command=ce,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_C= tk.Button(w, 
                text='C',                                
                command=c,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_delete= tk.Button(w, 
                text='delete',                                
                command=delete,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_eq= tk.Button(w, 
                text='=',                                
                command=eq,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_pl_min= tk.Button(w, 
                text='+/-',                                
                command=pl_min,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )
btn_fl= tk.Button(w, 
                text='.',                                
                command=fl,
                font = ('Arial', 25),
                width= 5,
                height= 2
                )

label.pack()
btn0.pack()
btn0.place(x = 105, y = 630)
btn1.pack()
btn1.place(x = 0, y = 525)
btn2.pack()
btn2.place(x = 105, y = 525)
btn3.pack()
btn3.place(x = 210, y = 525)
btn4.pack()
btn4.place(x = 0, y = 420)
btn5.pack()
btn5.place(x = 105, y = 420)
btn6.pack()
btn6.place(x = 210, y = 420)
btn7.pack()
btn7.place(x = 0, y = 315)
btn8.pack()
btn8.place(x = 105, y = 315)
btn9.pack()
btn9.place(x = 210, y = 315)
btn_pl_min.pack()
btn_pl_min.place(x = 0, y = 630)
btn_pl.pack()
btn_pl.place(x = 315, y = 525)
btn_min.pack()
btn_min.place(x = 315, y = 420)
btn_mult.pack()
btn_mult.place(x = 315, y = 315)
btn_del.pack()
btn_del.place(x = 315, y = 210)
btn_cor.pack()
btn_cor.place(x = 210, y = 210)
btn_step.pack()
btn_step.place(x = 105, y = 210)
btn_1dx.pack()
btn_1dx.place(x = 0, y = 210)
btn_proc.pack()
btn_proc.place(x = 0, y = 105)
btn_CE.pack()
btn_CE.place(x = 105, y = 105)
btn_C.pack()
btn_C.place(x = 210, y = 105)
btn_delete.pack()
btn_delete.place(x = 315, y = 105)
btn_eq.pack()
btn_eq.place(x = 315, y = 630)
btn_fl.pack()
btn_fl.place(x = 210, y = 630)
w.mainloop()