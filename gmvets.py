from nicegui import ui 

import sqlite3

import random

import time

import datetime
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
   
def isdate(date_str):
    try:
        datetime.datetime.strptime(date_str, '%m/%y')
        return True
    except ValueError:
        return False
def moving():
    ui.navigate.to("/main_menu")
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
def moving_to_settings():
    ui.navigate.to("/settings")
def top(islogin):
      #credit for the below belongs to https://css-generators.com/ribbon-shapes/
        ui.add_css("""
        
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
}""")
        if islogin==False:#if user is logged in show this version of the top bar
            with ui.button().classes(" card  w-full items-center justify-center ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);").on_click(moving):
                ui.image("https://i.ibb.co/cSPStcvF/gmvets-final-removebg-preview.jpg").classes("w-19 h-15 absolute left-4 top-1/2 -translate-y-1/2 vertical-align:middle")
                with ui.row().classes("w-full justify-center items-center"):
                    ui.label("Greenmount Vets").classes("text-black text-5xl font-bold")
            with ui.column().classes("w-full h-10 items-center justify-center"):

                with ui.card().classes("ribbon vw-75 items-center justify-center  ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
                    ui.label("Healing Paws, Healing Hearts").classes("text-black")
        else: #if user is not logged in show this version of the top bar
             with ui.button().classes(" card  w-full items-center justify-center ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);").on_click(moving):
                ui.image("https://i.ibb.co/cSPStcvF/gmvets-final-removebg-preview.jpg").classes("w-19 h-15 absolute left-4 top-1/2 -translate-y-1/2 vertical-align:middle")
                with ui.row().classes("w-full justify-center items-center"):
                    ui.label("Greenmount Vets").classes("text-black text-5xl font-bold")
             with ui.column().classes("w-full h-10 items-center justify-center"):

                with ui.card().classes("ribbon vw-75 items-center justify-center  ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
                    ui.label("Healing Paws, Healing Hearts").classes("text-black")           
@ui.page("/reports")
def reports():
    top(islogin=False)
@ui.page("/calendar")
def calendar():
    top(islogin=False)

    try:
        ctime=time.localtime()
    except:  # noqa: E722
        ui.alert("error obtaining the time")
    try:    
        currentdate = time.strftime("%Y-%m-%d", ctime)  
    except:  # noqa: E722
        ui.alert("error obtaining the date ")
    with ui.column().classes("w-full align-items:center"):
        ui.date(value=f"{currentdate}", on_change=lambda e: result.set_text(e.value))
    result = ui.label()
@ui.page("/invoices/create")
def create_invoice():
    def clear_fields():
        ui.notify("fields cleared")
        custid.value=""
        fname.value=""
        sname.value=""
        pnum.value=""
        email.value=""
        creditcard.value=""
        expirydate.value=""
        purchases.value="medicine"
        
    top(islogin=False)
    ui.space()
    with ui.column().classes("w-full items-center"):
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("customer name")
            with ui.row():
                custid=ui.input("customer ID(blank=new)", validation=lambda v: None if v == "" or v is None else ("must be 12 numbers long and numeric" if not (v.isdigit() and len(v) == 12) else None)).classes("w-50")
                ui.space().classes("w-9")
                fname=ui.input("forename", validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not rangecheck(v, 3, 15) else None)
                ui.space().classes("w-9")   
                sname=ui.input("surname",  validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not rangecheck(v, 3, 15) else None) 
                ui.space().classes("w-9")   
                pnum=ui.input("phone number", validation=lambda v: "must be 11 digits long and only contain numbers" if not (len(v) == 11 and v.isdigit()) else None) 
                ui.space().classes("w-9")
                email=ui.input("email address", validation=lambda v: "must contain an @ and a . " if not ("@" in v and "." in v) else None)
                ui.space().classes("w-9")
            with ui.row():
                creditcard=ui.input("credit(or debit) card number", validation=lambda v: "must be 16 digits long and only contain numbers" if not (len(creditcard.value) == 16 and creditcard.value.isdigit()) else None)
                ui.space().classes("w-9")
                expirydate=ui.input("expiry date", validation=lambda v: "must be in the format mm/yy" if isdate(expirydate.value) == False else None   )
            ui.space()
        with ui.card().classes("w-85 items-center justify-center").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("purchases")
            purchaselist = []
            purchaseoptions=["medicine","Carprofen - £25.50", "Meloxicam - £18.75", "Furosemide - £12.40", "Amoxicillin - £15.90", "Metronidazole - £14.20", "Prednisolone - £9.80", "Gabapentin - £22.60", "Enrofloxacin - £19.50", "Clindamycin - £16.30", "Pimobendan - £34.00"]
            purchaseslabel = ui.label("current purchases: none")
            def add_purchase(sel, label):
                val = sel.value
                if val:
                    purchaselist.append(val)
                    label.set_text(", ".join(purchaselist))
            ui.label("select a purchase and click \"Add to list\"")
            purchases = ui.select(purchaseoptions, with_input=True,value="medicine").style("box-shadow: 2px 2px 5px 0px rgba(100,123,238, 0.625);").props("outlined")
            ui.button("Add to list", on_click=lambda: add_purchase(purchases, purchaseslabel)).classes("btn w-30")
            ui.button("Make Invoice", color="black", on_click=lambda:handle_invoice_submit(custid.value, fname.value, sname.value, pnum.value, email.value, creditcard.value, expirydate.value, ",".join(purchaselist))).classes("btn w-50 text-white rounded-lg")

            def handle_invoice_submit(custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist):
                con=sqlite3.connect("gmvets.db")
                c=con.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS invoices (custid TEXT, fname TEXT, sname TEXT, pnum TEXT, email TEXT, creditcard TEXT, expirydate TEXT, purchaselist TEXT)")
                c.execute("INSERT INTO invoices (custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist))
                con.commit()
                con.close()
@ui.page("/invoices/read")  
def readinvoice():      
    top(islogin=False)
    ui.space()
    ui.label("Read an Invoice")
@ui.page("/invoices")
def invoice():
    top(islogin=False)
    ui.space()
    with ui.column().classes("w-full h-screen items-center justify-center"):

        with ui.card().classes("w-96 rounded-lg items-center p-8").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);") :
        

            ui.button("Make An Invoice", color="black", on_click=moving_to_invoices_create).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Read Invoices", color="black", on_click=moving_to_invoices_read).classes("btn w-50 text-white rounded-lg")

@ui.page("/booking")
def booking():
    global species
    top(islogin=False)
    def set_species(e):
        global species
        species = e.value
        ui.notify("species changed")
    def clearfields():# as
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
        global species
        species="other"
        ui.notify("species changed")
    def functiontomakecustomerid(custid):
        if custid == "" or custid is None:
            custid = f"{random.randint(100000000000, 999999999999)}"
        return custid

    def formsubmit(custid, species, fname, sname, pnum, email, petname, petinfo, staffuname, date):
        if custid == "" or custid is None:
            custid = functiontomakecustomerid(custid)
        
        c = sqlite3.connect("gmvets.db")
        cur = c.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS bookings(customerid TEXT,species TEXT,fname TEXT,sname TEXT,pnum TEXT,email TEXT,petname TEXT, date TEXT,petinfo TEXT, staffuname TEXT)")
        
        cur.execute("INSERT INTO bookings(customerid,species,fname,sname,pnum,email,petname,date,petinfo, staffuname) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (custid, species, fname, sname, pnum, email, petname, date, petinfo, staffuname))
        c.commit()
        c.close()
        ui.notify("booking added",color="green")
    
    try:
        ctime=time.localtime()#get current time(c is for current)
    except: 
        ui.alert("error obtaining the time")
        ctime=time.gmtime()
    try:    
        currentdate = time.strftime("%Y-%m-%d", ctime)  
    except:  # noqa: E722
        ui.alert("error obtaining the date ")
    try:
        currentyear, currentmonth, currentday=currentdate.split("-")
        nextyearjustyear=int(currentyear)+1
        nextyear=f"{nextyearjustyear}-{currentmonth}-{currentday}"
        
    except:
        ui.notify("pass")
    with ui.column().classes("w-full items-center"):
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("customer name")
            with ui.row():
                custid=ui.input("customer ID(blank=new)", validation=lambda v: "must be 12 numbers long" if not (len(custid.value)) == 12 and custid.value.isdigit() or custid.value=="" or custid==None else None).classes("w-50") 
                ui.space().classes("w-9")
                fname=ui.input("forename", validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not rangecheck(fname.value, 3, 15) else None)
                ui.space().classes("w-9")   
                sname=ui.input("surname",  validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not rangecheck(sname.value, 3, 15) else None) 
                ui.space().classes("w-9")   
                pnum=ui.input("phone number", validation=lambda v: "must be 11 digits long and only contain numbers" if not (len(pnum.value) == 11 and pnum.value.isdigit()) else None) 
                ui.space().classes("w-9")
                email=ui.input("email address", validation=lambda v: "must contain an @ and a . " if not ("@" in email.value and "." in email.value) else None)
                ui.space().classes("w-9")
        ui.space()
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("pet name")
            with ui.row():
                petname=ui.input("name")
                ui.space().classes("w-9")   
                
                ui.select(["cat","dog","rabbit","other"], label="species", on_change=set_species).classes("w-50")
            petinfo=ui.textarea("notes include any other relevant information\n here").classes("w-full")
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label ("booking info")
            with ui.column():
                date=ui.date_input(value=f"{currentdate}", on_change=lambda e: result.set_text(e.value))
        result = ui.label()
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("staff ID")
            staffuname=ui.input("enter user name", )
            
        with ui.card().classes("card width:50%").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            
            ui.button("submit",color="black",on_click=lambda: formsubmit(custid.value,species,fname.value,sname.value,pnum.value,email.value,petname.value,petinfo.value,staffuname.value,date.value)).classes("btn").props("rounded")
            ui.button("clear",color="red",on_click=clearfields()).classes("btn")

        
            


@ui.page("/main_menu")
def main():
    
    
    top(islogin=False)   
    
    with ui.column().classes("w-full h-screen items-center justify-center"):

        with ui.card().classes("w-96 rounded-lg items-center p-8").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);") :
        

            ui.button("Make A Booking", color="black", on_click=moving_to_booking).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Invoices", color="black", on_click=moving_to_invoices ).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Calendar", color="black",on_click=moving_to_calendar).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Reports", color="black", on_click=moving_to_report).classes("btn w-50 text-white rounded-lg")
            

#this is the main login, currently does"t do anything but output the username and password to the card
@ui.page("/")
def login():
    global username
    ui.add_head_html("""
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;500;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css" rel="stylesheet" />
""", shared=True)

#                                   css
#i have put each item in an individual  ui.add css so it is more readable
    

 
    ui.add_css(""".whiteglow{box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625)}""", shared=True)
    
    
    
    def handle_submit():
        usernameval=username.value
    
        passwordval=password.value
        
        ct=sqlite3.connect("gmvets.db")
        try:
            cur=ct.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)""")

            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (f"{usernameval}", f"{passwordval}"))

            ct.commit()

            cur.execute("SELECT * FROM users")

            rows = cur.fetchall()

            for row in rows:

                if rows != ():

                    ui.label(row)

            cur.close()

            ct.close()
            moving()
        except:  # noqa: E722
            moving()
        
        
    
    
    
    top(islogin=True)
    
    with ui.column().classes("w-full h-screen items-center justify-center"):
        
        with ui.card().classes("w-96 whiteglow shadow-xl items-center p-8"):
        
            ui.label("login").classes("text-2xl mb-4")
        
            username = ui.input("username").classes("w-full")
        
            ui.separator().classes("w-full border-gray-400 my-4")
        
            password = ui.input("password", password=True).classes("w-full")
        
            ui.space().classes("h-8")

            ui.button("submit", color="black", on_click=handle_submit).classes("btn text-white rounded-lg")

ui.add_css("""
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
#credit to https://stackoverflow.com however i have modified it to fit my needs and have lost the original question link and it only led to the theme change part i made the other parts through local storage snippets
ui.add_head_html("""
<script>
const THEMES = {
  default: { background: 'radial-gradient(circle, #0A0654 0%,#0C0765 20%, #000000 100%)', card:'#f3f4f6', text:'#000000' },
  glowing: { background: 'radial-gradient(circle,#a9a9a9 25%, #0b0f1a 100%)', card:'#1f2937', text:'#e5e7eb' },
  ocean:   { background: 'radial-gradient(circle,#2b7a78,#0b3d4a)', card:'#dff6f5', text:'#032b36' },
  solar:   { background: 'radial-gradient(circle,#fdf6e3,#fceac9)', card:'#fffaf0', text:'#5b2a06' },
  dark:    { background: 'radial-gradient(circle, #1a1a1a 0%, #000000 100%)', card:'#2d2d2d', text:'#f5f5f5' }
};
function applyTheme(name){
  const t = THEMES[name] || THEMES.default;
  const r = document.documentElement.style;
  r.setProperty('--background', t.background);
  r.setProperty('--card', t.card);
  r.setProperty('--text', t.text);
  localStorage.setItem('gmvets_theme', name);
}
document.addEventListener('DOMContentLoaded', ()=> {
  const saved = localStorage.getItem('gmvets_theme') || 'default';
  applyTheme(saved);
});
</script>
""", shared=True)
@ui.page('/settings')
def settings():
    top(islogin=False)
    with ui.column().classes('w-full items-center'):
        with ui.card():
            ui.label('Theme')
            theme = ui.select(['default', 'glowing', 'ocean', 'solar', 'dark'], value='default').classes('w-48')
        ui.row()
        ui.button('Apply', on_click=lambda: ui.run_javascript(f"applyTheme('{theme.value}');")).classes('btn')
ui.run()