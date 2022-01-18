from tkinter import *
from tkinter import messagebox
import random

class User_Register_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Billing Software")

        # ====================Variables========================#
        self.user_name = StringVar()
        self.user_pwd = StringVar()

#===================================
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Register User",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        F1 = LabelFrame(text = "New User",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        cname_lbl = Label(F1,text="User Name/Email",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.user_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        cphon_lbl = Label(F1,text = "Password",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.user_pwd)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        bill_btn = Button(F1, text="Save", command=self.save, bd=7, relief=GROOVE, font=("times new roman", 12, "bold"), bg=bg_color,
                          fg=fg_color)
        bill_btn.grid(row=0, column=6, ipady=5, padx=60, ipadx=19, pady=5)

    def save(self):
        if len(self.user_name.get()) == 0 or len(self.user_pwd.get()) == 0:
            messagebox.showerror("Error", "User name/Password cannot be empty")
        else:
            user_file = open("./user_details/" + self.user_name.get(), "w")
            user_details = self.user_name.get() + "|" + self.user_pwd.get()
            user_file.write(user_details)
            user_file.close()
            messagebox.showinfo("Information", "Registration Successful")



root = Tk()
object = User_Register_App(root)
root.mainloop()
