from tkinter import *
import clipboard
import webbrowser
import datetime

root = Tk()
root.config(bg='#2b2b2b')
root.geometry("476x251")
root.title('Calculator')
root.wm_maxsize(width=476, height=251)
root.wm_minsize(width=476, height=251)

Output_screen_value = StringVar()
Output_screen_value.set("")
from_date = StringVar()
to_date = StringVar()
diff_in_ymwd = StringVar()
diff_in_days = StringVar()
from_date.set(datetime.date.today())

def is_float(value):
    for e in value:
        if not (e >= '0' and e <= '9' or e == '.'):
            break
    else:
        if '.' in value:
            return True
    return False

def last_number_is_float(value):
    if len(value) > 0:
        if is_float(value):
            return True
        if value.isnumeric():
            return False
        ope = ''
        for e in value:
            if e in ['+', '-', '/', '*']:
                ope = e
        last_value = value.split(ope)
        last_value = last_value.pop()
        if is_float(last_value):
            return True
        else:
            return False
    else:
        return False
def last_value_is_ope(value):
    if len(value)>0 and value[len(value)-1] in ['-', '+', '*', '/', '.']:
        return True
    else:
        return False

def resolve_event(event):
    global Output_screen_value
    global Output_screen
    text = event.widget.cget('text')
    if text=='C':
        Output_screen_value.set("")
    elif text=='=' and len(Output_screen_value.get())>0:
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        ope = ['-', '+', '*', '/']
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
        if len(Output_screen_value.get()) != 0:
            value = Output_screen_value.get()
            value = value[0:len(value)-1]
            Output_screen_value.set(value)
    else:
        if (text >= '0' and text <= '9') and len(Output_screen_value.get()) < 50:
            Output_screen_value.set(Output_screen_value.get()+text)
        elif text=='.' and len(Output_screen_value.get())<49 and len(Output_screen_value.get())!=0:
            if not last_number_is_float(Output_screen_value.get()):
                if not last_value_is_ope(Output_screen_value.get()):
                    Output_screen_value.set(Output_screen_value.get() + text)
                else:
                    return
            else:
                return
        elif len(Output_screen_value.get()) < 49 and len(Output_screen_value.get()) != 0:
            if last_value_is_ope(Output_screen_value.get()):
                return
            Output_screen_value.set(Output_screen_value.get() + text)
def open_url(url):
    try:
        webbrowser.get('chrome').open_new(url)
    except:
        try:
            webbrowser.get('firefox').open_new_tab(url)
        except:
            try:
                webbrowser.open(url, new=1)
            except:
                return False
    return True

def author_profile():
    profile_screen = Tk()
    profile_screen.geometry('400x200')
    profile_screen.config(bg='#2b2b2b')
    profile_screen.title('About')

    info_label = Label(profile_screen, text='Copyright@2019 Calculator created by Harvindar singh', fg='white', bg='#2b2b2b')
    info_label2 = Label(profile_screen, text='Version 1.0.0, Build Date 13/05/2019', fg='white', bg='#2b2b2b')
    info_label3 = Label(profile_screen, text='www.brightgoal.com', fg='white', bg='#2b2b2b')
    Main_label = Label(profile_screen, text='Brightgoal.in', font=('calibari', 20), fg='white', bg='#2b2b2b')
    my_name = Label(profile_screen, text='by Harvindar singh', fg='white', bg='#2b2b2b')
    Visit_on = Button(profile_screen, text='  Visit on Brightgoal  ', bg='#2b2b2b', fg='white', command=(lambda  value='https://www.brightgoal.in': open_url(value)))
    Main_label.place(x=120, y=20)
    my_name.place(x=144, y=55)
    info_label.place(x=55, y=80)
    info_label2.place(x=105, y=100)
    info_label3.place(x=140, y=120)
    Visit_on.place(x=139, y=150)

def date_calculation(date_from='01-01-2019' , date_to='01-01-2019'):
    print('Working')
    # today = datetime.date.today()
    # someday = datetime.date(2008, 12, 25)
    # diff = someday - today
    # diff.days
    day = 0
    month = 0
    year = 0
    year, month, day = [int(e) for e in date_from.split('-')]
    From = datetime.date(year, month, day)
    year, month, day = [int(e) for e in date_to.split('-')]
    To = datetime.date(year, month, day)
    diff = To - From
    diff_in_days.set(diff.days)
    Total_days = diff.days
    year = str(int(Total_days/365))
    Total_days = Total_days%365
    week = str(int(Total_days/7))
    Total_days = str(int(Total_days%7))
    result = year +' years, '+week+' week, '+Total_days+' days'
    diff_in_ymwd.set(result)
#-------------------------- Menu Create ------------------------------
Mainmenu = Menu(root)
root.config(menu=Mainmenu)

Opption = Menu(Mainmenu, tearoff=0)
About_menu = Menu(Mainmenu, tearoff=0)

Email = Menu(About_menu, tearoff=0)
contact_number = Menu(About_menu, tearoff=0)
Email.add_command(label='brightgoal.enquiry@gmail.com', command=(lambda value="": clipboard.copy('brightgoal.enquiry@gmail.com')))
contact_number.add_command(label='+919140417112', command=(lambda value="": clipboard.copy('+919140417112')))

About_menu.add_command(label='About Calculator', command=author_profile)
About_menu.add_cascade(label='Contact number   ', menu=contact_number)
About_menu.add_cascade(label='Email', menu=Email)
About_menu.add_command(label='Support', command=(lambda  value='https://www.brightgoal.in': open_url(value)))

