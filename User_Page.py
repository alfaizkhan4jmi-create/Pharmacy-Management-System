#==========================Pharmacy user page==============================
from tkinter import *
from tkinter import ttk, messagebox
import pymysql


# ===== Window ka Size ko manage kiya  ====

user = Tk()

user.title("Pharmacy User Page")
user.geometry("1000x600")
user.config(bg="lightblue")
user.resizable(False, False)


# ==== Title  ====

Label(
    user,
    text="PHARMACY - MEDICINE SEARCH",
    font=("Arial", 26, "bold"),
    bg="darkblue",
    fg="white"
).pack(fill=X, pady=10)


# ================= Medicine search ke liye label me text ke liye  =================

Label(
    user,
    text="Medicine Name",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).place(x=100, y=100)


search_entry = Entry(
    user,
    font=("Arial", 18)
)

search_entry.place(x=300, y=100)


# ===== Treeview ke liye columns ko manage kiya.. =====

columns = (
    "MedicineID",
    "MedicineName",
    "Company",
    "Quantity",
    "Price",
    "ExpiryDate"
)

tree = ttk.Treeview(
    user,
    columns=columns,
    show="headings"
)

for column in columns:

    tree.heading(column, text=column)
    tree.column(column, width=140)

tree.place(
    x=30,
    y=200,
    width=940,
    height=280
)


# ==== Medicine Search Function or Sql ko Connect ====

def search_medicine():

    medicine_name = search_entry.get()

    if medicine_name == "":
        messagebox.showwarning(
            "Warning",
            "Enter Medicine Name"
        )
        return

    try:

        db = pymysql.connect(
            host="localhost",
            user="root",
            password="india123",
            database="pharmacy"
        )

        cursor = db.cursor()

        sql = """
        SELECT * FROM medicines
        WHERE MedicineName LIKE %s
        """

        cursor.execute(
            sql,
            ("%" + medicine_name + "%",)
        )

        records = cursor.fetchall()

        cursor.close()
        db.close()

        for item in tree.get_children():
            tree.delete(item)

        for record in records:
            tree.insert(
                "",
                END,
                values=record
            )

        if not records:

            messagebox.showinfo(
                "Result",
                "Medicine Not Found"
            )

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# ==== Show All Database ke liye function Create aur sql ko connect kiya query ====

def show_all():

    try:

        db = pymysql.connect(
            host="localhost",
            user="root",
            password="india123",
            database="pharmacy"
        )

        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM medicines"
        )

        records = cursor.fetchall()

        cursor.close()
        db.close()

        for item in tree.get_children():
            tree.delete(item)

        for record in records:
            tree.insert(
                "",
                END,
                values=record
            )

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# ==== Clear ke liye Function ====

def clear():

    search_entry.delete(0, END)

    for item in tree.get_children():
        tree.delete(item)


# ==== Search or Show All,Clear etc...Buttons  ====

Button(
    user,
    text="SEARCH",
    font=("Arial", 15, "bold"),
    bg="green",
    fg="white",
    command=search_medicine
).place(x=600, y=95)


Button(
    user,
    text="SHOW ALL",
    font=("Arial", 15, "bold"),
    command=show_all
).place(x=50, y=510)


Button(
    user,
    text="CLEAR",
    font=("Arial", 15, "bold"),
    command=clear
).place(x=180, y=510)


# ==== Back ke Function aur Button ====

def back():

    user.destroy()
    import Pharmacy_Main__Page


Button(
    user,
    text="BACK",
    font=("Arial", 15, "bold"),
    command=back
).place(x=800, y=510)


user.mainloop()

