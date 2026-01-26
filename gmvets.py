from nicegui import ui 

import sqlite3

import random

import time
#globals
dogbreedcalls=0

species="other"
usernameval=""
catbreedinputcalls=0

#functions
def rangecheck(value, low, high):
    if low <= len(value) <= high and not value.isdigit():
        return True
    else:
        return False
def handle_change(input1):
    result=input1.value
    return result
    #these functions handle the input for the dog and cat breed inputs and ensure that only one breed input is shown at a time
def catbreedinput():
    global catbreedinputcalls
    global catbreed
    global species
    if catbreedinputcalls==0:
        catbreed=ui.input("cat breed", on_change=lambda:species==f"cat({catbreed.value})")
        catbreedinputcalls+=1

    else:
        pass
def dogbreedinput():
   
    global dogbreedcalls
    
    global dogbreed
    if dogbreedcalls==0:
        dogbreed=ui.input("dog breed")
        dogbreedcalls+=1
    else:
        pass
def moving():
    ui.navigate.to('/main_menu')
def moving_to_invoices_create():
    ui.navigate.to("/invoices/create")
def moving_to_invoices_read():
    ui.navigate.to("/invoices/read")
def moving_to_booking():
    ui.navigate.to("/booking")
def moving_to_invoices():
    ui.navigate.to("/invoices")
def moving_to_report():
    ui.navigate.to("/reports")
def moving_to_calendar():
    ui.navigate.to("/calendar")
