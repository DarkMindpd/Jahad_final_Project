"""
کتابخانه های مورد نیاز برای اجرا
تیکینتر برای محیط گرافیکی
استرینگ برای حروف الفبا
اواس برای مدیریت فایل
متپلات برای نمودار و رسم آن در تیکینتر به جای محیط جدا
امپورت عکس به برنامه
"""

from tkinter import Tk, Label, Button, Frame, Entry, messagebox, ANCHOR, StringVar, ttk, PhotoImage
import string
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib

matplotlib.use('TkAgg')

Alphabet = set(string.ascii_lowercase + string.ascii_uppercase)
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '-', '.'}

"""
ساخت تابع برای ایجاد فرم ورود به محیط اصلی
"""


def enter_part():
    """
    ساخت کلاس پیج برای بالا کشیدن فریم های جدید
    """

    class Page(Frame):
        def __init__(self, *ar, **ars):
            Frame.__init__(self, *ar, **ars)

        def show(self):
            self.lift()

    """
    ساخت پیج با استفاده از کلاس که ولیو هارا تعریف کند
    """

    class Login(Page):
        """
        برای ارث بری از کلاس پیجی که ساختیم از این تابع استفاده میکنیم
        برای بالا کشیدن و ساخت فریم
        در دفعات بعد اشاره نمیکنم
        """

        def __init__(self, *ar, **ars):
            Page.__init__(self, *ar, **ars)

            """
            ساخت تابع کلی لاگین برای راستی آزمایی و ورود
            """

            def log_in():

                """
                ساخت تابع جست و جو برای یافتن کاربران
                """

                def login_registered():
                    user_pass_mail = open('./appfiles/Documents/userpass.txt')
                    upm = user_pass_mail.readlines()
                    ump_list = list()
                    for i in upm:
                        ump_list.append(i.split())
                    return ump_list

                """
                گرفتن دیتا از ورودی ها و راستی آزمایی
                """
                user_mail = log_in_User_Mail.get()
                log_in_password = log_in_Pass.get()
                exist = False
                for i in login_registered():
                    if user_mail in i:
                        if log_in_password in i:
                            log_in_User_Mail.configure(highlightbackground='green', highlightcolor='#4584F1')
                            log_in_Pass.configure(highlightbackground='green', highlightcolor='#4584F1')
                            messagebox.showinfo(title='Completed', message=f'Its all done.\nWellcome Back {user_mail}')
                            exist = True
                            frm.destroy()
                            login_trust = open('./appfiles/Documents/login_trust.txt', 'a')
                            login_trust.write(str(login_registered().index(i)))
                            login_trust.close()
                            app_part()
                            break
                        else:
                            log_in_User_Mail.configure(highlightbackground='red', highlightcolor='red')
                            log_in_Pass.configure(highlightbackground='red', highlightcolor='red')
                            messagebox.showinfo(title='Error', message='Invalid Username/Mail or Password.')
                            exist = True
                            break
                    else:
                        exist = False
                if not exist:
                    log_in_User_Mail.configure(highlightbackground='orange', highlightcolor='orange')
                    log_in_Pass.configure(highlightbackground='orange', highlightcolor='orange')
                    messagebox.showinfo(title='Error', message='Your Account not found.\nPlease Sing Up.')

            log_in_User_Mail_label = Label(self, text='Enter Username or Mail:', bg='Whitesmoke', font=('', '10'))
            log_in_User_Mail = Entry(self, bg='white', font=('', '20'), width=30, bd=2, relief='flat',
                                     highlightthickness=1,
                                     highlightbackground='black',
                                     highlightcolor='#4584F1')

            log_in_Pass_label = Label(self, text='Enter Password:', bg='Whitesmoke', font=('', '10'))
            log_in_Pass = Entry(self, bg='white', font=('', '20'), width=30, show='*', bd=2, relief='flat',
                                highlightthickness=1,
                                highlightbackground='black',
                                highlightcolor='#4584F1')

            log_in_button = Button(self, text='Log in', bg='#DCD0FF', fg='black', font=('', '20'), command=log_in)

            log_in_User_Mail_label.place(x=333, y=185)
            log_in_User_Mail.place(x=333, y=205)

            log_in_Pass_label.place(x=333, y=315)
            log_in_Pass.place(x=333, y=335)

            log_in_button.place(x=510, y=465)

            image = PhotoImage(file='./appfiles/image/jahad_daneshgahi.png')
            panel = Label(self, image=image)
            panel.photo = image
            panel.place(x=5, y=5)

    """
    ساخت پیج با استفاده از کلاس که ولیو هارا تعریف کنذ
    """

    class SingUP(Page):
        def __init__(self, *ar, **ars):
            Page.__init__(self, *ar, **ars)

            """
            تابع ساینآپ برای ساخت اکانت جدید
            """

            def sing_up():

                """
                یافتن اعضای از پیش ثبت شده در فایل
                """

                def registered():
                    reg = set()
                    user_pass = open('./appfiles/Documents/userpass.txt')
                    user_data = open('./appfiles/Documents/userdata.txt')

                    us = user_pass.readlines()

                    for i in us:
                        splitted = i.split()
                        reg.add(splitted[0])

                    ua = user_data.readlines()

                    for i in ua:
                        splitted = i.split()
                        reg.add(splitted[4])
                        reg.add(splitted[9])
                    user_data.close()
                    user_pass.close()
                    return reg

                """
                راستی آزمایی ورودی ها و سیو آنها
                """
                trust = False

                TorF = set(str(F_name.get()))
                for i in TorF:
                    if i in Alphabet and len(F_name.get()) > 2:
                        trust = True
                    else:
                        trust = False
                        break
                F_name.configure(highlightbackground='red', highlightcolor='red')
                if trust:
                    F_name.configure(highlightbackground='green', highlightcolor='#4584F1')
                    f_name = F_name.get()

                TorF = set(str(L_name.get()))
                for i in TorF:
                    if i in Alphabet and len(L_name.get()) > 2:
                        trust = True
                    else:
                        trust = False
                        break
                L_name.configure(highlightbackground='red', highlightcolor='red')
                if trust:
                    L_name.configure(highlightbackground='green', highlightcolor='#4584F1')
                    l_name = L_name.get()

                TorF = set(str(Mail.get()))
                mail_exist = Label(self)
                mail_exist.place(x=710, y=120)
                if '@' in TorF and len(Mail.get()) > 7:
                    if str(Mail.get()) not in registered():
                        mail = Mail.get()
                        Mail.configure(highlightbackground='green', highlightcolor='#4584F1')
                        mail_exist.config(text='                   ', bg='Whitesmoke', fg='orange', font=('', '10'))
                    elif str(Mail.get()) in registered():
                        mail_exist.config(text='already exist', bg='Whitesmoke', fg='orange', font=('', '10'))
                        Mail.configure(highlightbackground='orange', highlightcolor='orange')
                else:
                    Mail.configure(highlightbackground='red', highlightcolor='red')

                TorF = set(str(User.get()))
                user_exist = Label(self)
                user_exist.place(x=710, y=190)
                if len(str(User.get())) == 0:
                    TorF.add(0)
                for i in TorF:
                    if i in (Alphabet | numbers) and not i == '' and len(User.get()) > 6:
                        if str(User.get()) not in registered():
                            trust = True
                            user_exist.config(text='                   ', bg='Whitesmoke', fg='orange', font=('', '10'))
                        else:
                            user_exist.config(text='already exist', bg='Whitesmoke', fg='orange', font=('', '10'))
                            User.configure(highlightbackground='orange', highlightcolor='orange')
                            trust = False
                            break
                    else:
                        User.configure(highlightbackground='red', highlightcolor='red')
                        trust = False
                        break
                if trust:
                    User.configure(highlightbackground='green', highlightcolor='#4584F1')
                    user = User.get()

                if len(Pass.get()) > 7:
                    password = Pass.get()
                    Pass.configure(highlightbackground='green', highlightcolor='#4584F1')
                else:
                    Pass.configure(highlightbackground='red', highlightcolor='red')

                TorF = set(str(Born.get()))
                if len(str(Born.get())) == 0:
                    TorF.add(0)
                for i in TorF:
                    if i in numbers and len(Born.get()) == 10:
                        trust = True
                    else:
                        trust = False
                        break
                Born.configure(highlightbackground='red', highlightcolor='red')
                if trust:
                    Born.configure(highlightbackground='green', highlightcolor='#4584F1')
                    born = Born.get()

                TorF = set(str(Meli_code.get()))
                meli_code_exist = Label(self)
                meli_code_exist.place(x=635, y=260)
                if len(str(Meli_code.get())) == 0:
                    TorF.add(0)
                for i in TorF:
                    if i in numbers and len(Meli_code.get()) == 10 and i not in ('-', '_', '.'):
                        if str(Meli_code.get()) not in registered():
                            meli_code_exist.config(text='                   ', bg='Whitesmoke', fg='orange',
                                                   font=('', '10'))
                            trust = True
                        else:
                            meli_code_exist.config(text='already exist', bg='Whitesmoke', fg='orange', font=('', '10'))
                            Meli_code.configure(highlightbackground='orange', highlightcolor='orange')
                            trust = False
                            break
                    else:
                        trust = False
                        Meli_code.configure(highlightbackground='red', highlightcolor='red')
                        break
                if trust:
                    Meli_code.configure(highlightbackground='green', highlightcolor='#4584F1')
                    meli_code = Meli_code.get()

                """
                ذخیره ی دیتا در فایل ها
                """
                try:
                    data = f'Fullname: {f_name} {l_name} Mail: {mail} born: {born} Meli code: {meli_code}\n'
                    Password = f'{user} {password} {mail}\n'
                    user_pass = open('./appfiles/Documents/userpass.txt', 'a')
                    user_data = open('./appfiles/Documents/userdata.txt', 'a')
                    user_data.write(data)
                    user_pass.write(Password)
                    user_pass.close()
                    user_data.close()
                    registered()
                    messagebox.showinfo(title='Completed', message='Its all done.\nPlease log in')
                except:
                    messagebox.showinfo(title='Error', message='Invalid entries.\nPlease try again')

            F_name_label = Label(self, text='Enter First name:', bg='Whitesmoke', font=('', '10'))
            F_name = Entry(self, bg='white', font=('', '20'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')

            L_name_label = Label(self, text='Enter Last name:', bg='Whitesmoke', font=('', '10'))
            L_name = Entry(self, bg='white', font=('', '20'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')

            Mail_label = Label(self, text='Enter Mail:', bg='Whitesmoke', font=('', '10'))
            Mail = Entry(self, bg='white', font=('', '20'), width=30, bd=2, relief='flat',
                         highlightthickness=1,
                         highlightbackground='black',
                         highlightcolor='#4584F1')

            User_label = Label(self, text='Enter User name:', bg='Whitesmoke', font=('', '10'))
            User = Entry(self, bg='white', font=('', '20'), width=30, bd=2, relief='flat',
                         highlightthickness=1,
                         highlightbackground='black',
                         highlightcolor='#4584F1')

            Pass_label = Label(self, text='Enter Password:', bg='Whitesmoke', font=('', '10'))
            Pass = Entry(self, bg='white', font=('', '20'), width=20, show='*', bd=2, relief='flat',
                         highlightthickness=1,
                         highlightbackground='black',
                         highlightcolor='#4584F1')

            Born_label = Label(self, text='Enter date of born:', bg='Whitesmoke', font=('', '10'))
            Born = Entry(self, bg='white', font=('', '20'), width=20, bd=2, relief='flat',
                         highlightthickness=1,
                         highlightbackground='black',
                         highlightcolor='#4584F1')

            Meli_code_label = Label(self, text='Enter Melli code:', bg='Whitesmoke', font=('', '10'))
            Meli_code = Entry(self, bg='white', font=('', '20'), width=20, bd=2, relief='flat',
                              highlightthickness=1,
                              highlightbackground='black',
                              highlightcolor='#4584F1')

            SingUP_button = Button(self, text='Sing Up', bg='#DCD0FF', fg='black', font=('', '20'), command=sing_up)

            F_name_label.place(x=333, y=55)
            F_name.place(x=333, y=75)

            L_name_label.place(x=573, y=55)
            L_name.place(x=573, y=75)

            Mail_label.place(x=333, y=125)
            Mail.place(x=333, y=145)

            User_label.place(x=333, y=195)
            User.place(x=333, y=215)

            Meli_code_label.place(x=408, y=265)
            Meli_code.place(x=408, y=285)

            Pass_label.place(x=408, y=405)
            Pass.place(x=408, y=425)

            Born_label.place(x=408, y=335)
            Born.place(x=408, y=355)

            SingUP_button.place(x=500, y=495)

            image = PhotoImage(file='./appfiles/image/jahad_daneshgahi.png')
            panel = Label(self, image=image)
            panel.photo = image
            panel.place(x=5, y=5)

    """
    کلاس اصلی فرم برای ایجاد صفحات و قرار دادن آن ها روی یک فرم
    """

    class Main(Frame):
        def __init__(self, *ar, **ars):
            Frame.__init__(self, *ar, **ars)

            p1 = Login(self)
            p2 = SingUP(self)

            but = Frame(self)
            con = Frame(self)

            but.pack(side='bottom', fill='x', expand=False)
            con.pack(side='top', fill='both', expand=True)

            p1.place(in_=con, x=0, y=0, relheight=1, relwidth=1)
            p2.place(in_=con, x=0, y=0, relheight=1, relwidth=1)

            def change_color(button):
                for i in (b1, b2):
                    i.configure(bg='#DCD0FF')
                button.configure(bg='#6ca5eb')

            b1 = Button(but, text='Log IN page', bg='#DCD0FF', font=('', '15'),
                        command=lambda: [change_color(b1), p1.show()])
            b2 = Button(but, text='Sing UP page', bg='#DCD0FF', font=('', '15'),
                        command=lambda: [change_color(b2), p2.show()])

            b1.pack(side='left')
            b2.pack(side='left')

            change_color(b1)
            p1.show()

    frm = Tk(className='Student organizer Log in page')
    main = Main(frm)
    main.pack(side='top', fill='both', expand=True)
    frm.geometry('1120x680')
    frm.mainloop()


# ----------------------------------------------------------------------------------------------------------------------

"""
بعد از عبور از مرحله ی قبل وارد برنامه اصلی میشویم
تابع اپ پارت برای دسترسی کامل به فرم برنامه
"""


def app_part():
    """
    مانند بخش قبلی
    """

    class Page(Frame):
        def __init__(self, *ar, **ars):
            Frame.__init__(self, *ar, **ars)

        def show(self):
            self.lift()

    """
    صفحه ورود دیتا جدید دانش آموزان
    """

    class enter_data_page(Page):
        def __init__(self, *ar, **ars):
            Page.__init__(self, *ar, **ars)

            """
            تابع ذخیره ی داده برای ورودی های جدید
            """

            def save_data():

                """
                تابعی برای جلو گیری از ورود دیتا های تکرای
                و پیدا کردن دانش آموز
                دلیل تکرار این تابع در هر صفحه به دلیل قابلیت جدا شدن هر پارت میباشد
                نه افزونگی
                """

                def registered():
                    reg = set()
                    student_data = open('./appfiles/Documents/Student/Student_data.txt')

                    sd = student_data.readlines()

                    for s in sd:
                        splitted = s.split()
                        reg.add(splitted[5])
                        reg.add(splitted[8])

                    student_data.close()

                    return reg

                """
                راستی آزمایی ورودی ها با توجه به تابع سرچ
                """
                trust = False
                TorF = set(str(student_f_name.get()))
                for i in TorF:
                    if i in Alphabet and len(student_f_name.get()) > 2:
                        trust = True
                    else:
                        trust = False
                        break
                student_f_name.configure(highlightbackground='red', highlightcolor='red')
                if trust:
                    student_f_name.configure(highlightbackground='green', highlightcolor='#4584F1')
                    s_f_name = student_f_name.get()

                trust = False
                TorF = set(str(student_l_name.get()))
                for i in TorF:
                    if i in Alphabet and len(student_l_name.get()) > 2:
                        trust = True
                    else:
                        trust = False
                        break
                student_l_name.configure(highlightbackground='red', highlightcolor='red')
                if trust:
                    student_l_name.configure(highlightbackground='green', highlightcolor='#4584F1')
                    s_l_name = student_l_name.get()

                trust = False
                TorF = set(str(student_section.get()))
                for i in TorF:
                    if i in Alphabet and len(student_section.get()) > 2 or i == ' ':
                        trust = True
                    else:
                        trust = False
                        break
                student_section.configure(highlightbackground='red', highlightcolor='red')
                if trust:
                    student_section.configure(highlightbackground='green', highlightcolor='#4584F1')
                    s_section = student_section.get()

                trust = False
                TorF = set(str(student_major.get()))
                for i in TorF:
                    if i in Alphabet and len(student_major.get()) > 2:
                        trust = True
                    else:
                        trust = False
                        break
                student_major.configure(highlightbackground='red', highlightcolor='red')
                if trust:
                    student_major.configure(highlightbackground='green', highlightcolor='#4584F1')
                    s_major = student_major.get()

                TorF = set(str(student_meli_code.get()))
                if len(str(student_meli_code.get())) == 0:
                    TorF.add(0)
                student_meli_code_exist = Label(self)
                student_meli_code_exist.place(x=420, y=110)
                for i in TorF:
                    if i in numbers and len(student_meli_code.get()) == 10 and i not in ('-', '_', '.'):
                        if str(student_meli_code.get()) not in registered():
                            student_meli_code_exist.config(text='                   ', bg='Whitesmoke', fg='orange',
                                                           font=('', '10'))
                            trust = True
                        else:
                            student_meli_code_exist.config(text='already exist', bg='Whitesmoke', fg='orange',
                                                           font=('', '10'))
                            student_meli_code.configure(highlightbackground='orange', highlightcolor='orange')
                            trust = False
                            break
                    else:
                        trust = False
                        student_meli_code_exist.config(text='                   ', bg='white', fg='orange',
                                                       font=('', '10'))
                        student_meli_code.configure(highlightbackground='red', highlightcolor='red')
                        break
                if trust:
                    student_meli_code.configure(highlightbackground='green', highlightcolor='#4584F1')
                    s_meli_code = student_meli_code.get()

                TorF = set(str(student_code.get()))
                if len(str(student_code.get())) == 0:
                    TorF.add(0)
                student_code_exist = Label(self)
                student_code_exist.place(x=420, y=170)
                for i in TorF:
                    if i in numbers and i not in ('-', '_', '.'):
                        if str(student_code.get()) not in registered():
                            student_code_exist.config(text='                   ', bg='Whitesmoke', fg='orange',
                                                      font=('', '10'))
                            trust = True
                        else:
                            student_code_exist.config(text='already exist', bg='Whitesmoke',
                                                      fg='orange', font=('', '10'))
                            student_code.configure(highlightbackground='orange', highlightcolor='orange')
                            global c_trust
                            trust = False
                            break
                    else:
                        trust = False
                        student_code_exist.config(text='                   ', bg='white', fg='orange', font=('', '10'))
                        student_code.configure(highlightbackground='red', highlightcolor='red')
                        break
                if trust:
                    student_code.configure(highlightbackground='green', highlightcolor='#4584F1')
                    s_code = student_code.get()

                """
                ساخت این تابع برای این بود که از بین 1 تا 10
                درس بتوان به دانشجو اضافه کرد
                نه فقط میانگین
                """

                def get_scores():
                    l_s = [[], []]
                    trust = False
                    for code in lessons:
                        if not len(code.get()) == 0:
                            if not len((scores[lessons.index(code)]).get()) == 0 and \
                                    20 >= float((scores[lessons.index(code)]).get()) >= 0:
                                set_code = set(code.get())
                                set_score = set((scores[lessons.index(code)]).get())
                                for letter in (set_score | set_code):
                                    if letter in numbers and letter not in ('-', '_'):
                                        code.configure(highlightbackground='green', highlightcolor='#4584F1')
                                        (scores[lessons.index(code)]).configure(highlightbackground='green',
                                                                                highlightcolor='#4584F1')
                                        l_code = code.get()
                                        l_score = (scores[lessons.index(code)]).get()
                                        trust = True
                                    else:
                                        code.configure(highlightbackground='red', highlightcolor='red')
                                        (scores[lessons.index(code)]).configure(highlightbackground='red',
                                                                                highlightcolor='red')
                                        trust = False
                                        break
                            else:
                                trust = False
                                (scores[lessons.index(code)]).configure(highlightbackground='red',
                                                                        highlightcolor='red')
                        else:
                            code.configure(highlightbackground='red', highlightcolor='red')
                            (scores[lessons.index(code)]).configure(highlightbackground='red',
                                                                    highlightcolor='red')
                            trust = False

                        if trust:
                            l_s[0].append(l_code)
                            l_s[1].append(l_score)
                    return l_s

                """
                ذخیرهی داده های بدست آمده در فایل دانش آموزان
                با فرم مشخص
                """
                try:
                    student_data = open('./appfiles/Documents/Student/Student_data.txt', 'a')
                    student_data.write(f'FullName: {s_f_name} {s_l_name} Melli code: {s_meli_code} '
                                       f'Student code: {s_code} Section: {s_section} major: {s_major} '
                                       f'Course Credits: {(len((get_scores())[0]))} ')

                    if (len((get_scores())[0])) == 0:
                        student_data.write('\n')

                    try:
                        l_s = get_scores()
                        average = 0
                        for code in l_s[0]:
                            student_data.write(f'| Lesson Code: {code} Score: {l_s[1][(l_s[0]).index(code)]} |')
                            average += float(l_s[1][(l_s[0]).index(code)])
                        avg = average / (len((get_scores())[0]))
                        student_data.write(f' Average: {str(avg)} \n')
                        student_data.close()
                        messagebox.showinfo(title='Attention', message='Saved.')
                        c_trust = True
                    except:
                        messagebox.showinfo(title='Attention', message='New incoming student.\nWith no score.\nSaved.')
                        c_trust = True
                except:
                    messagebox.showinfo(title='Error', message='Invalid entries.\nPlease try again')
                    c_trust = False
                return c_trust

            """
            بخش ساخت و قرار دادن اشکال در صفحه
            """
            title = Label(self, text='Register:', bg='Whitesmoke', font=('', '30'))

            Label(self, text='Student FirstName:', bg='Whitesmoke', font=('', '10')).place(x=160, y=55)
            student_f_name = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                                   highlightthickness=1,
                                   highlightbackground='black',
                                   highlightcolor='#4584F1')

            Label(self, text='Student LastName:', bg='Whitesmoke', font=('', '10')).place(x=335, y=55)
            student_l_name = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                                   highlightthickness=1,
                                   highlightbackground='black',
                                   highlightcolor='#4584F1')

            Label(self, text='Student Melli code:', bg='Whitesmoke', font=('', '10')).place(x=160, y=115)
            student_meli_code = Entry(self, bg='white', font=('', '15'), width=30, bd=2, relief='flat',
                                      highlightthickness=1,
                                      highlightbackground='black',
                                      highlightcolor='#4584F1')

            Label(self, text='Student Code:', bg='Whitesmoke', font=('', '10')).place(x=160, y=175)
            student_code = Entry(self, bg='white', font=('', '15'), width=30, bd=2, relief='flat',
                                 highlightthickness=1,
                                 highlightbackground='black',
                                 highlightcolor='#4584F1')

            Label(self, text='Student Section:', bg='Whitesmoke', font=('', '10')).place(x=160, y=235)
            student_section = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                                    highlightthickness=1,
                                    highlightbackground='black',
                                    highlightcolor='#4584F1')

            Label(self, text='Student Major:', bg='Whitesmoke', font=('', '10')).place(x=335, y=235)
            student_major = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                                  highlightthickness=1,
                                  highlightbackground='black',
                                  highlightcolor='#4584F1')

            Label(self, text='Course Credits:', bg='Whitesmoke', font=('', '10')).place(x=160, y=295)
            selected_count = StringVar()
            month_cb = ttk.Combobox(self, textvariable=selected_count)
            month_cb['values'] = [a for a in range(1, 11)]
            month_cb['state'] = 'readonly'
            month_cb.current(0)

            score_lbl = Label(self, text='Lesson Score:', bg='Whitesmoke', font=('', '10'))
            score1 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score2 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score3 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score4 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score5 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score6 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score7 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score8 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score9 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                           highlightthickness=1,
                           highlightbackground='black',
                           highlightcolor='#4584F1')
            score10 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')

            lesson_lbl = Label(self, text='Lesson Code:', bg='Whitesmoke', font=('', '10'))
            lesson1 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson2 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson3 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson4 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson5 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson6 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson7 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson8 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson9 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                            highlightthickness=1,
                            highlightbackground='black',
                            highlightcolor='#4584F1')
            lesson10 = Entry(self, bg='white', font=('', '15'), width=14, bd=2, relief='flat',
                             highlightthickness=1,
                             highlightbackground='black',
                             highlightcolor='#4584F1')

            scores = [score1, score2, score3, score4, score5, score6, score7, score8, score9, score10]
            lessons = [lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8, lesson9, lesson10]
            infos = [student_f_name, student_l_name, student_meli_code, student_code, student_section, student_major]

            """
            این تابع برای قرار دادن ورودی های نمره و کد روی صفحه هستند
            """

            def enter_scores(x2=590, x=765):
                y = 75
                for k in (scores + lessons):
                    score_lbl.place_forget()
                    lesson_lbl.place_forget()
                    k.delete(0, 'end')
                    k.place_forget()

                lesson_lbl.place(y=(y - 20), x=x2)
                score_lbl.place(x=x, y=(y - 20))

                for i in scores[0:int(selected_count.get())]:
                    i.place(x=x, y=y)
                    lessons[scores.index(i)].place(y=y, x=x2)
                    y += 60

            """
            پاک کردن متن داخل ورودی ها
            """

            def clear_entry(x):
                if x:
                    for k in (scores + lessons + infos):
                        k.delete(0, 'end')

            Button(self, text='Enter Scores', bg='#DCD0FF', font=('', '10'), command=enter_scores).place(x=340, y=310)

            title.place(x=0, y=-5)

            student_f_name.place(x=160, y=75)
            student_l_name.place(x=335, y=75)
            student_meli_code.place(x=160, y=135)
            student_code.place(x=160, y=195)
            student_section.place(x=160, y=255)
            student_major.place(x=335, y=255)

            month_cb.place(x=160, y=315)

            save_button = Button(self, text='Save', bg='#DCD0FF', font=('', '20'),
                                 command=lambda: [clear_entry(save_data())])
            save_button.place(x=285, y=435)

    """
    صفحه ای برای نشان دادن میانگین اشخاص
    و میانگین مکس و مین
    """

    class average_page(Page):
        def __init__(self, *ar, **ars):
            Page.__init__(self, *ar, **ars)

            """
            تابع پیدا کردن دانش آموز
            برای قابلیت جدا شوندگی
            و قرار دادن پاسخ رو صفحه
            """

            def find_average(average_out):
                code = meli_student.get()
                students = open('./appfiles/Documents/Student/Student_data.txt')
                student_data = students.readlines()
                average = StringVar()
                avg = f'Not found'
                for i in student_data:
                    sp = i.split()
                    if code in sp:
                        if 'Average:' in sp:
                            a = sp[(sp.index('Average:')) + 1]
                            avg = f'FullName: {sp[1]} {sp[2]}\n\n' \
                                  f'Student code: {sp[8]}\n\nMelli code: {sp[5]}\n\nAverage: {a}'
                            break
                        else:
                            avg = f'FullName: {sp[1]} {sp[2]} \n\nStudent code: {sp[8]}\n\n Melli code: {sp[5]}' \
                                  f'\n\nAverage: Without score'
                            break
                    else:
                        avg = f'Student not found'
                average.set(avg)
                average_out.config(textvariable=average)
                average_out.place_forget()
                average_out.place(x=160, y=120)

            """
            تابع نمایش بیشتربن و کمترین میانگین
            طوری کار میکند که اگر دو یا چند دانش آموز برابر بودند همه را نشان دهد
            """

            def max_min(average_max, average_min):
                max_count = 0
                min_count = 20
                max_lst = list()
                min_lst = list()
                max_out = StringVar()
                min_out = StringVar()
                students = open('./appfiles/Documents/Student/Student_data.txt')
                student_data = students.readlines()
                for i in student_data:
                    sp = i.split()
                    if 'Average:' in sp:
                        a = float(sp[(sp.index('Average:')) + 1])
                        info = f'FullName: {sp[1]} {sp[2]} | Student code: {sp[8]} | Melli code: {sp[5]} | Average: {a}'
                        if a > max_count:
                            max_lst.clear()
                            max_lst.append(info)
                            max_count = a
                        elif a == max_count:
                            max_lst.append(info)
                        if a < min_count:
                            min_lst.clear()
                            min_lst.append(info)
                            min_count = a
                        elif a == min_count:
                            min_lst.append(info)
                max_out.set('\n'.join(max_lst))
                min_out.set('\n'.join(min_lst))
                average_max.config(textvariable=max_out)
                average_min.config(textvariable=min_out)
                average_max.place_forget()
                average_min.place_forget()
                average_max.place(x=180, y=350)
                average_min.place(x=180, y=500)

            """
            بخش قرار دادن متن ها دکمه ها و ورودی ها روی صفحه
            """
            title = Label(self, text='Average:', bg='Whitesmoke', font=('', '30'))

            average_out = Label(self, bg='#B9F5F3', font=('', '15'))

            Label(self, text='Enter Student/Melli code:', bg='Whitesmoke', font=('', '10')).place(x=160, y=55)
            meli_student = Entry(self, bg='white', font=('', '15'), width=30, bd=2, relief='flat',
                                 highlightthickness=1,
                                 highlightbackground='black',
                                 highlightcolor='#4584F1')

            Label(self, text='Max Average:', bg='#FBE39F', font=('', '15')).place(x=30, y=350)
            average_max = Label(self, bg='#B9F5F3', font=('', '15'))

            Label(self, text='Min Average:', bg='#FBE39F', font=('', '15')).place(x=30, y=500)
            average_min = Label(self, bg='#B9F5F3', font=('', '15'))

            search = Button(self, text='Search', bg='#DCD0FF', font=('', '13'),
                            command=lambda: [find_average(average_out)])

            refresh = Button(self, text='Refresh', bg='#DCD0FF', font=('', '10'),
                             command=lambda: [max_min(average_max, average_min)])

            title.place(x=0, y=-5)

            meli_student.place(x=160, y=75)
            search.place(y=73, x=550)

            refresh.place(x=60, y=425)

    """
    صفحه پیدا کردن دانش آموز با کلیه ی دیتا
    """

    class find_page(Page):
        def __init__(self, *ar, **ars):
            Page.__init__(self, *ar, **ars)

            """
            تابع جست و جو
            قابلیت جداشوندگی
            و قرار دادن پاسخ رو صفحه
            """

            def find_student(search_out):
                code = meli_student.get()
                students = open('./appfiles/Documents/Student/Student_data.txt')
                student_data = students.readlines()
                infor = StringVar()
                info = f'Student not found'
                for i in student_data:
                    sp = i.split()
                    if code in sp:
                        lesson = ''
                        for f in (sp[16:]):
                            if f in ('|', '||'):
                                lesson += '\n'
                            else:
                                lesson += f + ' '
                        info = f'Fullname: {sp[1]} {sp[2]} \t\t Melli code: {sp[5]} \t\t Student code: {sp[8]} \n\n' \
                               f'Section: {sp[10]} \t \t Major: {sp[12]} \t \t Course Credits: {sp[15]} \n\n' \
                               f'Lesson code and Scores:\n {lesson}'
                        break
                    else:
                        info = f'Student not found'
                infor.set(info)
                search_out.config(textvariable=infor)
                search_out.place_forget()
                search_out.place(x=45, y=120)

            """
            نمایش اشکال روی صفحه
            """
            title = Label(self, text='Search:', bg='Whitesmoke', font=('', '30'))

            Label(self, text='Enter Student/Melli code:', bg='Whitesmoke', font=('', '10')).place(x=160, y=55)
            meli_student = Entry(self, bg='white', font=('', '15'), width=30, bd=2, relief='flat',
                                 highlightthickness=1,
                                 highlightbackground='black',
                                 highlightcolor='#4584F1')

            search_out = Label(self, text='Enter Student/Melli code:', bg='#B9F5F3', font=('', '15'))

            search = Button(self, text='Search', bg='#DCD0FF', font=('', '13'),
                            command=lambda: [find_student(search_out)])

            title.place(x=0, y=-5)

            meli_student.place(x=160, y=75)
            search.place(y=73, x=550)

    """
    صفحه ی نمودار میانگین دانش آموزان
    با کد ملی
    """

    class chart_page(Page):
        def __init__(self, *ar, **ars):
            Page.__init__(self, *ar, **ars)

            """
            گرفتن تمام میانگین های موجود
            به صورت دیکشنری
            با کلید کدملی و ولیو میانگین
            """

            def get_code_avg():
                code_avg = dict()
                students = open('./appfiles/Documents/Student/Student_data.txt')
                student_data = students.readlines()
                for i in student_data:
                    sd = i.split()
                    if 'Average:' in sd:
                        code_avg[sd[5]] = float(sd[(sd.index('Average:')) + 1])

                """
                مرتب کردن اعضا براساس ولیو ها(میانگین ها)
                """
                code_avg = dict(sorted(code_avg.items(), key=lambda item: item[1]))
                students.close()
                return code_avg

            """
            ساخت بک گراند نمودار با سایز 12 در 6 و حساسیت 100
            و افزودن پلات(نقشه نمودار)در بکگراند
            """
            fig = Figure(figsize=(12, 6), dpi=100)
            plt = fig.add_subplot()

            """
            پاک کردن نمودار قبلی جهت رفرش کردن
            برای نمایش در تیکینتر بجای show از draw برای کشیدن استفاده میشود
            """

            def plot():
                plt.clear()

                plt.bar([i for i in range(len(get_code_avg()))], (get_code_avg()).values())
                plt.set_xticks([i for i in range(len(get_code_avg()))], (get_code_avg()).keys())
                plt.set_xlabel('Melli code')
                plt.set_ylabel('Average')

                canvas.draw()

            """
            پیاده کردن بکگراند و نمودار 
            روی صفحه با اضافه کردن تولبار به آن
            """
            canvas = FigureCanvasTkAgg(fig, master=self)

            canvas.get_tk_widget().pack()

            toolbar = NavigationToolbar2Tk(canvas, self)

            toolbar.update()

            canvas.get_tk_widget().pack()

            refresh = Button(self, text='Refresh', bg='#DCD0FF', font=('', '10'), command=plot)
            refresh.pack(side='bottom')

            Label(self, text='Histogram:', bg='#FFFFFF', font=('', '30')).place(x=0, y=-5)

    """
    صفحه ادیت برای حذف تغییر و اضافه در دیتا های موجود
    """

    class edit_page(Page):
        def __init__(self, *ar, **ars):
            Page.__init__(self, *ar, **ars)

            search_lbl = Label(self, bg='#B9F5F3', font=('', '15'))

            """
            جستوجو دانش آموزان
            جدایی پذیر
            """

            def find_student(search_lable):
                search_out = StringVar()
                code = meli_student.get()
                students = open('./appfiles/Documents/Student/Student_data.txt')
                student_data = students.readlines()
                info = f'Student not found'
                selected = ''
                for i in student_data:
                    sp = i.split()
                    if code in sp:
                        selected = i
                        info = f'Student found'
                        break
                    else:
                        info = f'Student not found'
                search_out.set(info)
                search_lable.place(x=160, y=110)
                search_lable.config(textvariable=search_out)
                students.close()

                if selected == '':
                    Label(self, text='\t \t \t \t \n \t \t \t', bg='Whitesmoke', font=('', '500')).place(x=25, y=140)
                return selected

            """
            تابع حذف برای گرفتن خروجی از تابع سرچ و حذف آن از فایل
            """

            def delete_student():
                if messagebox.askokcancel('Warning!!!', 'Press OK to Continue.'):
                    students = open('./appfiles/Documents/Student/Student_data.txt')
                    student_data = students.readlines()
                    selected = find_student(search_lbl)
                    students_new = []
                    for i in student_data:
                        if not i == selected:
                            students_new.append(i)
                        else:
                            infor = f'Student deleted permanently'
                            x = StringVar()
                            x.set(infor)
                            search_lbl.config(textvariable=x)
                    students.close()
                    students = open('./appfiles/Documents/Student/Student_data.txt', 'w')
                    for n in students_new:
                        students.write(n)
                    students.close()
                    Label(self, text='\t \t \t \t \n \t \t \t', bg='Whitesmoke', font=('', '500')).place(x=25, y=140)

            """
            تابع ادیت برای ایجاد تغییرات در ولیو های هر دانش آموز
            """

            def edite():
                student = find_student(search_lbl)
                lesson_score_lbl = Label(self, text='Score:', bg='Whitesmoke', font=('', '10'))
                edite_lbl = Label(self, text='Edite value:', bg='Whitesmoke', font=('', '10'))
                delete_lbl = Label(self, text='Delete score:', bg='Whitesmoke', font=('', '10'))
                lesson_code_lbl = Label(self, text='Lesson code:', bg='Whitesmoke', font=('', '10'))

                if not student == '':
                    student_data = student.split()
                    edite_lbl.place(x=50, y=150)
                    selected_value = StringVar()
                    edite_cb = ttk.Combobox(self, textvariable=selected_value)

                    """
                    ادد کردن گزینه های کمبو باکس با توجه به داده های متغییر هر دانش آموز
                    """

                    def edite_values():
                        edite_value = ['First Name', 'Last Name', 'Section', 'Major']
                        edite_lesson = []
                        cash = []
                        for i in student_data[17:]:
                            if i not in ('||', '|'):
                                cash.append(i)
                            else:
                                edite_lesson.append(cash.copy())
                                cash.clear()
                            if i == '|':
                                break

                        for c in range(len(edite_lesson)):
                            if not edite_lesson == [[]]:
                                edite_value.append(f'Lesson {edite_lesson[c][2]}')
                        return edite_value

                    """
                    روشی برای تعریف آرگیومنت های تیکینتر بعد از ایجاد اشکال
                    """
                    edite_cb['values'] = [a for a in edite_values()]
                    edite_cb['state'] = 'readonly'
                    edite_cb.current(0)
                    edite_cb.place(x=50, y=170)

                    """
                    قرار دادن مقادیر موجود در فایل در ورودی ها جهت نمایش مقدار آنها قبل تغییر
                    """

                    def edit_value():
                        key = selected_value.get()
                        value_en = Entry(self, bg='white', font=('', '10'), width=30, bd=2, relief='flat',
                                         highlightthickness=1,
                                         highlightbackground='black',
                                         highlightcolor='#4584F1')

                        value_en.place(x=50, y=200)

                        if key == 'First Name':
                            value_en.insert('end', f'{student_data[1]}')
                        elif key == 'Last Name':
                            value_en.insert('end', f'{student_data[2]}')
                        elif key == 'Section':
                            value_en.insert('end', f'{student_data[10]}')
                        elif key == 'Major':
                            value_en.insert('end', f'{student_data[12]}')
                        else:
                            l_code = (key.split())[1]
                            value_en.insert('end', f'{student_data[(student_data.index(l_code)) + 2]}')

                        """
                        ذخیره ی موقت ورودی ها در متغیر student_data
                        جهت ذخیره ی کلی آن در آخر
                        """

                        def pre_save():
                            value = value_en.get()
                            trust = True
                            for p in value:
                                if p in Alphabet:
                                    trust = True
                                else:
                                    trust = False
                                    break
                            if key == 'First Name' and trust:
                                student_data[1] = value
                            elif key == 'Last Name' and trust:
                                student_data[2] = value
                            elif key == 'Section' and trust:
                                student_data[10] = value
                            elif key == 'Major' and trust:
                                student_data[12] = value
                            else:
                                trust = True
                                try:
                                    a = float(value)

                                except:
                                    trust = False

                                if trust:
                                    if 0 <= float(value) <= 20:
                                        l_c = (key.split())[1]
                                        student_data[(student_data.index(l_c)) + 2] = value
                                else:
                                    trust = False
                            if trust:
                                value_en.delete(0, 'end')
                                value_en.configure(highlightbackground='black', highlightcolor='#4584F1')
                                value_en.place_forget()
                                save_edited.place_forget()
                            else:
                                value_en.configure(highlightbackground='red', highlightcolor='red')

                        save_edited = Button(self, text='Pre Save', bg='#DCD0FF', font=('', '8'), command=pre_save)
                        save_edited.place(x=135, y=230)

                    selected_edite = Button(self, text='Select', bg='#DCD0FF', font=('', '8'), command=edit_value)
                    selected_edite.place(x=200, y=168)

                """
                اگر دانش آموز نمره ای داش بخش حذف درس را باز کن
                """
                if not find_student(search_lbl) == '':
                    if edite_values()[4:]:
                        delete_lbl.place(x=525, y=150)
                        selected_score = StringVar()
                        delete_cb = ttk.Combobox(self, textvariable=selected_score)
                        delete_cb['values'] = [a for a in edite_values()[4:]]
                        delete_cb['state'] = 'readonly'
                        delete_cb.current(0)
                        delete_cb.place(x=525, y=170)

                        """
                        تابعی برای حذف درس های دانش آموز
                        ادد کردن درس ها در کمبو باکس 
                        اگر درسی نبود بگه نمره نداره
                        """

                        def delete_value():
                            l_code = delete_cb.get()
                            score = StringVar()
                            Label(self, text='\t \t \t', bg='Whitesmoke', font=('', '10')).place(x=525, y=200)
                            if not l_code == '':
                                l_c = (l_code.split())[1]
                                score.set(f'Score: {student_data[(student_data.index(l_c)) + 2]}')
                            else:
                                score.set('Without Score')
                            score_lbl = Label(self, textvariable=score, bg='#B9F5F3', font=('', '10'))
                            score_lbl.place(x=525, y=200)

                            """
                            حذف موقت جهت ذخیره ی فایل در آخر
                            """

                            def pre_delete():

                                if 'Lesson' in student_data:

                                    if student_data[student_data.index(l_c) + 4] == 'Average:':
                                        del student_data[(student_data.index(l_c) + 3)]
                                        del student_data[(student_data.index(l_c) - 2):(student_data.index(l_c) + 3)]
                                    else:
                                        del student_data[16:]
                                        student_data[15] = '0'

                                    delete_cb.configure(values=[a for a in edite_values()[4:]])
                                    edite_cb.configure(values=[a for a in edite_values()])

                                delete_cb.set('')
                                score_lbl.place_forget()
                                save_deleted.place_forget()

                            if not score.get() == 'Without Score':
                                save_deleted = Button(self, text='Pre Delete', bg='#DCD0FF', font=('', '8'),
                                                      command=pre_delete)
                                save_deleted.place(x=610, y=230)

                        selected_delete = Button(self, text='Select', bg='#DCD0FF', font=('', '8'),
                                                 command=delete_value)
                        selected_delete.place(x=675, y=168)

                    """
                    اضافه کردن درس به دانش آموز
                    """

                    def add_lesson():
                        """
                        راستی آزمایی ورودی ها
                        """
                        code = lesson_code_en.get()
                        trust = False
                        for i in code:
                            if i in numbers and i not in ('.', '_', '-'):
                                trust = True
                            else:
                                trust = False
                                break

                        score = lesson_score_en.get()
                        score_trust = False
                        for i in score:
                            if i in numbers and i not in ('_', '-'):
                                score_trust = True
                            else:
                                score_trust = False
                                break

                        if score == '':
                            score_trust = False
                        elif not 0 <= float(score) <= 20:
                            score_trust = False

                        """
                        اگر همچی درست بود
                        آنها را در فایل موقت سیو میکند
                        """
                        if trust and score_trust:
                            if int(student_data[15]) == 0:
                                new_data = f'| Lesson Code: {code} Score: {score} | Average: 0'
                                for a in new_data.split():
                                    student_data.append(a)
                            else:
                                new_data = f'|| Lesson Code: {code} Score: {score}'
                                del student_data[(student_data.index('Average:') - 1):]
                                for b in new_data.split():
                                    student_data.append(b)
                                for c in ('|', 'Average:', '0'):
                                    student_data.append(c)
                            lesson_code_en.configure(highlightbackground='green', highlightcolor='#4584F1')
                            lesson_score_en.configure(highlightbackground='green', highlightcolor='#4584F1')

                            lesson_code_en.delete(0, 'end')
                            lesson_score_en.delete(0, 'end')

                            """
                            برای رفرش کمبو باکش ها بعد تغییرات
                            """
                            delete_cb.configure(values=[a for a in edite_values()[4:]])
                            edite_cb.configure(values=[a for a in edite_values()])
                        else:
                            lesson_code_en.configure(highlightbackground='red', highlightcolor='red')
                            lesson_score_en.configure(highlightbackground='red', highlightcolor='red')

                    lesson_code_lbl.place(x=50, y=300)
                    lesson_code_en = Entry(self, bg='white', font=('', '10'), width=30, bd=2, relief='flat',
                                           highlightthickness=1,
                                           highlightbackground='black',
                                           highlightcolor='#4584F1')
                    lesson_code_en.place(x=50, y=320)

                    lesson_score_lbl.place(x=300, y=300)
                    lesson_score_en = Entry(self, bg='white', font=('', '10'), width=30, bd=2, relief='flat',
                                            highlightthickness=1,
                                            highlightbackground='black',
                                            highlightcolor='#4584F1')
                    lesson_score_en.place(x=300, y=320)

                    pre_add = Button(self, text='Pre Add', bg='#DCD0FF', font=('', '8'), command=add_lesson)
                    pre_add.place(x=530, y=319)

                    """
                    ذخیره ی نهایی student_data در فایل اصلی
                    با فرم مشخس
                    و سوال اطمینان که در تابع دیلیت میباشد
                    """

                    def save():
                        if 'Average:' in student_data:
                            count = 0
                            grade = 0
                            l_en = 0
                            for s in student_data:
                                if s == 'Score:':
                                    grade += float(student_data[l_en + 1])
                                    count += 1
                                l_en += 1
                            student_data[15] = str(count)
                            student_data[(student_data.index('Average:')) + 1] = str(grade / count)

                        delete_student()
                        students = open('./appfiles/Documents/Student/Student_data.txt', 'a')
                        student_data.append('\n')
                        for a in student_data:
                            if not a == '\n':
                                students.write(a + ' ')
                            else:
                                students.write(a)
                        y = StringVar()
                        y.set('Student Edited Permanently')
                        search_lbl.config(textvariable=y)

                    save_all = Button(self, text='Save All', bg='#DCD0FF', font=('', '20'), command=save)
                    save_all.place(x=425, y=450)

            """
            محل ساخت و قرار اشکال
            """
            title = Label(self, text='Edite:', bg='Whitesmoke', font=('', '30'))

            Label(self, text='Enter Student/Melli code:', bg='Whitesmoke', font=('', '10')).place(x=160, y=55)
            meli_student = Entry(self, bg='white', font=('', '15'), width=30, bd=2, relief='flat',
                                 highlightthickness=1,
                                 highlightbackground='black',
                                 highlightcolor='#4584F1')

            select = Button(self, text='Select for edite', bg='#DCD0FF', font=('', '13'), command=edite)
            delete = Button(self, text='Delete student', bg='#DCD0FF', font=('', '13'), command=delete_student)

            title.place(x=0, y=-5)

            meli_student.place(x=160, y=75)

            select.place(y=73, x=550)
            delete.place(y=73, x=700)

    """
    صفحه ای جهت نشان دادن اطلاعات شخصی که وارد برنامه شده
    """

    class profile_page(Page):
        def __init__(self, *ar, **ars):
            Page.__init__(self, *ar, **ars)

            """
            با خواندن فایل trust_login که جهت راستی آزمایی ورود به برنامه که
            در صفحه لاگین فرم اول ساخته شده
            """

            def read_data():
                """
                با توجه به فایل اطلاعات شخص رو از فایل های دیگر میخواند
                وبعد فایل را پاک میکند
                """
                try:

                    login_trust = open('./appfiles/Documents/login_trust.txt')
                    trust_login = login_trust.readline()
                    login_trust.close()
                    os.remove('./appfiles/Documents/login_trust.txt')
                    user_pass_mail = open('./appfiles/Documents/userpass.txt').readlines()
                    user_data = open('./appfiles/Documents/userdata.txt').readlines()
                    person_data = user_data[int(trust_login)].split()
                    person_pass = user_pass_mail[int(trust_login)].split()

                    f_name_str = StringVar()
                    l_name_str = StringVar()
                    mail_str = StringVar()
                    meli_code_str = StringVar()
                    user_name_str = StringVar()
                    birthday_str = StringVar()
                    password_str = StringVar()

                    f_name_str.set(person_data[1])
                    l_name_str.set(person_data[2])
                    mail_str.set(person_data[4])
                    meli_code_str.set(person_data[9])
                    user_name_str.set(person_pass[0])
                    birthday_str.set(person_data[6])
                    password_str.set(person_pass[1])

                    Label(self, textvariable=f_name_str, bg='Whitesmoke', font=('', '20')).place(x=320, y=100)
                    Label(self, textvariable=l_name_str, bg='Whitesmoke', font=('', '20')).place(x=680, y=100)
                    Label(self, textvariable=mail_str, bg='Whitesmoke', font=('', '20')).place(x=240, y=180)
                    Label(self, textvariable=meli_code_str, bg='Whitesmoke', font=('', '20')).place(x=325, y=260)
                    Label(self, textvariable=user_name_str, bg='Whitesmoke', font=('', '20')).place(x=325, y=340)
                    Label(self, textvariable=birthday_str, bg='Whitesmoke', font=('', '20')).place(x=295, y=420)
                    Label(self, text='********', bg='Whitesmoke', font=('', '20')).place(x=320, y=508)
                    password_show = Label(self, textvariable=password_str, bg='Whitesmoke', font=('', '20'))

                    show_pass_button = Button(self, text='Show', bg='#DCD0FF', font=('', '10'), command=lambda:
                    [password_show.place(x=320, y=500), show_pass_button.destroy()])

                    show_pass_button.place(x=600, y=505)

                    """
                    اگر شخص بدون مجوز لاگاین وارد برناممه شود برنامه با یک خطا بسته شده و فرم لاگ این بالا میآید
                    """
                except:
                    messagebox.showinfo(title='Error', message='Please Log in')
                    frm.destroy()
                    enter_part()

            title = Label(self, text='Profile:', bg='Whitesmoke', font=('', '30'))
            f_name = Label(self, text='FirstName:', bg='Whitesmoke', font=('', '20'))
            l_name = Label(self, text='LastName:', bg='Whitesmoke', font=('', '20'))
            mail = Label(self, text='Mail:', bg='Whitesmoke', font=('', '20'))
            meli_code = Label(self, text='Melli Code:', bg='Whitesmoke', font=('', '20'))
            user_name = Label(self, text='UserName:', bg='Whitesmoke', font=('', '20'))
            birthday = Label(self, text='Birthday:', bg='Whitesmoke', font=('', '20'))
            password = Label(self, text='PassWord:', bg='Whitesmoke', font=('', '20'))

            """
            ساخت تابع ای برای بستن فرم و برگشت به صفحه لاگین
            """

            def log_out():
                if messagebox.askokcancel('Log out?', 'Press OK to Log out.'):
                    frm.destroy()
                    enter_part()

            logout_button = Button(self, text='Log out', bg='#DCD0FF', font=('', '20'), command=log_out)

            title.place(x=0, y=-5)
            f_name.place(x=175, y=100)
            l_name.place(x=535, y=100)
            mail.place(x=175, y=180)
            meli_code.place(x=175, y=260)
            user_name.place(x=175, y=340)
            birthday.place(x=175, y=420)
            password.place(x=175, y=500)

            logout_button.pack(side='bottom')

            read_data()

    """
    ساخت صفحات فرم دوم
    """

    class Main(Frame):
        def __init__(self, *ar, **ars):
            Frame.__init__(self, *ar, **ars)

            p1 = enter_data_page(self)
            p2 = average_page(self)
            p3 = find_page(self)
            p4 = chart_page(self)
            p5 = edit_page(self)
            p6 = profile_page(self)

            p4.configure(bg='#FFFFFF')

            for p in (p1, p2, p3, p5, p6):
                p.configure(bg='Whitesmoke')

            but = Frame(self)
            con = Frame(self)

            but.pack(side='left', fill='y', expand=False)
            con.pack(side='top', fill='both', expand=True)

            p1.place(in_=con, x=0, y=0, relheight=1, relwidth=1)
            p2.place(in_=con, x=0, y=0, relheight=1, relwidth=1)
            p3.place(in_=con, x=0, y=0, relheight=1, relwidth=1)
            p4.place(in_=con, x=0, y=0, relheight=1, relwidth=1)
            p5.place(in_=con, x=0, y=0, relheight=1, relwidth=1)
            p6.place(in_=con, x=0, y=0, relheight=1, relwidth=1)

            """
            تابعی برای تغییر رنگ دکمه ها
            """

            def change_color(button):
                for i in (b1, b2, b3, b4, b5, b6):
                    i.configure(bg='#DCD0FF')
                button.configure(bg='#6ca5eb')

            def exit_config():
                if messagebox.askokcancel('Exit', 'Press OK to Exit.'):
                    frm.destroy()

            b1 = Button(but, text='Register', bg='#DCD0FF', font=('', '15'),
                        command=lambda: [change_color(b1), p1.show()])
            b2 = Button(but, text='Average', bg='#DCD0FF', font=('', '15'),
                        command=lambda: [change_color(b2), p2.show()])
            b3 = Button(but, text='Search', bg='#DCD0FF', font=('', '15'),
                        command=lambda: [change_color(b3), p3.show()])
            b4 = Button(but, text='Histogram', bg='#DCD0FF', font=('', '15'),
                        command=lambda: [change_color(b4), p4.show()])
            b5 = Button(but, text='Edit', bg='#DCD0FF', font=('', '15'),
                        command=lambda: [change_color(b5), p5.show()])
            b6 = Button(but, text='Profile', bg='#DCD0FF', font=('', '15'),
                        command=lambda: [change_color(b6), p6.show()])
            b7 = Button(but, text='Exit', bg='#DCD0FF', font=('', '15'),
                        command=exit_config)

            b1.pack(fill='both')
            b2.pack(fill='both')
            b3.pack(fill='both')
            b4.pack(fill='both')
            b5.pack(fill='both')
            b6.pack(fill='both')
            b7.pack(side='bottom', fill='both')

            change_color(b6)
            p6.show()

    frm = Tk(className='Student organizer')
    main = Main(frm)
    main.pack(side='top', fill='both', expand=True)
    frm.geometry('1120x680')
    frm.mainloop()


# ----------------------------------------------------------------------------------------------------------------------
"""
دستور شروع برنامه :)
"""
enter_part()