from nicegui import ui, app
import sqlite3
import bcrypt
from validation import iscreditcard, range_check, mmyy_format, password_hash

def moving(pages):
    ui.navigate.to(f"/{pages}")

def has_space(name):
    return " " in name
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
    except TypeError:
        for i in range(len(wage)):
            if wage[i] == "£":
                wage = wage[:i] + wage[i+1:]
                break
    except ValueError:
        return False
def top(page):
   if page=="edit":
        with ui.card().classes("w-full h-12 card fill-neutral-400") :
            ui.button("+", on_click=lambda:moving(pages=""))
            ui.label ("greenmountvets")
   elif page=="addusers": 
       with ui.card().classes("w-full h-12 card fill-neutral-400") :
            ui.button("edit", on_click=lambda:moving(pages="edit"))
            ui.label ("greenmountvets")
@ui.page("/edit")
def editinvoice():
    top(page="edit")
    ui.space()

    with ui.column().classes("w-full items-center"):
        ui.label("Edit Invoice").classes("text-3xl")
        ui.separator().classes("w-96")
        ui.space().classes("h-4")

        #clears all fields and resets the page to the default state
        loadedinvoiceid = ""
        purchaselist = []
        purchaseoptions=["medicine","Carprofen - £25.50", "Meloxicam - £18.75", "Furosemide - £12.40", "Amoxicillin - £15.90", "Metronidazole - £14.20", "Prednisolone - £9.80", "Gabapentin - £22.60", "Enrofloxacin - £19.50", "Clindamycin - £16.30", "Pimobendan - £34.00"]

       
