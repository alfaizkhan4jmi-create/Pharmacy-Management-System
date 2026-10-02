# Pharmacy-Management-System
Pharmacy Management System built using Python, Tkinter, MySQL, and PyMySQL. It allows admins to add, update, delete, and manage medicines, while users can search and view medicine details....
#   Pharmacy Management System

A desktop-based Pharmacy Management System developed using *Python Tkinter* and *MySQL*.

##  Project Overview

This project is designed to manage pharmacy medicines efficiently. The system provides separate Admin and User pages.

The Admin can manage medicine records, while users can search and view available medicines.

##  Features

-  Admin Login
-  Add Medicine
-  Update Medicine
-  Delete Medicine
-  Search Medicine
-  Display All Medicines
-  Manage Medicine Quantity
-  Manage Medicine Price
-  Company Details
-  Expiry Date Management
-  Tkinter GUI
-  MySQL Database
-  Environment Variables for Database Credentials

##  Technologies Used

- Python
- Tkinter
- MySQL
- PyMySQL
- python-dotenv
- ttk Treeview

## 📂 Project Structure

PharmacyProject/
│
├── main.py
├── userpage.py
├── adminpage.py
├── .gitignore
└── README.md

## 👨‍💻 Admin Access

Username:
XXXXX

Password:
XXXXXX

After login, the admin can:

- Add medicines
- Update medicines
- Delete medicines
- View all medicines

## 🗄️ Database

Database Name:

pharmacy

Main table:

medicines

Fields:

- MedicineID
- MedicineName
- Company
- Quantity
- Price
- ExpiryDate

##  Installation

Install required libraries:

```bash
pip install pymysql python-dotenv
