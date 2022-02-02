from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.scrolledtext as st
from PIL import ImageTk, Image
from find_people import *

class App(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("InstagramBot") #Change!
        self.geometry("600x600")

        self.username = StringVar()
        self.password = StringVar()
        # photo = PhotoImage(file="./photos/robo2.png")
        # img = Label(self,image=photo)
        # img.place(relx=0.5, rely=0.5, anchor=CENTER)

        login_frame = Frame()
        #####-LOGIN FRAME-######
        self.normal_sign = Message(master = login_frame, text= "Please enter your email & password to sign in.\n",width= 250,font = ("calibre",15))
        self.normal_sign_button = Button(master = login_frame,text="Sign In",command = self.program)
        self.tx1 = Label(master=login_frame,text = "Username")
        self.tx2 = Label(master=login_frame,text = "Password")
        self.name_entry = Entry(master = login_frame,textvariable = self.username, font=('calibre',10,'normal'),width= 40)
        self.passw_entry= Entry(master = login_frame, textvariable = self.password, font = ('calibre',10,'normal'), show = '*',width= 40)
        self.normal_sign.pack()
        self.tx1.pack()
        self.name_entry.pack()
        self.tx2.pack()
        self.passw_entry.pack()
        self.normal_sign_button.pack(pady=10)
        ########################
        login_frame.place(relx=0.5,rely=0.4,anchor=CENTER)

        CREATOR = Label(self,text = "Creator Arda Numanoğlu")
        CREATOR.place(relx=0.5,rely=0.97,anchor=CENTER)


    def program(self):
        
        self.tx1.destroy(),self.tx2.destroy(),self.name_entry.destroy(),self.passw_entry.destroy(),self.normal_sign.destroy(),self.normal_sign_button.destroy()
        self.processing = Label(self,text = "Processing...")
        self.processing.place(relx = 0.5, rely= 0.4, anchor=CENTER)
        self.update() ###JESUS
        self.process_data()
        

    def process_data(self):
        scrape = InstaBot("firefox")
        username = self.username.get()
        password = self.password.get()
        scrape.login(username,password)
        sleep(30)
        scrape.go_profile()
        sleep(5)
        scrape.get_followers()
        sleep(5)
        scrape.get_followings()
        users1,users2 = scrape.find_difference()
        # PROCESSİNGİ KALDIR
        self.processing.destroy()
        self.open_list(users1,users2)
        


    def on_close(self):
        response= messagebox.askyesno("Exit","Are you sure you want to exit?")
        if response:
            self.destroy()

    def open_list(self,users1,users2):
        # self = Toplevel(self)
        # self.title("Results")
        # self.geometry("700x500")

        instruction1 = Label(self, text = "Users who do not follow you back",font = ("FreeSans",10))
        instruction2 = Label(self, text = "Users who you do not follow back",font = ("FreeSans",10))
        instruction1.place(relx=0.25,rely=0.1,anchor=CENTER)
        instruction2.place(relx=0.75,rely=0.1,anchor=CENTER)

        text_area1 = st.ScrolledText(self,
                            width = 20, 
                            height = 15, 
                            font = ("Times New Roman",
                                    15))
        text_area1.place(relx=0.25,rely=0.5,anchor=CENTER)
        text_area1.insert(INSERT,
            "--> "+ "\n--> ".join(users1))
        # Making the text read only
        text_area1.configure(state ='disabled')

        text_area2 = st.ScrolledText(self,
                            width = 20, 
                            height = 15, 
                            font = ("Times New Roman",
                                    15))
        text_area2.place(relx=0.75,rely=0.5,anchor=CENTER)
        text_area2.insert(INSERT,
            "--> "+ "\n--> ".join(users2))
        # Making the text read only
        text_area2.configure(state ='disabled')

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW",app.on_close)
    app.mainloop()





        #frames = [PhotoImage(file='./sand-clock-loader.gif',format = 'gif -index %i' %(i)) for i in range(31)]

        # def update(ind):
        #     frame = frames[ind]
        #     ind += 1
        #     print(ind)
        #     if ind>30: #With this condition it will play gif infinitely
        #         ind = 0
        #     label.configure(image=frame)
        #     self.after(100, update, ind)

        # label = Label(self)
        # label.pack()
        # self.after(0, update, 0)