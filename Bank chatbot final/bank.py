import  ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox
import datetime
import time

questions=[
    "1) how should i transfer the amount to other bankaccounts?",
    "2) i need to see bank balance in my account?",
    "3) can you show me recent transactions on my credit card?",
    "4) How do I transfer money between my accounts?",
    "5) What is the interest rate on a specific savings account?",
    "6) How can I reset my online banking password?",
    "7) can i open a new checking account online?",
    "8) what are the requirements for getting a personal loan?",
    "9) How do I report a lost or stolen credit card?",
    "10) can you help me set up automatic bill payments?",
    "11) Are there any special offers or promotions available for credit card holders?"
]


def response():
    global ans
    res=entry_str.get()
    if res.lower()=="2) i need to see bank balance in my account?":
        ans=( "Bank Balance in the account is Rs. ₹34243.23")
    
    elif res.lower()=="1) how should i transfer the amount to other bankaccounts?":
        ans=("""However you choose to transfer money, you’ll usually 
             need the following details of the person or organisation
             you’re paying:
            *The date you want the payment to be made.
            *Name of the person or business you’re
            paying.
            *six-digit sort code of the account you’re
            paying.
            *Eight-digit account number of the account
            you’re paying.
            *A payment reference (often your name or 
            customer number) to let them know the 
            money came from you.
            *Sometimes you’ll need the name and 
            address of the bank you’re sending 
            the money to. This helps them to 
            check that sort code is right.""")
    elif res.lower()=="3) can you show me recent transactions on my credit card?":
        ans=("""Sure! Here are the most recent 
            transactions on your credit card: 
            Transaction 1: ₹550 -Grocery Store, 
             Transaction 2: ₹250 - Gas Station,
             Transaction 3: ₹100 - Online Retailer.""")
    elif res.lower()=="4) how do i transfer money between my accounts?":
        ans=(""" To transfer money between your accounts,
             you can use our online banking platform. 
             Simply log in, navigate to the 'Transfer Funds' section,
             and follow the instructions""")
    elif res.lower()=="5) what is the interest rate on a specific savings account?":
        ans=("""The current interest rate on our High-Yield Savings Account is 2.5% APY.""")
    elif res.lower()=="6) how can i reset my online banking password?":
        ans=("""If you need to reset your online banking password, click on the 'Forgot Password'
             link on the login page. You'll receive instructions to reset your password via email 
             or text message.""")
    elif res.lower()=="7) can i open a new checking account online?":
        ans=("""yes, you can open a new checking account online.
             Visit our website, go to the 'Open an Account' section, 
             and follow the steps to apply""")
    elif res.lower()=="8) what are the requirements for getting a personal loan?":
        ans=("""To apply for a personal loan, you'll need to meet certain requirements,
             including a good credit score and proof of income. 
             Please visit our nearest branch or apply online for more information""")
    elif res.lower()=='9) how do i report a lost or stolen credit card?':
        ans=("""I'm sorry to hear that your credit card is lost or stolen.
             Please report it immediately by calling our 24/7 customer 
             service hotline at [customer service number].""")
    elif res.lower()=='10) can you help me set up automatic bill payments?':
        ans=("""Sure! We can help you set up automatic bill payments.
             Log in to your online banking account, navigate to the 
             'Bill Pay' section, and follow the steps to set up recurring payments.""")
    elif res.lower()=='11) are there any special offers or promotions available for credit card holders?':
        ans=(""""As a valued credit card holder, you are eligible for exclusive offers and promotions.
             Please visit our website or check your email for the latest deals.""")
    
    
    else:
        ans = "Sorry, I don't understand the question."
	    
    typing_speed = 0.05  
    typing_delay = 0.5   
    
    output_label.config(text='')
    window.update()  
    
    for char in ans:
        output_label.config(text=output_label.cget('text') + char)
        window.update()  
        time.sleep(typing_speed)

    
    time.sleep(typing_delay)

    return ans
    

