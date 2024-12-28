from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image , ImageTk
from login_screen import LoginPage


class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="black")

        # Design Elements for SignUp
        self.frame1 = Frame(self.window, bg="white")
        self.frame1.place(x=0, y=0, width=450, relheight=1)

        self.frame2 = Frame(self.window, bg="teal")
        self.frame2.place(x=450, y=0, relwidth=1, relheight=1)

        frame = Frame(self.frame2, bg="white")
        frame.place(x=140, y=120, width=500, height=540)
        
        self.bg_img = Image.open("C:\\Users\\hp\\Desktop\\Pharmacy management System\\logo.jpg")
        self.logo_img = ImageTk.PhotoImage(self.bg_img)   
        self.logo_label = Label(self.frame1, image=self.logo_img, bg="white")
        self.logo_label.place(x=100, y=200) 

        self.frame2 = Frame(self.window, bg="white")
        self.frame1.place(x=0, y=0, width=450, relheight=1)

        title1 = Label(frame, text="Sign Up", font=("times new roman", 25, "bold"), bg="white").place(x=20, y=10)
        # Fields for SignUp
        self.fname_txt = Label(frame , text="First Name" ,font=("times new roman", 20, "bold"), bg="white").place(x=10, y=60)
        self.fname_txt = Entry(frame, font=("arial"))
        self.fname_txt.place(x=40, y=100, width=270)
        self.lname_txt = Label(frame , text="Last Name" ,font=("times new roman", 20, "bold"), bg="white").place(x=10, y=130)
        self.lname_txt = Entry(frame, font=("arial"))
        self.lname_txt.place(x=40, y=170, width=270)
        self.email_txt = Label(frame , text="Email" ,font=("times new roman", 20, "bold"), bg="white").place(x=10, y=200)
        self.email_txt = Entry(frame, font=("arial"))
        self.email_txt.place(x=40, y=240, width=270)
        self.password_txt = Label(frame , text="Password" ,font=("times new roman", 20, "bold"), bg="white").place(x=10, y=270)
        self.password_txt = Entry(frame, font=("arial"))
        self.password_txt.place(x=40, y=310, width=270)
        self.question_txt = Label(frame , text="Security Question" ,font=("times new roman", 20, "bold"), bg="white").place(x=7, y=340)
        self.question_txt = ttk.Combobox(frame, font=("arial"), state="readonly", width=20)
        self.question_txt['values'] = ("Select", "What's your pet name?", "Your first teacher name", "Your birthplace", "Your favorite movie")
        self.question_txt.place(x=20, y=380)
        self.question_txt.current(0)
        self.answer_txt = Label(frame , text="Answer" ,font=("times new roman", 20, "bold"), bg="white").place(x=7, y=410)
        self.answer_txt = Entry(frame, font=("arial"))
        self.answer_txt.place(x=20, y=450, width=270)

        self.submit_button = Button(frame, text="Submit", command=self.signup_func, font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="teal", fg="white").place(x=70, y=490, width=340)

    def signup_func(self):
        if self.fname_txt.get() == "" or self.lname_txt.get() == "" or self.email_txt.get() == "" or self.password_txt.get() == "" or self.question_txt.get() == "Select" or self.answer_txt.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.window)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", user="root", password="case1234tor", database="student_database")
                cur = connection.cursor()
                cur.execute("INSERT INTO student_register (f_name, l_name, email, password, question, answer) VALUES (%s, %s, %s, %s, %s, %s)",
                            (self.fname_txt.get(), self.lname_txt.get(), self.email_txt.get(), self.password_txt.get(), self.question_txt.get(), self.answer_txt.get()))
                connection.commit()
                messagebox.showinfo("Success", "Sign Up Successful", parent=self.window)
                connection.close()
                self.window.destroy()  
                login_root = Tk()  
                LoginPage(login_root)  
                login_root.mainloop()
            except Exception as e:
                messagebox.showerror("Error", f"{e}", parent=self.window)