#takes invoice id as input and displays it for editing
        with ui.card().classes("card width:50% whiteglow"):
            with ui.row():
                invoiceid=ui.input("invoice ID").classes("w-50")
                ui.space().classes("w-9")
                ui.button("Load Invoice", color="black", on_click=lambda:load_invoice(invoiceid.value)).classes("btn w-50 text-white rounded-lg")

            ui.space()
            ui.label("customer name")

            with ui.row():
                custid=ui.input("customer ID", validation=lambda v: None if v == "" or v is None else ("must be 12 numbers long and numeric" if not (v.isdigit() and len(v) == 12) else None)).classes("w-50")
                ui.space().classes("w-9")
                fname=ui.input("forename", validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not range_check(v, 3, 15) else None)
                ui.space().classes("w-9")
                sname=ui.input("surname",  validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not range_check(v, 3, 15) else None)
                ui.space().classes("w-9")
                pnum=ui.input("phone number", validation=lambda v: "must be 11 digits long and only contain numbers" if not (len(v) == 11 and v.isdigit()) else None)
                ui.space().classes("w-9")
                email=ui.input("email address", validation=lambda v: "must contain an @ and a . " if not ("@" in v and "." in v) else None)
                ui.space().classes("w-9")

            with ui.row():
                creditcard=ui.input("credit(or debit) card number", validation=lambda v: "must be 16 digits long and only contain numbers" if not iscreditcard(v) else None)
                ui.space().classes("w-9")
                expirydate=ui.input("expiry date", validation=lambda v: "must be in the format mm/yy" if not mmyy_format(v) else None)
                ui.space().classes("w-9")
                staffname=ui.input("staff member")

        with ui.card().classes("w-85 whiteglow items-center justify-center"):
            ui.label("purchases")
            purchaseslabel = ui.label("current purchases: none")
            ui.label("select a purchase and click \"Add to list\"")
            purchases = ui.select(purchaseoptions, with_input=True,value="medicine").classes("w-50 whiteglow").props("outlined color=black")

            #refreshes the purchase label to show the current purchases in the purchaselist variable if there are no purchases shows "current purchases: none"
            def refresh_purchase_label():
                if len(purchaselist) == 0:
                    purchaseslabel.set_text("current purchases: none")
                else:
                    purchaseslabel.set_text(", ".join(purchaselist))

            def add_purchase(sel):
                selected = sel.value
                if selected:
                    purchaselist.append(selected)
                    refresh_purchase_label()

            def clear_purchase_list():
                purchaselist.clear()
                refresh_purchase_label()
                ui.notify("purchase list cleared")

            def clear_fields():
                nonlocal loadedinvoiceid
                loadedinvoiceid = ""
                invoiceid.value=""
                custid.value=""
                fname.value=""
                sname.value=""
                pnum.value=""
                email.value=""
                creditcard.value=""
                expirydate.value=""
                staffname.value=""
                purchases.value="medicine"
                purchaselist.clear()
                refresh_purchase_label()
                ui.notify("fields cleared")

            #takes the invoice id input and retrieves the corresponding invoice data from the db then fills the fields with that data for editing
            def load_invoice(loadedid):
                nonlocal loadedinvoiceid
                if loadedid is None or loadedid == "":
                    ui.notify("enter an invoice id", color="red")
                    return

                if not loadedid.isdigit():
                    ui.notify("invoice id must be numeric", color="red")
                    return

                con = sqlite3.connect("gmvets.db")
                c = con.cursor()
                c.execute("SELECT id, custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist, staffname FROM invoices WHERE id = ?", (loadedid,))
                invoicerow = c.fetchone()
                con.close()

                if invoicerow is None:
                    ui.notify("invoice not found", color="red")
                    return

                loadedinvoiceid = str(invoicerow[0])
                invoiceid.value = str(invoicerow[0])
                custid.value = "" if invoicerow[1] is None else str(invoicerow[1])
                fname.value = "" if invoicerow[2] is None else str(invoicerow[2])
                sname.value = "" if invoicerow[3] is None else str(invoicerow[3])
                pnum.value = "" if invoicerow[4] is None else str(invoicerow[4])
                email.value = "" if invoicerow[5] is None else str(invoicerow[5])
                creditcard.value = "" if invoicerow[6] is None else str(invoicerow[6])
                expirydate.value = "" if invoicerow[7] is None else str(invoicerow[7])
                staffname.value = "" if invoicerow[9] is None else str(invoicerow[9])

                purchaselist.clear()
                if invoicerow[8] is not None and invoicerow[8] != "":
                    splitpurchases = str(invoicerow[8]).split(",")
                    for i in range(len(splitpurchases)):
                        purchaseitem = splitpurchases[i].strip()
                        if purchaseitem != "":
                            purchaselist.append(purchaseitem)
                refresh_purchase_label()
                ui.notify("invoice loaded", color="green")

            #updates invoices
            def update_invoice():
                if loadedinvoiceid == "":
                    ui.notify("load an invoice first", color="red")
                    return

                con = sqlite3.connect("gmvets.db")
                c = con.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY AUTOINCREMENT, custid TEXT, fname TEXT, sname TEXT, pnum TEXT, email TEXT, creditcard TEXT, expirydate TEXT, purchaselist TEXT, staffname TEXT)")
                c.execute(
                    "UPDATE invoices SET custid = ?, fname = ?, sname = ?, pnum = ?, email = ?, creditcard = ?, expirydate = ?, purchaselist = ?, staffname = ? WHERE id = ?",
                    (custid.value, fname.value, sname.value, pnum.value, email.value, creditcard.value, expirydate.value, ",".join(purchaselist), staffname.value, loadedinvoiceid),
                )
                con.commit()
                updatedrows = c.rowcount
                con.close()

                if updatedrows == 0:
                    ui.notify("invoice update failed", color="red")
                else:
                    ui.notify("invoice updated", color="green")

            ui.button("Add to list", on_click=lambda: add_purchase(purchases)).classes("btn w-30")
            ui.button("Clear purchase list", color="red", on_click=clear_purchase_list).classes("btn w-50 text-white rounded-lg")
            ui.button("Save Changes", color="black", on_click=update_invoice).classes("btn w-50 text-white rounded-lg")
            ui.button("Clear Fields", color="red", on_click=clear_fields).classes("btn w-50 text-white rounded-lg")