def top():
      #credit for the below belongs to https://css-generators.com/ribbon-shapes/
        ui.add_css('''
        
.ribbon {
  font-size: 28px;
  font-weight: bold;
  color: #fff;
}
.ribbon {
  --s: 1.8em; /* the ribbon size */
  --d: .8em;  /* the depth */
  --c: .8em;  /* the cutout part */
  
  padding: var(--d) calc(var(--s) + .5em) 0;
  line-height: 1.8;
  background:
    conic-gradient(from  45deg at left  var(--s) top var(--d),
     #0008 12.5%,#0000 0 37.5%,#0004 0) 0   /50% 100% no-repeat,
    conic-gradient(from -45deg at right var(--s) top var(--d),
     #0004 62.5%,#0000 0 87.5%,#0008 0) 100%/50% 100% no-repeat;
  clip-path: polygon(0 0,calc(var(--s) + var(--d)) 0,calc(var(--s) + var(--d)) var(--d),calc(100% - var(--s) - var(--d)) var(--d),calc(100% - var(--s) - var(--d)) 0,100% 0, calc(100% - var(--c)) calc(50% - var(--d)/2),100% calc(100% - var(--d)),calc(100% - var(--s)) calc(100% - var(--d)),calc(100% - var(--s)) 100%,var(--s) 100%,var(--s) calc(100% - var(--d)),0 calc(100% - var(--d)),var(--c) calc(50% - var(--d)/2));
  background-color: #ffffff; /* the main color */
  width: fit-content;
}''')
        with ui.button().classes(" card  w-full items-center justify-center ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);").on_click(moving):
            ui.image("https://i.ibb.co/cSPStcvF/gmvets-final-removebg-preview.jpg").classes("w-19 h-15 absolute left-4 top-1/2 -translate-y-1/2 vertical-align:middle")
            with ui.row().classes("w-full justify-center items-center"):
                ui.label("Greenmount Vets").classes("text-black text-5xl font-bold")
        with ui.column().classes("w-full h-10 items-center justify-center"):

            with ui.card().classes("ribbon vw-75 items-center justify-center  ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
                ui.label("Healing Paws, Healing Hearts").classes("text-black")
@ui.page('/reports')
def reports():
    top()
@ui.page('/calendar')
def calendar():
    top()

    try:
        c_time=time.localtime()
    except:  # noqa: E722
        ui.alert("error obtaining the time")
    try:    
        current_date = time.strftime("%Y-%m-%d", c_time)  
    except:  # noqa: E722
        ui.alert("error obtaining the date ")
    with ui.column().classes("w-full align-items:center"):
        ui.date(value=f"{current_date}", on_change=lambda e: result.set_text(e.value))
    result = ui.label()
@ui.page('/invoices/create')
def createinvoice():
    top()
    ui.space()
    with ui.column().classes("w-full items-center"):
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("customer name")
            with ui.row():
                custid=ui.input("customer ID(blank=new)", validation=lambda v: 'must be 12 numbers long' if not (len(custid.value)) == 12 and custid.value.isdigit() or custid.value=="" or custid==None else None).classes("w-50") 
                ui.space().classes("w-9")
                fname=ui.input("forename", validation=lambda v: 'must be between 3 and 15 letters long if your name is too long use a shortening' if not rangecheck(fname.value, 3, 15) else None)
                ui.space().classes("w-9")   
                sname=ui.input("surname",  validation=lambda v: 'must be between 3 and 15 letters long if your name is too long use a shortening' if not rangecheck(sname.value, 3, 15) else None) 
                ui.space().classes("w-9")   
                pnum=ui.input("phone number", validation=lambda v: 'must be 11 digits long and only contain numbers' if not (len(pnum.value) == 11 and pnum.value.isdigit()) else None) 
                ui.space().classes("w-9")
                email=ui.input("email address", validation=lambda v: 'must contain an @ and a . ' if not ('@' in email.value and '.' in email.value) else None)
                ui.space().classes("w-9")
            with ui.row():
                creditcard=ui.input("credit(or debit) card number", validation=lambda v: 'must be 16 digits long and only contain numbers' if not (len(creditcard.value) == 16 and creditcard.value.isdigit()) else None)
                ui.space().classes("w-9")
                expirydate=ui.input("expiry date", validation=lambda v: 'must be in the format dd/mm/yyyy' if not (len(expirydate.value) == 8 and expirydate.value.isalnum()) else None)
            ui.space()
        with ui.card().classes("w-50 items-center justify-center").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("purchases")
            purchase_list = []
            
            
            def handle_purchase(purchases):
                val = purchases.value
                ui.label(val)
                if val:
                    purchase_list.append(val)
                    purchases.set_value('')
                    return purchase_list
            
            purchases_str=",".join(purchase_list)
            purchase=" "
            purchases = ui.input("list your purchases and press enter after each purchase").on("keydown.enter", lambda:purchase==handle_purchase(purchases))
            ui.button("Make Invoice", color="black", on_click=lambda:handle_invoice_submit(custid.value, fname.value, sname.value, pnum.value, email.value, creditcard.value, expirydate.value, purchases_str)).classes("btn w-50 text-white rounded-lg")

            def handle_invoice_submit(custid, fname, sname, pnum, email, creditcard, expirydate, purchase_list):
                con=sqlite3.connect("invoices.db")
                c=con.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS invoices (custid TEXT, fname TEXT, sname TEXT, pnum TEXT, email TEXT, creditcard TEXT, expirydate TEXT, purchase_list TEXT)")
                c.execute("INSERT INTO invoices (custid, fname, sname, pnum, email, creditcard, expirydate, purchase_list) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (custid, fname, sname, pnum, email, creditcard, expirydate, purchase_list))
                con.commit()
                con.close()
@ui.page('/invoices/read')  
def readinvoice():      
    top()
    ui.space()
    ui.label("Read an Invoice")
@ui.page('/invoices')
def invoice():
    top()
    ui.space()
    with ui.column().classes('w-full h-screen items-center justify-center'):

        with ui.card().classes('w-96 rounded-lg  bg-gray-100 items-center p-8').style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);") :
        

            ui.button("Make An Invoice", color="black", on_click=moving_to_invoices_create).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Read Invoices", color="black", on_click=moving_to_invoices_read).classes("btn w-50 text-white rounded-lg")

@ui.page('/booking')
def booking():
    global species
    top()
    def clearfields():
        global species
        custid.value =""
        species=""
        fname.value=""
        sname.value=""
        pnum.value=""
        email.value=""
        petname.value=""
        petinfo.value=""
    def iscat():
        global species
        species="cat"
        ui.notify("species changed")
        
    def isdog():
        global species
        species="dog"
        ui.notify("species changed")
    def israbbit():
        global species
        species="rabbit"
        ui.notify("species changed")
    def isother():
        species="other"
    def functiontomakecustomerid(custid):
        if custid == "" or custid is None:
            custid = f"{random.randint(100000000000, 999999999999)}"
        return custid

    def formsubmit(custid, species, fname, sname, pnum, email, petname, petinfo, staffuname, date):
        if custid == "" or custid is None:
            custid = functiontomakecustomerid(custid)
        
        c = sqlite3.connect("booking.db")
        cur = c.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS bookings(customerid TEXT,species TEXT,fname TEXT,sname TEXT,pnum TEXT,email TEXT,petname TEXT, date TEXT,petinfo TEXT, staffuname TEXT)")
        
        cur.execute("INSERT INTO bookings(customerid,species,fname,sname,pnum,email,petname,date,petinfo, staffuname) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (custid, species, fname, sname, pnum, email, petname, date, petinfo, staffuname))
        c.commit()
        c.close()
        ui.notify("booking added",color="green")
    
    try:
        c_time=time.localtime()
    except:  # noqa: E722
        ui.alert("error obtaining the time")
    try:    
        current_date = time.strftime("%Y-%m-%d", c_time)  
    except:  # noqa: E722
        ui.alert("error obtaining the date ")
    try:
        current_year, current_month, current_day=current_date.split("-")
        next_year_just_year=int(current_year)+1
        next_year=f"{next_year_just_year}-{current_month}-{current_day}"
        
    except:
        ui.notify("pass")
    with ui.column().classes("w-full items-center"):
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("customer name")
            with ui.row():
                custid=ui.input("customer ID(blank=new)", validation=lambda v: 'must be 12 numbers long' if not (len(custid.value)) == 12 and custid.value.isdigit() or custid.value=="" or custid==None else None).classes("w-50") 
                ui.space().classes("w-9")
                fname=ui.input("forename", validation=lambda v: 'must be between 3 and 15 letters long if your name is too long use a shortening' if not rangecheck(fname.value, 3, 15) else None)
                ui.space().classes("w-9")   
                sname=ui.input("surname",  validation=lambda v: 'must be between 3 and 15 letters long if your name is too long use a shortening' if not rangecheck(sname.value, 3, 15) else None) 
                ui.space().classes("w-9")   
                pnum=ui.input("phone number", validation=lambda v: 'must be 11 digits long and only contain numbers' if not (len(pnum.value) == 11 and pnum.value.isdigit()) else None) 
                ui.space().classes("w-9")
                email=ui.input("email address", validation=lambda v: 'must contain an @ and a . ' if not ('@' in email.value and '.' in email.value) else None)
                ui.space().classes("w-9")
        ui.space()
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("pet name")
            with ui.row():
                petname=ui.input("name")
                ui.space().classes("w-9")   
                with ui.dropdown_button("species").classes("bg-black").props("rounded") :
                    ui.item("cat", on_click=catbreedinput).on("click", iscat)
                    ui.item("dog", on_click=dogbreedinput).on("click", isdog)
                    ui.item("rabbit", on_click=israbbit)
                    ui.item("other", on_click=lambda: ui.notify("please specify in notes")).on("click", isother)
            petinfo=ui.textarea("notes include any other relevant information\n here").classes("w-full")
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label ("booking info")
            with ui.column():
                date=ui.date_input(value=f"{current_date}", on_change=lambda e: result.set_text(e.value))
        result = ui.label()
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("staff ID")
            staffuname=ui.input("enter user name", )
            
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            
            ui.button("submit",color="black",on_click=lambda: formsubmit(custid.value,species,fname.value,sname.value,pnum.value,email.value,petname.value,petinfo.value,staffuname.value,date.value)).classes("btn").props("rounded")
        

        
            


@ui.page('/main_menu')
def main():
    
    
    top()   
    
    with ui.column().classes('w-full h-screen items-center justify-center'):

        with ui.card().classes('w-96 rounded-lg  bg-gray-100 items-center p-8').style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);") :
        

            ui.button("Make A Booking", color="black", on_click=moving_to_booking).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Invoices", color="black", on_click=moving_to_invoices ).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Calendar", color="black",on_click=moving_to_calendar).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Reports", color="black", on_click=moving_to_report).classes("btn w-50 text-white rounded-lg")
            

