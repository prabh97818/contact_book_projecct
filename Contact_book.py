import tkinter as tk
from tkinter import ttk
from csv import DictWriter, DictReader
from os import stat, system
from tkinter import messagebox as mbox

def action():
    global name_var
    global age_var
    global gender_var
    global occ_var
    global email_var
    global phone_var
    global city_var
    global state_entry
    global state_var
    global confirm_var

    name = name_var.get().title()
    age = age_var.get()
    gender = gender_var.get().title()
    occupation = occ_var.get().title()
    email = email_var.get()
    phone = phone_var.get()
    city = city_var.get().title()
    state = state_var.get().title()
    confirm = confirm_var.get()

    confirm_checkbutton['fg'] = 'Black'

    if name == "" or age == "" or gender == "" or occupation == "" or email == "" or phone =="" or city == "" or state =="":
        mbox.showinfo("Null Value Error", "Please fill your detail completely!")
        name_entry.focus()
    else:
        if confirm == 1:
            with open("contacts.csv", "a", newline="\n") as wf:
                writer = DictWriter(wf, fieldnames = ['Name', 'Age', 'Gender', 'Occupation', 'Email', 'Phone', 'City', 'State'])
                if stat('contacts.csv').st_size == 0:
                    writer.writeheader()
                writer.writerow({
                    'Name':name,
                    'Age': age,
                    'Gender':gender,
                    'Occupation': occupation,
                    'Email':email,
                    'Phone':phone,
                    'City':city,
                    'State':state
                })
            mbox.showinfo("Success", "Values Added Successfully!")
            name_entry.delete(0, "end")
            age_entry.delete(0, "end")
            occ_combobox.delete(0, "end")
            email_entry.delete(0, "end")
            phone_entry.delete(0, "end")
            city_entry.delete(0, "end")
            state_entry.delete(0, "end")
            name_entry.focus()
                     
        else:
            mbox.showinfo("Confirm", "Please! Recheck Your Detail!")
            confirm_checkbutton['fg'] = 'Red'
            win1.focus()

def contact_n():
    global win1
    win1 = tk.Toplevel(win)
    win1.config(background = "Black")
    win1.title("Add New Contact - Contact Book")

    our_frame = tk.LabelFrame(win1)
    our_frame.pack(anchor = tk.CENTER, padx = 20, pady = 20)

    title_label = ttk.Label(our_frame, text = "Add New Contact", font = 20)
    title_label.grid(row = 0, columnspan = 2, pady = 5)

    # Name Label
    name_label = ttk.Label(our_frame, text = "Name :")
    name_label.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 3)

    #age abel 
    age_label = ttk.Label(our_frame, text = "Age : ")
    age_label.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 3)

    #gender with radio button
    global gender_var
    gender_var = tk.StringVar()
    radiobtn1 = ttk.Radiobutton(our_frame, text = "Male", value = "Male", variable = gender_var)
    radiobtn1.grid(row = 3, column = 0, sticky = tk.W, padx = 10, pady = 3)
    radiobtn2 = ttk.Radiobutton(our_frame, text = 'Female', value = "Female", variable = gender_var)
    radiobtn2.grid(row = 3, column = 1, padx = 10, pady = 3)

    # More Labels
    occ_label = ttk.Label(our_frame, text = "Occupation :")
    occ_label.grid(row = 4, column = 0, sticky = tk.W, padx = 10, pady = 3)

    email_label = ttk.Label(our_frame, text = "Email :")
    email_label.grid(row = 5, column = 0, sticky = tk.W, padx = 10, pady = 3)

    phone_label = ttk.Label(our_frame, text = "Phone No. :")
    phone_label.grid(row = 6, column = 0, sticky = tk.W, padx = 10, pady = 3)

    city_label = ttk.Label(our_frame, text = "City : ")
    city_label.grid(row = 7, column = 0, sticky = tk.W, padx = 10, pady = 3)

    state_label = ttk.Label(our_frame, text = "State : ")
    state_label.grid(row = 8, column = 0, sticky = tk.W, padx = 10, pady = 3)

    # Entry_boxes
    global name_var 
    name_var = tk.StringVar()
    global name_entry
    name_entry = ttk.Entry(our_frame, width = 16, textvariable = name_var)
    name_entry.grid(row = 1, column = 1, padx = 10, pady = 3)
    name_entry.focus()

    global age_var
    age_var = tk.StringVar()
    global age_entry
    age_entry = ttk.Entry(our_frame, width = 16, textvariable = age_var)
    age_entry.grid(row = 2, column = 1, padx = 10, pady = 3)

    # COmbobox for occupation
    global occ_var
    occ_var = tk.StringVar()
    global occ_combobox
    occ_combobox = ttk.Combobox(our_frame, width = 13, textvariable = occ_var)
    occ_combobox['values'] = ("Student", "Worker", "Businessman")
    occ_combobox.grid(row = 4, column = 1, padx = 10, pady = 3)
    occ_combobox.current(0)

    global email_var
    email_var = tk.StringVar()
    global email_entry
    email_entry = ttk.Entry(our_frame, width = 16, textvariable = email_var)
    email_entry.grid(row = 5, column = 1, padx = 10, pady = 3)

    global phone_var
    phone_var = tk.StringVar()
    global phone_entry
    phone_entry = ttk.Entry(our_frame, width = 16, textvariable = phone_var)
    phone_entry.grid(row = 6, column = 1, padx = 10, pady = 3)

    global city_var
    city_var = tk.StringVar()
    global city_entry
    city_entry = ttk.Entry(our_frame, width = 16, textvariable = city_var)
    city_entry.grid(row = 7, column = 1, padx = 10, pady = 3)

    global state_var
    state_var = tk.StringVar()
    global state_entry
    state_entry = ttk.Entry(our_frame, width = 16, textvariable = state_var)
    state_entry.grid(row = 8, column = 1, padx = 10, pady = 3)

    #checkbutton
    global confirm_var
    confirm_var = tk.IntVar()
    global confirm_checkbutton
    confirm_checkbutton = tk.Checkbutton(our_frame, text = "I have rechecked the detail", variable = confirm_var)
    confirm_checkbutton.grid(row = 9, columnspan = 2, sticky = tk.W, padx = 10, pady = 3)

    #submit Button
    submitbtn = tk.Button(our_frame, text = "Add Contact", command = action, bg = "Light Grey")
    submitbtn.grid(row = 10, columnspan = 2, padx = 10, pady = 5)

    # win1.mainloop()

