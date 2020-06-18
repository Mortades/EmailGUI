import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import smtplib
from readEmailCredentials import readCredentials
from tkinter import ttk


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
        window.title(f"Simple Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    # header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

    return problems

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def spamEmailsButton():
    # readCredential call here
    sending_email, password = readCredentials("Credentials.txt")
    text = txt_edit.get(1.0, tk.END)
    email_subject =  subject.get()

    repeat = number_of_times.get()
    try:
        repeat = int(repeat)
    except ValueError:
        popupmsg('Number of times must be an integer written like this: "8"')
        raise Exception('User dumb')

    email_recipient = email.get()
    email_recipient_list = email_recipient.split(",")
    for i in range(0,len(email_recipient_list)):
        email_recipient_list[i-1].strip(" ")
    for person in email_recipient_list:
        try:
            assert "@" in person
            assert "." in person
        except AssertionError:
            popupmsg('Please use the correct formatting for email addresses')
    for i in range(0,repeat):
        sendemail(from_addr    = sending_email,
                  to_addr_list = email_recipient_list,
                  # cc_addr_list = [],
                  subject      = email_subject,
                  message      = text,
                  login        = sending_email,
                  password     = password)

    popupmsg("Email Sent")


def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if email.get() == 'Enter Recieving Emails: ':
       email.delete(0, "end") # delete all the text in the entry
       email.insert(0, '') #Insert blank for user input
       email.config(fg = 'black')
def on_focusout(event):
    if email.get() == '':
        email.insert(0, 'Enter Recieving Emails: ')
        email.config(fg = 'grey')
def handle_focus_in(_):
    email.delete(0, tk.END)
    email.config(fg='black')


def on_entry_click_sub(event):
    """function that gets called whenever entry is clicked"""
    if subject.get() == 'Enter Subject: ':
       subject.delete(0, "end") # delete all the text in the entry
       subject.insert(0, '') #Insert blank for user input
       subject.config(fg = 'black')
def on_focusout_sub(event):
    if subject.get() == '':
        subject.insert(0, 'Enter Subject: ')
        subject.config(fg = 'grey')
def handle_focus_in_sub(_):
    subject.delete(0, tk.END)
    subject.config(fg='black')

    
def on_entry_click_times(event):
    """function that gets called whenever entry is clicked"""
    if number_of_times.get() == 'Enter Number Of Times To Send Email: ':
       number_of_times.delete(0, "end") # delete all the text in the entry
       number_of_times.insert(0, '') #Insert blank for user input
       number_of_times.config(fg = 'black')
def on_focusout_times(event):
    if number_of_times.get() == '':
        number_of_times.insert(0, 'Enter Number Of Times To Send Email: ')
        number_of_times.config(fg = 'grey')
def handle_focus_in_times(_):
    number_of_times.delete(0, tk.END)
    number_of_times.config(fg='black')


window = tk.Tk()
window.title("Email Editor")

window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

txt_edit = tk.Text(window, height=30)
fr_buttons = tk.Frame(window)


email = tk.Entry(fr_buttons, bd=1) #Assigning special email box to frame
email.insert(0, 'Enter Recieving Emails: ') #Box prompt - if changed also change in functions
email.bind('<FocusIn>', on_entry_click) #Command executed when focus is gained
email.bind('<FocusOut>', on_focusout)  #Command executed when focus is lost
email.config(fg = 'grey')


subject = tk.Entry(fr_buttons) #Assign buttons and entry boxes a frame
subject.insert(0, 'Enter Subject: ') #Box prompt - if changed also change in functions
subject.bind('<FocusIn>', on_entry_click_sub) #Command executed when focus is gained
subject.bind('<FocusOut>', on_focusout_sub)  #Command executed when focus is lost
subject.config(fg = 'grey')


number_of_times = tk.Entry(fr_buttons) #Assign buttons and entry boxes a frame
number_of_times.insert(0, 'Enter Number Of Times To Send Email: ') #Box prompt - if changed also change in functions
number_of_times.bind('<FocusIn>', on_entry_click_times) #Command executed when focus is gained
number_of_times.bind('<FocusOut>', on_focusout_times)  #Command executed when focus is lost
number_of_times.config(fg = 'grey')

btn_send = tk.Button(fr_buttons, text="Send", command = spamEmailsButton, width = 60)
btn_save = tk.Button(fr_buttons, text="Save As...", command = save_file) #Assign buttons and entry boxes a frame ends here

btn_send.grid(row=0, column=0, sticky="ew", padx=5, pady=5) #Sets the order of buttons in the first column of the grrid
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
email.grid(row=2, column=0, sticky="ew",padx=5, pady=5)
subject.grid(row=3, column=0, sticky="ew",padx=5, pady=5)
number_of_times.grid(row=4, column=0,sticky="ew",padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns") #Sets the frame 'fr_buttons' to the first column of the grid
txt_edit.grid(row=0, column=1, sticky="nw",padx=5, pady=5) #Sets the order of buttons in the second column of the grrid



window.mainloop()