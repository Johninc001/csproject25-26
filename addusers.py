from nicegui import ui 
import random
import sqlite3
def has_space(name):
    return " " in name
def make_id():
    staffid=random.randint(100000, 999999)
    return staffid
def is_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
def is_phone(phone):
    if phone.isdigit() and (7 <= len(phone) <= 15):
        return True
    else:
        return False
def is_above_min_wage(wage):
    try:
        wage_value = float(wage)
        if wage_value >= 12.76:
            return True
        else:
            return False
    except ValueError:
        return False
@ui.page("/")
def add_user():
    ui.add_css("""
    .btn {
        background-color: #000000;
        border: none;
        color: white;
        padding: 10px 24px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        text-align: center;""")
    with ui.column().classes("w-full items-center"):
        with ui.card().classes("w-50 items-center justify-center"):
            ui.label("Add User Page")
        with ui.card().classes("w-50 items-center justify-center"):
            ui.label("fullname:")
            fullname=ui.input("fullname", validation=lambda v: "must contain a space between first and last name" if not has_space(v) else None,)
            ui.label("username:")
            username=ui.input("username", validation=lambda v: "must be at least 5 characters long" if len(v) < 5 else None,)
            ui.label("password:")
            password=ui.input("password", validation=lambda v: "must be at least 8 characters long" if len(v) < 8 else None,)
            ui.label("email:")
            email=ui.input("email address", validation=lambda v: "must be a valid email address" if not is_email(v) else None)
            ui.label("phone number:")
            phone=ui.input("phone number", validation=lambda v: "must be a valid phone number" if not is_phone(v) else None)
            ui.label("gender:")
            gender=ui.select(options=["Male", "Female", "Other", "gender"], value="gender")
            ui.label("wage/hour:")
            wage=ui.input("wage", validation=lambda v: "must be a valid wage above minimum wage of £12.76" if not is_above_min_wage(v) else None)
            ui.label("paid status:")
            paid=ui.checkbox("Paid?")

            def handle_user_submit():
                if not (fullname.value and username.value and password.value and email.value and phone.value and wage.value):
                    ui.notify("Please fill in all fields.", color="red")
                    return
                conn=sqlite3.connect('gmvets.db')
                c=conn.cursor()
                staffid=make_id()
                c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, fullname TEXT, username TEXT, password TEXT, email TEXT, phone TEXT, gender TEXT, wage TEXT, paid BOOLEAN)")
                c.execute("INSERT INTO users (id, fullname, username, password, email, phone, gender, wage, paid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (staffid, fullname.value, username.value, password.value, email.value, phone.value, gender.value, wage.value, paid.value))
                conn.commit()
                conn.close()
                ui.notify("User added successfully!", color="green")
            ui.button("Add User", on_click=handle_user_submit).classes("btn w-30")
ui.run(title="Add User Page")