def all_contacts():
    global win3
    win3 = tk.Toplevel(win)
    win3.title("All Contact - Contact Book")
    win3.config(background = "Black")
    place_holder = tk.LabelFrame(win3)
    place_holder.pack(anchor = tk.CENTER, padx = 20, pady = 20)

    title_label = ttk.Label(place_holder, text = "Your Contacts", font = ('Arial', 15))
    title_label.grid(row = 0, columnspan = 8, pady = 5)

    name_label = ttk.Label(place_holder, text = "Name", font = ('Arial', 13))
    name_label.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 3)

    age_label = ttk.Label(place_holder, text = "Age", font = ('Arial', 13))
    age_label.grid(row = 1, column = 1, sticky = tk.W, padx = 10, pady = 3)

    gender_label = ttk.Label(place_holder, text = "Gender", font = ('Arial', 13))
    gender_label.grid(row = 1, column = 2, sticky = tk.W, padx = 10, pady = 3)

    occ_label = ttk.Label(place_holder, text = "Occupation", font = ('Arial', 13))
    occ_label.grid(row = 1, column = 3, sticky = tk.W, padx = 10, pady = 3)

    email_label = ttk.Label(place_holder, text = "Email", font = ('Arial', 13))
    email_label.grid(row = 1, column = 4, sticky = tk.W, padx = 10, pady = 3)

    phone_label = ttk.Label(place_holder, text = "Phone No.", font = ('Arial', 13))
    phone_label.grid(row = 1, column = 5, sticky = tk.W, padx = 10, pady = 3)

    city_label = ttk.Label(place_holder, text = "City", font = ('Arial', 13))
    city_label.grid(row = 1, column = 6, sticky = tk.W, padx = 10, pady = 3)

    state_label = ttk.Label(place_holder, text = "State", font = ('Arial', 13))
    state_label.grid(row = 1, column = 7, sticky = tk.W, padx = 10, pady = 3)

    try:
        with open("contacts.csv") as rf:
            reader = DictReader(rf)
            row_n = 2
            for items in reader:
                column_n = 0
                for val in items.values():
                    Label1  = ttk.Label(place_holder, text = val)
                    Label1.grid(row = row_n, column = column_n, sticky = tk.W, padx = 10, pady = 3)
                    # print(val)
                    column_n += 1
                row_n += 1
    except FileNotFoundError:
        Label2  = ttk.Label(place_holder, text = "Your Contact List is Empty")
        Label2.grid(row = 2, columnspan = 8, pady = 5)
    except:
        mbox.showerror("Error", "Unknown Error Occured!")
        win3.destroy()