Opption.add_command(label='Copy result in clipbord', command=(lambda value="": clipboard.copy(Output_screen_value.get())))
Opption.add_command(label='More Projects', command=(lambda  value='https://www.instamojo.com/Brightgoal/': open_url(value)))
Opption.add_command(label='Exit', command=(lambda value=0: exit(value)))

Mainmenu.add_cascade(label='Option', menu=Opption)
Mainmenu.add_cascade(label='Help', menu=About_menu)

#-------------------------- Main Screen Creation ------------------------------
Output_screen = Entry(root, bg='#2b2b2b', disabledbackground='#2b2b2b', foreground='white', textvar=Output_screen_value, justify=RIGHT)
Output_screen.config(font=('calibari', 12), state=DISABLED, disabledforeground='white')
Output_screen.config(highlightbackground='gray33', highlightthickness=1)
Output_screen.place(x=4, y=4, width=469, height=35)

Date_cal_frame = Frame(root, bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Date_cal_frame.place(x=172, y=42, width = 300, height=205)
Date_label = Label(Date_cal_frame, bg='#3c3f41', text='Date Calculation', fg='#BBBBBB')
Date_label.pack(fill=X)

#-------------------------- Calculators Frame ------------------------------
Calculator_frame = Frame(root, bg='#2b2b2b')
Calculator_frame.place(x=4, y=42, width=166, height=207)

#-------------------------- Date Calculation Graphic ------------------------------
Date_from_label = Label(Date_cal_frame, text='From', fg='#BBBBBB', bg='#2b2b2b')
Date_to_label = Label(Date_cal_frame, text='To', fg='#BBBBBB', bg='#2b2b2b')
Date_from = Entry(Date_cal_frame, textvar = from_date, fg='white', bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Date_to = Entry(Date_cal_frame, textvar = to_date, fg='white', bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Date_result_label = Label(Date_cal_frame, text='Difference (year, months, weeks, days)', fg='#BBBBBB', bg='#2b2b2b')
Date_result_label2 = Label(Date_cal_frame, text='Difference(days)', fg='#BBBBBB', bg='#2b2b2b')
Result1 = Entry(Date_cal_frame, disabledforeground='white', disabledbackground='#2b2b2b', state=DISABLED, textvar = diff_in_ymwd, fg='white', bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Result2 = Entry(Date_cal_frame, disabledforeground='white', disabledbackground='#2b2b2b', state=DISABLED, textvar = diff_in_days, fg='white', bg='#2b2b2b', highlightbackground='gray33', highlightthickness=1)
Calculate = Button(Date_cal_frame, bg='#2b2b2b', fg='white', text='Calculate', command=(lambda value=0: date_calculation(from_date.get(), to_date.get())))

Date_from_label.place(x=10, y=35)
Date_to_label.place(x=170, y=35)
Date_from.place(x=50, y=35, width=90)
Date_to.place(x= 200, y=35, width=90)
Date_result_label.place(x=10, y=65)
Date_result_label2.place(x=10, y=115)
Result1.place(x=13, y=87, width=278)
Result2.place(x=13, y=137, width=278)
Calculate.place(x=214, y=169, width=77, height=26)

#-------------------------- Calculator Graphic ------------------------------
backspace = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='Backspace')
backspace.bind("<Button>", resolve_event)

clear = b1 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='C')
clear.bind("<Button>", resolve_event)

b1 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='1')
b1.bind("<Button>", resolve_event)

b2 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='2')
b2.bind("<Button>", resolve_event)

b3 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='3')
b3.bind("<Button>", resolve_event)

b4 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='4')
b4.bind("<Button>", resolve_event)

b5 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='5')
b5.bind("<Button>", resolve_event)

b6 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='6')
b6.bind("<Button>", resolve_event)

b7 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='7')
b7.bind("<Button>", resolve_event)

b8 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='8')
b8.bind("<Button>", resolve_event)

b9 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='9')
b9.bind("<Button>", resolve_event)

b0 = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='0')
b0.bind("<Button>", resolve_event)

point = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='.')
point.bind("<Button>", resolve_event)

equla = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='=')
equla.bind("<Button>", resolve_event)

devide = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='/')
devide.bind("<Button>", resolve_event)

multiply = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='*')
multiply.bind("<Button>", resolve_event)

minus = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='-')
minus.bind("<Button>", resolve_event)

plus = Button(Calculator_frame, bg='#2b2b2b', fg='white', text='+')
plus.bind("<Button>", resolve_event)

backspace.place(x=0, y=0, height=35, width=78)
clear.place(x=86, y=0, width=35, height=35)
b1.place(x=0, y=41, width=35, height=35)
b2.place(x=43, y=41, width=35, height=35)
b3.place(x=86, y=41, width=35, height=35)
b4.place(x=0, y=84, width=35, height=35)
b5.place(x=43, y=84, width=35, height=35)
b6.place(x=86, y=84, width=35, height=35)
b7.place(x=0, y=127, width=35, height=35)
b8.place(x=43, y=127, width=35, height=35)
b9.place(x=86, y=127, width=35, height=35)
b0.place(x=0, y=170, width=78, height=35)
point.place(x=86, y=170, width=35, height=35)
equla.place(x=129, y=170, width=35, height=35)
devide.place(x=129, y=0, width=35, height=35)
multiply.place(x=129, y=41, width=35, height=35)
minus.place(x=129, y=84, width=35, height=35)
plus.place(x=129, y=127, width=35, height=35)
root.mainloop()
