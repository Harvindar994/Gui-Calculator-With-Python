from tkinter import *

root = Tk()
root.config(bg='#2b2b2b')
root.geometry("475x288")
root.title('Calculator')

Output_screen_value = StringVar()
Output_screen_value.set("")
Last_value = ''
Last_number = ''
def last_value_is_float(value):
    value = ''
    if value.isnumeric():
        return False
    lenth = len(value)-1
    text = ''
    if lenth>0:
        while (value[lenth]>='0' and value[lenth]<='9' or value[lenth]=='.') and lenth!=0:
            text += value[lenth]
            lenth -= 1
        if '.' in text:
            return True
        else:
            return False
def resolve_event(event):
    global Last_value
    global Last_number
    global Output_screen_value
    global Output_screen
    text = event.widget.cget('text')
    if text=='C':
        Last_value = ''
        Last_number = ''
        Output_screen_value.set("")
    elif text=='=':
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        ope = ['-','+','*','/']
        value = Output_screen_value.get()
        if value[len(value)-1] in ope:
            return

        for e in num:
            if e in value:
                break
        else:
            return

        result = eval(Output_screen_value.get())
        Output_screen_value.set(result)

    elif text=='Backspace':
        if len(Output_screen_value.get())!=0:
            value = Output_screen_value.get()
            value = value[0:len(value)-1]
            Output_screen_value.set(value)
    else:
        print(last_value_is_float(Output_screen_value.get()))
        if text>='0' and text<='9':
            Last_number += text
            Output_screen_value.set(Output_screen_value.get()+text)
        elif Last_value!='+' and Last_value!='-' and Last_value!='*' and Last_value!='/' and Last_value!='.':
            if text=='.':
                if '.' in Last_number:
                    return
                else:
                    Last_number += text
                    Output_screen_value.set(Output_screen_value.get() + text)
            else:
                Last_number = ''
                Output_screen_value.set(Output_screen_value.get() + text)
    Last_value = text

#-------------------------- Main Screen Creation ------------------------------
Output_screen = Entry(root, bg='#2b2b2b', disabledbackground='#2b2b2b', foreground='white', textvar=Output_screen_value, justify=RIGHT)
Output_screen.config(font=('calibari', 12), state=DISABLED)
Output_screen.config(highlightbackground='gray33', highlightthickness=1)
Output_screen.place(x=4, y=4, width=467, height=80)
Date_cal_frame = Frame(root, bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Date_cal_frame.place(x=171, y=87, width = 300, height=197)
Date_label = Label(Date_cal_frame, bg='#3c3f41', text='Date Calculation', fg='#BBBBBB')
Date_label.pack(fill=X)

#-------------------------- Date Calculation Graphic ------------------------------
Date_from_label = Label(Date_cal_frame, text='From', fg='#BBBBBB', bg='#2b2b2b')
Date_to_label = Label(Date_cal_frame, text='To', fg='#BBBBBB', bg='#2b2b2b')
Date_from = Entry(Date_cal_frame, fg='white', bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Date_to = Entry(Date_cal_frame, fg='white', bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Date_result_label = Label(Date_cal_frame, text='Difference (year, months, weeks, days)', fg='#BBBBBB', bg='#2b2b2b')
Date_result_label2 = Label(Date_cal_frame, text='Difference(days)', fg='#BBBBBB', bg='#2b2b2b')
Result1 = Entry(Date_cal_frame, fg='white', bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Result2 = Entry(Date_cal_frame, fg='white', bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Calculate = Button(Date_cal_frame, bg='#2b2b2b', fg='white', text='Calculate')

Date_from_label.place(x=10, y=30)
Date_to_label.place(x=170, y=35)
Date_from.place(x=50, y=35, width=90)
Date_to.place(x= 200, y=35, width=90)
Date_result_label.place(x=10, y=65)
Date_result_label2.place(x=10, y=115)
Result1.place(x=13, y=87, width=278)
Result2.place(x=13, y=137, width=278)
Calculate.place(x=220, y=165, width=71, height=23)

#-------------------------- Calculator Graphic ------------------------------
backspace = Button(root, bg='#2b2b2b', fg='white', text='Backspace')
backspace.bind("<Button-1>", resolve_event)

clear = b1 = Button(root, bg='#2b2b2b', fg='white', text='C')
clear.bind("<Button-1>", resolve_event)

b1 = Button(root, bg='#2b2b2b', fg='white', text='1')
b1.bind("<Button-1>", resolve_event)

b2 = Button(root, bg='#2b2b2b', fg='white', text='2')
b2.bind("<Button-1>", resolve_event)

b3 = Button(root, bg='#2b2b2b', fg='white', text='3')
b3.bind("<Button-1>", resolve_event)

b4 = Button(root, bg='#2b2b2b', fg='white', text='4')
b4.bind("<Button-1>", resolve_event)

b5 = Button(root, bg='#2b2b2b', fg='white', text='5')
b5.bind("<Button-1>", resolve_event)

b6 = Button(root, bg='#2b2b2b', fg='white', text='6')
b6.bind("<Button-1>", resolve_event)

b7 = Button(root, bg='#2b2b2b', fg='white', text='7')
b7.bind("<Button-1>", resolve_event)

b8 = Button(root, bg='#2b2b2b', fg='white', text='8')
b8.bind("<Button-1>", resolve_event)

b9 = Button(root, bg='#2b2b2b', fg='white', text='9')
b9.bind("<Button-1>", resolve_event)

b0 = Button(root, bg='#2b2b2b', fg='white', text='0')
b0.bind("<Button-1>", resolve_event)

point = Button(root, bg='#2b2b2b', fg='white', text='.')
point.bind("<Button-1>", resolve_event)

equla = Button(root, bg='#2b2b2b', fg='white', text='=')
equla.bind("<Button-1>", resolve_event)

devide = Button(root, bg='#2b2b2b', fg='white', text='/')
devide.bind("<Button-1>", resolve_event)

multiply = Button(root, bg='#2b2b2b', fg='white', text='*')
multiply.bind("<Button-1>", resolve_event)

minus = Button(root, bg='#2b2b2b', fg='white', text='-')
minus.bind("<Button-1>", resolve_event)

plus = Button(root, bg='#2b2b2b', fg='white', text='+')
plus.bind("<Button-1>", resolve_event)

backspace.place(x=4, y=87, height=35, width=80)
clear.place(x=89, y=87, width=35, height=35)
b1.place(x=4, y=126, width=35, height=35)
b2.place(x=48, y=126, width=35, height=35)
b3.place(x=89, y=126, width=35, height=35)
b4.place(x=4, y=167, width=35, height=35)
b5.place(x=48, y=167, width=35, height=35)
b6.place(x=89, y=167, width=35, height=35)
b7.place(x=4, y=208, width=35, height=35)
b8.place(x=48, y=208, width=35, height=35)
b9.place(x=89, y=208, width=35, height=35)
b0.place(x=4, y=249, width=80, height=35)
point.place(x=89, y=249, width=35, height=35)
equla.place(x=130, y=249, width=35, height=35)
devide.place(x=130, y=87, width=35, height=35)
multiply.place(x=130, y=126, width=35, height=35)
minus.place(x=130, y=167, width=35, height=35)
plus.place(x=130, y=208, width=35, height=35)
root.mainloop()