#this is the main login, currently does't do anything but output the username and password to the card
@ui.page('/')
def login():
    global username
    ui.add_head_html('''
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;500;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css" rel="stylesheet" />
''', shared=True)

#                                   css
#i have put each item in an individual  ui.add css so it is more readable
    ui.add_css('''
body {
    background: radial-gradient(circle, #0A0654 0%,#0C0765 20%, #000000 100% );
    font-family: "DM Sans", sans-serif;
}
''', shared=True) 
    ui.add_css('''.whiteglow{box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625)}''', shared=True)
    
    
    
    def handle_submit():
        usernameval=username.value
    
        passwordval=password.value
        
        ct=sqlite3.connect("username_password.db")
        try:
            cur=ct.cursor()

            cur.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')

            cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (f"{usernameval}", f"{passwordval}"))

            ct.commit()

            cur.execute('SELECT * FROM users')

            rows = cur.fetchall()

            for row in rows:

                if rows != ():

                    ui.label(row)

            cur.close()

            ct.close()
            moving()
        except:  # noqa: E722
            moving()
        
        
    
    
    
    top()
    
    with ui.column().classes('w-full h-screen items-center justify-center'):
        
        with ui.card().classes('w-96 whiteglow shadow-xl bg-gray-100 items-center p-8'):
        
            ui.label('login').classes('text-2xl mb-4')
        
            username = ui.input('username').classes('w-full')
        
            ui.separator().classes('w-full border-gray-400 my-4')
        
            password = ui.input('password', password=True).classes('w-full')
        
            ui.space().classes('h-8')

            ui.button("submit", color="black", on_click=handle_submit).classes("btn text-white rounded-lg")

ui.run()