@ui.page("/")
def add_user():
    top(page="addusers")
    ui.add_css("""
    .btn {
        background-color: #000000;
        border: none;
        color: white;
        padding: 10px 24px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        text-align: center;
    }""")
    with ui.column().classes("w-full items-center"):
        with ui.card().classes("w-50 items-center justify-center"):
            ui.label("Add User Page")
        with ui.card().classes("w-50 items-center justify-center"):
            ui.label("fullname:")
            fullname=ui.input("fullname", validation=lambda v: "must contain a space between first and last name" if not has_space(v) and range_check(v, 3, 30) else None,)
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
                conn = sqlite3.connect("gmvets.db")
                c = conn.cursor()
                passwordhash = password_hash(password.value)
                #creates user and user profile tables if not exist
                c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
                c.execute("CREATE TABLE IF NOT EXISTS user_profiles (id INTEGER PRIMARY KEY AUTOINCREMENT, fullname TEXT, username TEXT, email TEXT, phone TEXT, gender TEXT, wage TEXT, paid TEXT)")
                #presence check for all fields to prevent empty fields being added to the db 
                if not (fullname.value and username.value and passwordhash and email.value and phone.value and wage.value):
                    ui.notify("Please fill in all fields.", color="red")
                    return
                
                
                #uniqueness check for username to prevent duplication
                c.execute("SELECT username FROM users")
                usernames = c.fetchall()
                onefound = 0
                for i in range(len(usernames)):
                    if username.value == usernames[i][0]:
                        onefound = 1
                        break

                if onefound == 1:
                    conn.close()
                    ui.notify("That username already exists.", color="red")
                    return

                #inserts user data into the db then clears fields
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username.value, passwordhash))
                c.execute("INSERT INTO user_profiles (fullname, username, email, phone, gender, wage, paid) VALUES (?, ?, ?, ?, ?, ?, ?)", (fullname.value, username.value, email.value, phone.value, gender.value, wage.value, str(paid.value)))
                conn.commit()
                conn.close()
                ui.notify("User added successfully!", color="green")
            ui.button("Add User", on_click=handle_user_submit).classes("btn w-30")
            ui.add_css("""
#defaults

:root{
  --background: radial-gradient(circle, #0A0654 0%,#0C0765 20%, #000000 100%);
  --card: #f3f4f6;
  --text: #000000;
}
body { 
    background: var(--background) !important; 
    background-attachment: fixed;
    color: var(--text); 
}
.card, .q-card { 
    background-color: var(--card) !important; 
    color: var(--text) !important; 
}
""", shared=True)
#credit to https://stackoverflow.com however i have modified it to fit my needs and have lost the original question link although it only led to the theme change part i made the other parts through various code snippets
@ui.page('/settings')
def settings():
    top(page="settings")
    def theme_change(e):
        
        if e.value == "default":
            ui.add_css(""":root{
            --background: radial-gradient(circle, #0A0654 0%,#0C0765 20%, #000000 100%);
            --card: #f3f4f6;
            --text: #000000;
            
            }""", shared=True)
        elif e.value == "glowing":
            ui.add_css(""":root{
           --background: radial-gradient(circle,#333333 25%, #0b0f1a 100%);
        --card: #f0f0f0;
        --text: #000000;
        
        }""", shared=True)
        elif e.value == "ocean":
            ui.add_css(""":root{
            --background: radial-gradient(circle,#2b7a78,#0b3d4a);
            --card: #f0f0f0;
            --text: #032b36;
            .dropdown-content{background-color: #1f1f1f !important;
            color: #000000 !important;
            background-color: #000000 !important;}
            
        }""", shared=True)
        elif e.value=="dark":
            ui.add_css(""":root{
            --background: radial-gradient(circle, #000000 0%,#000000 20%, #000000 100%);
            --card: #1f1f1f;
            --text: #000000;
            .dropdown-content{background-color: #1f1f1f !important;
            color: #000000 !important;}
            background-color: #000000 !important;
        }""", shared=True)
    def text_size_change(e):
        
        if e.value == "small":
            ui.add_css(""":root{
            --text: #000000;
            font-size: 14px;
        }""", shared=True)
        elif e.value == "medium":
            ui.add_css(""":root{
            --text: #000000;
            font-size: 16px;
        }""", shared=True)
        elif e.value == "large":
            ui.add_css(""":root{
            --text: #000000;
            font-size: 18px;
        }""", shared=True)    
    with ui.card().classes("w-128 whiteglow items-center justify-center"):
        with ui.row():
            ui.select(["default", "glowing", "ocean","dark"], label="theme", on_change=lambda e: theme_change(e)).classes("w-50  whiteglow").props("outlined bg-color:dark ")
            ui.select(["small", "medium", "large"], label="Text Size", on_change=lambda e: text_size_change(e)).classes("w-50 whiteglow").props("outlined bg-color:dark ")
ui.run("greenmount vets-add", storage_secret="mysecretkey")
