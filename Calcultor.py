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
to_date.set(datetime.date.today())

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

def check_leap_year_or_not(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

def formating_date(date):
    if len(date) == 10:
        if (date[2] == '-' or date[2] == '/' or date[2] == ',' or date[2] == ':' or date[2] == '.' or date[2] == '\\') and (date[5] == '-' or date[5] == '/' or date[5] == ',' or date[5] == ':' or date[5] == '.' or date[5] == '\\'):
            try:
                day = int(date[0:2])
                month = int(date[3:5])
                year = int(date[6:10])
            except:
                return 0, 0, 0
        elif (date[4] == '-' or date[4] == '/' or date[4] == ',' or date[4] == ':' or date[4] == '.' or date[4] == '\\') and (date[7] == '-' or date[7] == '/' or date[7] == ',' or date[7] == ':' or date[7] == '.' or date[7] == '\\'):
            try:
                year = int(date[0:4])
                month = int(date[5:7])
                day = int(date[8:10])
            except:
                return 0, 0, 0
        else:
            return 0, 0, 0
    elif len(date) == 9:
        if (date[4] == '-' or date[4] == '/' or date[4] == ',' or date[4] == ':' or date[4] == '.' or date[4] == '\\') and (date[1] == '-' or date[1] == '/' or date[1] == ',' or date[1] == ':' or date[1] == '.' or date[1] == '\\'):
            day = date[0:1]
            month = date[2:4]
            year = date[5:9]
        elif (date[4] == '-' or date[4] == '/' or date[4] == ',' or date[4] == ':' or date[4] == '.' or date[4] == '\\') and (date[2] == '-' or date[2] == '/' or date[2] == ',' or date[2] == ':' or date[2] == '.' or date[2] == '\\'):
            day = date[0:2]
            month = date[3:4]
            year = date[5:9]
        elif (date[4] == '-' or date[4] == '/' or date[4] == ',' or date[4] == ':' or date[4] == '.' or date[4] == '\\') and (date[6] == '-' or date[6] == '/' or date[6] == ',' or date[6] == ':' or date[6] == '.' or date[6] == '\\'):
            year = date[0:4]
            month = date[5:7]
            day = date[8:9]
        elif (date[4] == '-' or date[4] == '/' or date[4] == ',' or date[4] == ':' or date[4] == '.' or date[4] == '\\') and (date[7] == '-' or date[7] == '/' or date[7] == ',' or date[7] == ':' or date[7] == '.' or date[7] == '\\'):
            year = date[0:4]
            month = date[5:6]
            day = date[7:9]
        else:
            return 0, 0, 0
    elif len(date) == 8:
        if (date[3] == '-' or date[3] == '/' or date[3] == ',' or date[3] == ':' or date[3] == '.' or date[3] == '\\') and (date[1] == '-' or date[1] == '/' or date[1] == ',' or date[1] == ':' or date[1] == '.' or date[1] == '\\'):
            day = date[0:1]
            month = date[2:3]
            year = date[4:8]
        elif (date[4] == '-' or date[4] == '/' or date[4] == ',' or date[4] == ':' or date[4] == '.' or date[4] == '\\') and (date[6] == '-' or date[6] == '/' or date[6] == ',' or date[6] == ':' or date[6] == '.' or date[6] == '\\'):
            year = date[0:4]
            month = date[5:6]
            day = date[7:8]
        else:
            return 0, 0, 0
    else:
        return 0, 0, 0

    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except:
        return 0, 0, 0
    return day, month, year

def calculate_date(from_date, to_date):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_from, month_from, year_from = formating_date(from_date)
    day_to, month_to, year_to = formating_date(to_date)

    Total_weeks = 0
    Total_year = 0
    Total_days = 0
    Total_month = 0
    if year_from != year_to:
        # Count from_date total months and remains days.
        if check_leap_year_or_not(year_from):
            if leap_months[month_from-1]-day_from == 0:
                Total_month_of_from_date = 12 - month_from
                Total_remains_day_of_from_date = 0
            else:
                Total_month_of_from_date = 12 - month_from
                Total_remains_day_of_from_date = leap_months[month_from-1] - day_from
        else:
            if month_days[month_from-1]-day_from == 0:
                Total_month_of_from_date = 12 - month_from
                Total_remains_day_of_from_date = 0
            else:
                Total_month_of_from_date = 12 - month_from
                Total_remains_day_of_from_date = month_days[month_from-1] - day_from

        # Count to_date total months and remains days.
        if check_leap_year_or_not(year_to):
            if leap_months[month_to-1]-day_to == 0:
                Total_month_of_to_date = month_to
                Total_remains_day_of_to_date = 0
            else:
                Total_month_of_to_date = month_to - 1
                Total_remains_day_of_to_date = day_to
        else:
            if month_days[month_to-1]-day_to == 0:
                Total_month_of_to_date = month_to
                Total_remains_day_of_to_date = 0
            else:
                Total_month_of_to_date = month_to - 1
                Total_remains_day_of_to_date = day_to

        Total_year = (year_to - year_from) - 1

        if Total_month_of_from_date == 12 and Total_remains_day_of_from_date == 0:
            Total_year += 1
            Total_month_of_from_date = 0
        if Total_month_of_to_date == 12 and Total_remains_day_of_to_date == 0:
            Total_year += 1
            Total_month_of_to_date = 0

        Total_days = Total_remains_day_of_to_date + Total_remains_day_of_from_date
        if check_leap_year_or_not(year_to):
            while True:
                if Total_days >= leap_months[Total_month_of_to_date]:
                    Total_days -= leap_months[Total_month_of_to_date]
                    Total_month_of_to_date += 1
                    if Total_month_of_to_date == 12:
                        Total_year += 1
                        Total_month_of_to_date = 0
                else:
                    break
        else:
            while True:
                if Total_days >= month_days[Total_month_of_to_date]:
                    Total_days -= month_days[Total_month_of_to_date]
                    Total_month_of_to_date += 1
                    if Total_month_of_to_date == 12:
                        Total_year += 1
                        Total_month_of_to_date = 0
                else:
                    break
        Total_month = Total_month_of_to_date + Total_month_of_from_date
        while True:
            if Total_month >= 12:
                Total_year += 1
                Total_month -= 12
            else:
                break
        if Total_days > 7:
            Total_weeks = int(Total_days / 7)
            Total_days = Total_days % 7

        result = ''
        if int(Total_year) > 0:
            result = str(Total_year) + ' year'
        if int(Total_month) > 0:
            result += ', ' + str(Total_month) + ' month'
        if int(Total_weeks) > 0:
            result += ', ' + str(Total_weeks) + ' week'
        if int(Total_days) > 0:
            result += ', ' + str(Total_days) + ' day'

        From_date = datetime.date(year_from, month_from, day_from)
        TO_date = datetime.date(year_to, month_to, day_to)
        Total_day = TO_date - From_date
        Total_day = str(Total_day.days)
        diff_in_ymwd.set(result)
        diff_in_days.set(Total_day+' day')
    else:

        Total_month = 0
        Total_year = 0
        Total_day = 0
        Total_weeks = 0
        From_date = datetime.date(year_from, month_from, day_from)
        TO_date = datetime.date(year_to, month_to, day_to)

        Total_day = TO_date - From_date
        Total_day = Total_day.days
        start_month = month_from
        while True:
            if check_leap_year_or_not(year_to):
                if Total_day > leap_months[start_month-1]:
                    Total_month += 1
                    Total_day -= leap_months[start_month-1]
                    start_month += 1
                    if Total_month >= 12:
                        Total_year += 1
                        Total_month = 0
                else:
                    break
            else:
                if Total_day > month_days[start_month-1]:
                    Total_month += 1
                    Total_day -= month_days[start_month-1]
                    start_month += 1
                    if Total_month >= 12:
                        Total_year += 1
                        Total_month = 0
                else:
                    break
        if Total_day >= 7:
            Total_weeks = str(int(Total_day / 7))
            Total_day = str(int(Total_day % 7))

        result = ''
        if int(Total_year) > 0:
            result = str(Total_year)+' year'
        if int(Total_month) > 0:
            result += ', '+str(Total_month)+' month'
        if int(Total_weeks) > 0:
            result += ', '+str(Total_weeks)+' week'
        if int(Total_day) > 0:
            result += ', '+str(Total_day)+' day'

        Total_day = TO_date - From_date
        Total_day = str(Total_day.days)
        diff_in_ymwd.set(result)
        diff_in_days.set(Total_day+' day')

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
Calculate = Button(Date_cal_frame, bg='#2b2b2b', fg='white', text='Calculate', command=(lambda value=0: calculate_date(from_date.get(), to_date.get())))

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
