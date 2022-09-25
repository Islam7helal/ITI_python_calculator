from tkinter import *



def validateLogin():

    name=username.get()
    passs=password.get()
    
    print("the username is :"+name)
    print("the password is :"+passs)
    
    
    if(name == "admin") and (passs == "admin"):
        window1.destroy()
        import CALCULATOR
    
    username.set("")
    password.set("")
  
#######################################

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 

	
#////////////////////////////////////////////////////////////

#the main window
window1 = Tk(className="log in to calculator")
window1.geometry('400x200')


#frame for login
frame = Frame(window1)
frame.pack(expand=True) 

#username label and text entry box
usernameLabel = Label(frame, text="User Name").grid(row=0, column=0,padx=10,pady=10)
username = StringVar()
usernameEntry = Entry(frame, textvariable=username).grid(row=0, column=1,padx=10,pady=10)  

#password label and password entry box
passwordLabel = Label(frame,text="Password").grid(row=1, column=0,padx=10,pady=10)  
password = StringVar()
passwordEntry = Entry(frame, textvariable=password, show='*').grid(row=1, column=1,padx=10,pady=10)  

#login button
loginButton = Button(frame, text="Login", command=validateLogin).grid(row=2, rowspan=2,columnspan=3,sticky='ew',padx=10,pady=10,ipadx=10,ipady=10)  

                                                                                                                                 

window1.mainloop()


