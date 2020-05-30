import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import smtplib


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


def spamEmailsButton():
    text = txt_edit.get(1.0, tk.END)
    email_subject =  subject.get()
    repeat = int(number_of_times.get())
    email_recipient = email.get()
    email_recipient_list = email_recipient.split(",")
    for i in range(1,repeat):
        sendemail(from_addr    = "humanreal20@gmail.com",
                  to_addr_list = email_recipient_list,
                  # cc_addr_list = [],
                  subject      = email_subject,
                  message      = text,
                  login        = "humanreal20@gmail.com",
                  password     = "TotallyReal999")


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

'''
def handle_focus_out(_):
    email.delete(0, tk.END)
    email.config(fg='grey')
    email.insert(0, "Enter Email Address")

def handle_enter(txt):
    print(email.get())
    # handle_focus_out('dummy')
    fr_buttons.foucs()
'''
window = tk.Tk()
window.title("Email Editor")

window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

txt_edit = tk.Text(window, height=30)
fr_buttons = tk.Frame(window)
# email = tk.Entry(fr_buttons)
label = tk.Label(window, text="User: ")
# label.pack(side="left")

email = tk.Entry(window, bd=1)
email.insert(0, 'Enter Recieving Emails: ')
email.bind('<FocusIn>', on_entry_click)
email.bind('<FocusOut>', on_focusout)
email.config(fg = 'grey')
# email.pack(side="left")

# email = tk.Entry(fr_buttons, bg='white', fg='grey')
# email.bind("<FocusIn>", handle_focus_in)
# email.bind("<FocusOut>", handle_focus_out)
# email.bind("<Return>", handle_enter)
subject = tk.Entry(fr_buttons)
number_of_times = tk.Entry(fr_buttons)
btn_send = tk.Button(fr_buttons, text="Send", command = spamEmailsButton, width = 60)
btn_save = tk.Button(fr_buttons, text="Save As...", command = save_file)

btn_send.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
email.grid(row=2, column=0, sticky="ew",padx=5, pady=5)
subject.grid(row=3, column=0, sticky="ew",padx=5, pady=5)
number_of_times.grid(row=4, column=0,sticky="ew",padx=5, pady=5)
label.grid(row=5, column=0,sticky="ew",padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nw",padx=5, pady=5)

# email.insert(0, "Enter Email Address")



window.mainloop()