#================PHARMACY PROJECT===================
## Libraries...
from tkinter import *
from tkinter import ttk,messagebox
import pymysql

#=======DATABASES=======

db = pymysql.connect(
    host="localhost",
    user="root",
    password="india123",
    database="PHARMACY"
)

cursor= db.cursor()

#========PHARMACY MAIN WINDOW=======
boot = Tk()
boot.title("Pharmacy Management SYSTEM")
boot.geometry("1200x650")
boot.config(bg="lightblue")

#========TITLE=======
Label(
    boot,
    text="PHARMACY MANAGEMENT SYSTEM",
    font=("Arial",28,"bold"),
    bg="darkblue",
    fg="white"
).pack(fill=X,pady=10)

#=======LABLES=======

Label(boot,text="Medicine ID",
font=("Arial",16,"bold"),
bg="lightblue").place(x=50,y=100)


Label(boot,text="Medicine Name",
font=("Arial",16,"bold"),
bg="lightblue").place(x=50,y=160)



Label(boot,text="Company",
font=("Arial",16,"bold"),
bg="lightblue").place(x=50,y=220)



Label(boot,text="Quantity",
font=("Arial",16,"bold"),
bg="lightblue").place(x=50,y=280)




Label(boot,text="Price",
font=("Arial",16,"bold"),
bg="lightblue").place(x=50,y=340)




Label(boot,text="Expiry Date",
font=("Arial",16,"bold"),
bg="lightblue").place(x=50,y=400)

#=======Entries=======

id_entry =Entry(boot,font=("Arial",16))
id_entry.place(x=230,y=100)


name_entry =Entry(boot,font=("Arial",16))
name_entry.place(x=230,y=160)


company_entry =Entry(boot,font=("Arial",16))
company_entry.place(x=230,y=220)



quantity_entry =Entry(boot,font=("Arial",16))
quantity_entry.place(x=230,y=280)



price_entry =Entry(boot,font=("Arial",16))
price_entry.place(x=230,y=340)



expiry_entry =Entry(boot,font=("Arial",16))
expiry_entry.place(x=230,y=400)



#=======Page ko clean kerne ke liye function create========
def clear():
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    company_entry.delete(0,END)
    quantity_entry.delete(0,END)
    price_entry.delete(0,END)
    expiry_entry.delete(0,END)


#========Add Medicine=========

def add_medicine():
    if id_entry.get()=="" or name_entry.get()=="":
        messagebox.showwarning("Warning","Medicine ID and Name required")
        return

    try:
        sql ="""
        INSERT INTO medicines
        (MedicineID,MedicineName,
         Company,Quantity,Price,ExpiryDate)
         VALUES(%s,%s,%s,%s,%s,%s)
         """

        values = (
            id_entry.get(),
            name_entry.get(),
            company_entry.get(),
            quantity_entry.get(),
            price_entry.get(),
            expiry_entry.get()
        )

        cursor.execute(sql,values)
        db.commit()


        messagebox.showinfo("Success","Medicine Added Successfully")
        clear()
        show_medicines()


    except Exception as error:
        messagebox.showerror("Database Error",str(error))



#=====Show Medicines=====

def show_medicines():
    for item in tree.get_children():
        tree.delete(item)


    cursor.execute("Select * from medicines")

    records = cursor.fetchall()



    for record in records:
        tree.insert("",END,values=record)



#====Delete function======
def delete_medicines():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Warning","Selected a medicine")
        return

    data = tree.item(selected[0])["values"]

    cursor.execute(
        "Delete from medicines where MedicineID=%s",
        (data[0],)
    )

    db.commit()

    messagebox.showinfo("Success","Medicine Deleted")
    show_medicines()

#====TreeView=====

columns =(
    "MedicineID",
    "MedicineName",
    "Company",
    "Quantity",
    "Price",
    "ExpiryDate"
)

tree = ttk.Treeview(
    boot,
    columns=columns,
    show="headings"
)

for column in columns:
    tree.heading(column,text=column)
    tree.column(column,width=120)
tree.place(x=550,y=100,width=600,height=350)


#=====Buttons=====

Button(
    boot,
    text="ADD MEDICINE",
    font=("Arial",14,"bold"),
    bg="green",
    fg="white",
    command=add_medicine
).place(x=100,y=480)



Button(
    boot,
    text="CLEAR",
    font=("Arial",14,"bold"),
    command=clear
).place(x=270,y=480)


Button(
    boot,
    text="DELETE",
    font=("Arial",14,"bold"),
    bg="red",
    fg="white",
    command=delete_medicines
).place(x=550,y=480)



Button(
    boot,
    text="ADD MEDICINE",
    font=("Arial",14,"bold"),
    command=show_medicines
).place(x=680,y=480)




show_medicines()
boot.mainloop()

              













                            
        