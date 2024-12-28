from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk


class LoginPage:
    def __init__(self, root):
        self.window = root
        self.window.title("Login")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="white")

        # Design Elements for Login
        self.frame1 = Frame(self.window, bg="white")
        self.frame1.place(x=0, y=0, width=450, relheight=1)
        self.bg_img = Image.open("C:\\Users\\hp\\Desktop\\Pharmacy management System\\logo.jpg")
        self.logo_img = ImageTk.PhotoImage(self.bg_img)
        self.logo_label = Label(self.frame1, image=self.logo_img, bg="white")
        self.logo_label.place(x=100, y=200)

        # Frame for Login Form
        self.frame2 = Frame(self.window, bg="teal")
        self.frame2.place(x=450, y=0, relwidth=1, relheight=1)
        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140, y=150, width=500, height=450)

        # Login Form Fields
        self.email_label = Label(self.frame3, text="Email Address", font=("Times New Roman", 20, "bold"), bg="white", fg="black").place(x=50, y=40)
        self.email_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.email_entry.place(x=50, y=80, width=300)
        
        self.password_label = Label(self.frame3, text="Password", font=("Times New Roman", 20, "bold"), bg="white", fg="black").place(x=50, y=120)
        self.password_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray", show="*")
        self.password_entry.place(x=50, y=160, width=300)

        # Buttons
        self.forgotten_pass = Button(self.frame3, text="Forgotten password?", command=self.forgot_func,
                                      font=("times new roman", 10, "bold"), bd=0,
                                      cursor="hand2", bg="white", fg="teal").place(x=220, y=200, width=150)
        
        self.login_button = Button(self.frame3, text="Log In", command=self.login_func,
                                   font=("times new roman", 17, "bold"), bd=0,
                                   cursor="hand2", bg="teal", fg="white").place(x=50, y=240, width=300)
        
        self.create_button = Button(self.frame3, text="Create New Account", command=self.redirect_window,
                                    font=("times new roman", 18, "bold"), bd=0,
                                    cursor="hand2", bg="teal", fg="white").place(x=50, y=320, width=300)

    def login_func(self):
        if self.email_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
            return
        
        try:
            connection = mysql.connector.connect(host="localhost", user="root",
                                                 password="case1234tor",
                                                 database="student_database")
            cur = connection.cursor()
            cur.execute("SELECT * FROM student_register WHERE email=%s AND password=%s",
                        (self.email_entry.get(), self.password_entry.get()))
            row = cur.fetchone()
            
            if row is None:
                messagebox.showerror("Error!", "Invalid USERNAME & PASSWORD", parent=self.window)
            else:
                messagebox.showinfo("Success","Login successful" ,parent=self.window)
                self.reset_fields()  
            
            connection.close()  
            self.window.destroy()
            
            pharmacy_root = Tk()
            from pharma import PharmacyManagementSystem  
            PharmacyManagementSystem(pharmacy_root)  
            pharmacy_root.mainloop()

        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def forgot_func(self):
        if self.email_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your Email Id", parent=self.window)
            return
        
        try:
            connection = mysql.connector.connect(host="localhost", user="root",
                                                 password="case1234tor",
                                                 database="student_database")
            cur = connection.cursor()
            cur.execute("SELECT * FROM student_register WHERE email=%s", (self.email_entry.get(),))
            row = cur.fetchone()
            
            if row is None:
                messagebox.showerror("Error!", "Email Id doesn't exist", parent=self.window)
                return
            
            connection.close()
            
            # Setup for password reset form
            self.root = Toplevel()
            self.root.title("Forget Password?")
            self.root.geometry("400x440+450+200")
            self.root.config(bg="white")
            self.root.focus_force()
            self.root.grab_set()

            title3 = Label(self.root, text="Change your password",
                           font=("times new roman", 20, "bold"), bg="white").place(x=10,y=10)
            title4 = Label(self.root,text="It's quick and easy",
                           font=("times new roman", 12), bg="white").place(x=10,y=45)
            
            title5 = Label(self.root,text="Select your question",
                           font=("times new roman", 15,"bold"),bg="white").place(x=10,y=85)

            self.sec_ques = ttk.Combobox(self.root,font=("times new roman",13),state='readonly',justify=CENTER)
            self.sec_ques['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace","Your favorite movie")
            self.sec_ques.place(x=10,y=120,width=270)
            self.sec_ques.current(0)

            title6 = Label(self.root,text="Answer",
                           font=("times new roman",15,"bold"),bg="white").place(x=10,y=160)
            
            self.ans = Entry(self.root,font=("arial"))
            self.ans.place(x=10,y=195,width=270)

            title7 = Label(self.root,text="New Password",
                           font=("times new roman",15,"bold"),bg="white").place(x=10,y=235)

            self.new_pass = Entry(self.root,font=("arial"))
            self.new_pass.place(x=10,y=270,width=270)

            submit_button = Button(self.root,text="Submit",
                                   command=self.change_pass,
                                   font=("times new roman",18,"bold"),
                                   bd=0,cursor="hand2",
                                   bg="teal",
                                   fg="white").place(x=60,y=340,width=270)

        except Exception as e:
            messagebox.showerror("Error", f"{e}")

    def change_pass(self):
        if (self.email_entry.get() == "" or 
                self.sec_ques.get() == "Select" or 
                self.new_pass.get() == ""):
                
                messagebox.showerror("Error!", "Please fill in all fields correctly", parent=self.root)
                return

        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="root",
                                                 password="case1234tor",
                                                 database="student_database")
            
            cur = connection.cursor()
            
            cur.execute("SELECT * FROM student_register WHERE email=%s AND question=%s AND answer=%s",
                        (self.email_entry.get(), 
                         self.sec_ques.get(), 
                         self.ans.get()))
            
            row = cur.fetchone()
            
            if row is None:
                messagebox.showerror("Error!", "Invalid information", parent=self.root)
                return
            
            cur.execute("UPDATE student_register SET password=%s WHERE email=%s",
                        (self.new_pass.get(), 
                         self.email_entry.get()))
            
            connection.commit()
            
            messagebox.showinfo("Successful","Password has been changed successfully", parent=self.root)
            
            connection.close()
            
            self.reset_fields()
            
            self.root.destroy()

        except Exception as er:
             messagebox.showerror("Error!", f"{er}", parent=self.root)

    def redirect_window(self):
        from signup_screen import SignUp  # Local import to avoid circular dependency
        self.window.destroy()
        
        root = Tk()
        obj = SignUp(root)  
        root.mainloop()

    def reset_fields(self):
        """Reset entry fields."""
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)

# Main execution block
if __name__ == "__main__":
    pharmacy_root = Tk()
    login_page_instance = LoginPage(pharmacy_root)  
    pharmacy_root.mainloop()
