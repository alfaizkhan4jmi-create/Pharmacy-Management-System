from tkinter import *
from tkinter import messagebox


# ================= Admin_Page ki Window Creation ====

admin = Tk()

admin.title("Pharmacy Admin Login")
admin.geometry("600x450")
admin.config(bg="lightblue")
admin.resizable(False, False)


# ==== Pharmacy Admin Login ke liye Label create ====

Label(
    admin,
    text="PHARMACY ADMIN LOGIN",
    font=("Arial", 26, "bold"),
    bg="Darkblue",
    fg="white"
).pack(fill=X, pady=20)


# ====  Username ke liye label create ====

Label(
    admin,
    text="Username",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).place(x=100, y=130)


username_entry = Entry(
    admin,
    font=("Arial", 18)
)

username_entry.place(x=250, y=130)


# ==== Label Create Kiya Password ke Liye ====

Label(
    admin,
    text="Password",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).place(x=100, y=190)


password_entry = Entry(
    admin,
    font=("Arial", 18),
    show="*"
)

password_entry.place(x=250, y=190)


# =====Login time password entry ko accept or deny ke condition .....

def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":

        messagebox.showwarning(
            "Warning",
            "Please enter Username and Password"
        )

        return

    if username == "Alfaiz" and password == "1789":

        messagebox.showinfo(
            "Login",
            "Admin Login Successful"
        )

    else:

        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password"
        )


# ====Login ke liye button====

Button(
    admin,
    text="LOGIN",
    font=("Arial", 18, "bold"),
    bg="green",
    fg="white",
    command=login
).place(x=250, y=270)


# ================= BACK =================

def back():

    admin.destroy()
    import Pharmacy_Main__Page


Button(
    admin,
    text="BACK",
    font=("Arial", 14, "bold"),
    command=back
).place(x=270, y=350)




admin.mainloop()