count = 0
def search():
    global count
    global win4
    global place_holder2
    # a = input("enter a value: ")
    # b = input("second value : ")
    search_type = opt_var.get()
    query1 = query_var.get()

    try:
        contacts1 = []
        with open("contacts.csv") as rf:
            reader = DictReader(rf)
            for item in reader:
                if (search_type,query1.title()) in item.items():
                    contacts1.append(item)

        if len(contacts1) == 0:
            mbox.showinfo("Message", "No Contact Found!")
            win4.focus()
        else:
            if count !=0 :
                place_holder2.destroy()
            place_holder2 = tk.LabelFrame(win4)
            place_holder2.pack(anchor = tk.CENTER, padx = 20, pady = 20)

            title_label = ttk.Label(place_holder2, text = "Search Results", font = ('Arial', 15))
            title_label.grid(row = 0, columnspan = 8, pady = 5)

            name_label = ttk.Label(place_holder2, text = "Name", font = ('Arial', 13))
            name_label.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 3)

            age_label = ttk.Label(place_holder2, text = "Age", font = ('Arial', 13))
            age_label.grid(row = 1, column = 1, sticky = tk.W, padx = 10, pady = 3)

            gender_label = ttk.Label(place_holder2, text = "Gender", font = ('Arial', 13))
            gender_label.grid(row = 1, column = 2, sticky = tk.W, padx = 10, pady = 3)

            occ_label = ttk.Label(place_holder2, text = "Occupation", font = ('Arial', 13))
            occ_label.grid(row = 1, column = 3, sticky = tk.W, padx = 10, pady = 3)

            email_label = ttk.Label(place_holder2, text = "Email", font = ('Arial', 13))
            email_label.grid(row = 1, column = 4, sticky = tk.W, padx = 10, pady = 3)

            phone_label = ttk.Label(place_holder2, text = "Phone No.", font = ('Arial', 13))
            phone_label.grid(row = 1, column = 5, sticky = tk.W, padx = 10, pady = 3)

            city_label = ttk.Label(place_holder2, text = "City", font = ('Arial', 13))
            city_label.grid(row = 1, column = 6, sticky = tk.W, padx = 10, pady = 3)

            state_label = ttk.Label(place_holder2, text = "State", font = ('Arial', 13))
            state_label.grid(row = 1, column = 7, sticky = tk.W, padx = 10, pady = 3)

            row_n = 2
            for val in contacts1:
                column_n = 0
                for a,b in val.items():
                    Label1  = ttk.Label(place_holder2, text = b)
                    Label1.grid(row = row_n, column = column_n, sticky = tk.W, padx = 10, pady = 3)
                    column_n += 1
                row_n += 1
    except:
        mbox.showinfo("Title", "No Contact Found!")
        win4.focus()

    count += 1

def search_contact():
    global win4
    # win4 = tk.Toplevel(win)
    win4 = tk.Toplevel(win)
    win4.title("Search - Contact Book")
    win4.config(background = "Black")
    place_holder = tk.LabelFrame(win4)
    place_holder.pack(anchor = tk.CENTER, padx = 20, pady = 20)

    title_label = ttk.Label(place_holder, text = "Search Contacts", font = ('Arial', 15))
    title_label.grid(row = 0, columnspan = 8, pady = 5)

    global opt_var
    opt_var = tk.StringVar()
    opt_combobox = ttk.Combobox(place_holder, width = 13, textvariable = opt_var, state = "readonly")
    opt_combobox['values'] = ("Name", "Age", "Gender", "Occupation", "City", "State")
    opt_combobox.current(0)
    opt_combobox.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 3)
    
    global query_var 
    query_var = tk.StringVar()
    global query_entry
    query_entry = ttk.Entry(place_holder, width = 16, textvariable = query_var)
    query_entry.grid(row = 1, column = 1, padx = 10, pady = 3)

    search_label = tk.Button(place_holder, text = "Search", font = ('Arial', 13), command = search, bg = "Light Grey")
    search_label.grid(row = 1, column = 2, sticky = tk.W, padx = 10, pady = 3)

def home():
    global win
    win = tk.Tk()

    win.title("Contact Book")
    win.config(background = "Black")

    holder = tk.LabelFrame(win)
    holder.pack(anchor = tk.CENTER, padx = 20, pady = 20)

    title1 = ttk.Label(holder, text = "Welcome To The Contact Book", font = 15)
    title1.grid(row = 0, column = 0, padx = 20, pady = 5)

    global label1
    label1 = tk.Button(holder, text = "Add New Contact", command = contact_n, font = 10, bg = "Grey")
    label1.grid(row = 1, padx = 10, pady = 5)

    label2 = tk.Button(holder, text = "Show All Contact", command = all_contacts, font = 10, bg = "Grey")
    label2.grid(row = 2, padx = 10, pady = 5)

    label3 = tk.Button(holder, text = "Search Contact", command = search_contact, font = 10, bg = "Grey")
    label3.grid(row = 3, padx = 10, pady = 5)

    win.mainloop()

home()