def update_output_label():
    response()
    output_label.config(text=ans) 
    
def clear():
    output_label.config(text='')
    entry_str.set("")
    
def show_questions():
    for question in questions:
        listbox.insert(tk.END, question)

def hide_questions():
    listbox.delete(0, tk.END)


def on_list_select(event):
    selected_item = listbox.get(listbox.curselection())
    entry.delete(0, tk.END)  # Clear the entry before inserting new text
    entry.insert(tk.END, selected_item)

def submit_feedback():
    name=feedback_name_entry.get().strip()
    comments = feedback_entry.get().strip()
    rating = rating_var.get()
   
    
    with open("feedback.txt", "a") as file:
        file.write(f"Names: {name}\n")
        file.write(f"Rating: {rating}\n")
        file.write(f"Comments: {comments}\n")
        file.write("\n")
    feedback_entry.delete("0","end")
    rating_var.set(0)
    feedback_name_entry.delete("0","end")
    messagebox.showinfo("Thank You!", "Thank you for your feedback!")
    
def update_clock():
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    window.after(1000, update_clock)
    
    
window=ttk.Window(themename='solar')
window.title("Bank ChatBot")
window.geometry('1550x600')
photo = tk.PhotoImage(file = "bank.png")
window.iconphoto(False, photo)


chatbot_photo = tk.PhotoImage(file="pngegg.png")
chatbot_label = ttk.Label(master=window, image=chatbot_photo)
chatbot_label.pack(side='left', padx=5)

label_ask=ttk.Label(master=window,text="ASK HERE",font='Calibri 24 bold')
label_ask.pack()
input_frame=ttk.Frame(master=window)
clock_label = ttk.Label(master=window, text="", font=("Helvetica", 24))
clock_label.pack(side='right',anchor='n', padx=5, pady=5)
update_clock()
entry_str=tk.StringVar()
entry=ttk.Entry(master=input_frame,textvariable=entry_str)
button=ttk.Button(master=input_frame,text='Enter',command= update_output_label,style="Custom.TButton")
clear_button=ttk.Button(master=input_frame,text='Clear',command=clear,style="Custom.TButton")
clear_button.pack(side='right',padx=10,)


entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

output_label=ttk.Label(master=window,text='output',font='Calibri 24 bold')
output_label.pack(pady=5)




#frame2=tk.Toplevel(window) 
scroll_frame=tk.Frame(window)
scroll_frame.pack(pady=10,side=tk.LEFT)
listbox = tk.Listbox(scroll_frame, width=50, height=10,font=("Helvetica", 12))
listbox.pack(side=tk.LEFT,)
listbox.bind('<<ListboxSelect>>', on_list_select)


scrollbar = ttk.Scrollbar(scroll_frame ,command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

show_button = tk.Button(scroll_frame, text="Show Questions", command=show_questions,font=("Helvetica", 12))
show_button.pack(padx=10)


hide_button = tk.Button(scroll_frame, text="Hide Questions", command=hide_questions,font=("Helvetica", 12))
hide_button.pack(pady=10)


feedback_frame=tk.Frame(window)
feedback_frame.pack(pady=10)
feedback_name_label=ttk.Label(feedback_frame,text="Name")
feedback_name_label.pack(pady=10)
feedback_name_entry=ttk.Entry(feedback_frame)
feedback_name_entry.pack()
feedback_label=ttk.Label(feedback_frame,text="FeedBack")
feedback_label.pack(pady=10)

feedback_entry=ttk.Entry(feedback_frame)
feedback_entry.pack()

rating_var = tk.IntVar()
rating_label = tk.Label(feedback_frame, text="Rating:")
rating_label.pack()

for i in range(1, 6):
    tk.Radiobutton(feedback_frame, text=str(i), variable=rating_var, value=i).pack()

submit_button = tk.Button(feedback_frame, text="Submit Feedback", command=submit_feedback)
submit_button.pack()






window.mainloop()