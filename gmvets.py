#my coding project for my computer science a level.
from nicegui import ui , app

import sqlite3

import random

import time

import datetime
#globals
usernameval=""


#functions
def column_as_list( table, column):
    conn = sqlite3.connect('gmvets.db')
    cur = conn.cursor()
    cur.execute(f"SELECT {column} FROM {table}")
    vals = ["" if v[0] is None else str(v[0]) for v in cur.fetchall()]
    conn.close()
    return vals
def range_check(value, low, high):
    if low <= len(value) <= high and not value.isdigit():
        return True
    else:
        return False
def mmyy_format(datestr):
    try:
        mm,yy = datestr.split("/")
        validmonths=["1","2","3","4","5","6","7","8","9","10","11","12","01","02","03","04","05","06","07","08","09"]
        validyears=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99"]# ai use declaration. prompt:list every number from 00-99 in a comma separated list with speech marks around each number
        if mm not in validmonths:
            return False
        elif yy not in validyears:
            return False
        else:
            return True
    except ValueError:
        return False
def handle_change(input1):
    result=input1.value
    return result
   
def is_date(datestr):
    try:
        datetime.datetime.strptime(datestr, '%m/%y')
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
            with ui.button().classes(" card  w-full items-center justify-center whiteglow").on_click(moving):
                ui.image("https://i.ibb.co/cSPStcvF/gmvets-final-removebg-preview.jpg").classes("w-19 h-15 absolute left-4 top-1/2 -translate-y-1/2 vertical-align:middle")
                with ui.row().classes("w-full justify-center items-center"):
                    ui.label("Greenmount Vets").classes("text-black text-5xl font-bold")
            with ui.column().classes("w-full h-10 items-center justify-center"):

                with ui.card().classes("ribbon vw-75 items-center justify-center  whiteglow"):
                    ui.label("Healing Paws, Healing Hearts").classes("text-black")
        else: #if user is not logged in show this version of the top bar
             with ui.button().classes(" card  w-full items-center justify-center whiteglow"):
                ui.image("https://i.ibb.co/cSPStcvF/gmvets-final-removebg-preview.jpg").classes("w-19 h-15 absolute left-4 top-1/2 -translate-y-1/2 vertical-align:middle")
                with ui.row().classes("w-full justify-center items-center"):
                    ui.label("Greenmount Vets").classes("text-black text-5xl font-bold")
             with ui.column().classes("w-full h-10 items-center justify-center"):

                with ui.card().classes("ribbon vw-75 items-center justify-center whiteglow"):
                    ui.label("Healing Paws, Healing Hearts").classes("text-black")           
@ui.page("/reports")
def reports():
    top(islogin=False)
    ui.space()
@ui.page("/calendar")
def calendar():
    top(islogin=False)
    datelist = column_as_list("bookings", "date")
    try:
        ctime=time.localtime()
    except:  # noqa: E722
        ui.alert("error obtaining the time")
    try:    
        currentdate = time.strftime("%Y-%m-%d", ctime)  
    except:  # noqa: E722
        ui.alert("error obtaining the date ")
    with ui.column().classes("w-full align-items:center"):
        ui.date(value=f"{currentdate}", on_change=lambda e: handle_change(e)).classes("w-50 whiteglow")
        result = ui.label()
        results_container = ui.column()
        
        def handle_change(input1):
            results_container.clear()
            selected_date = input1.value
            result.set_text(selected_date)
            
            # Get all booking data once
            fnames = column_as_list('bookings', 'fname')
            snames = column_as_list('bookings', 'sname')
            species_list = column_as_list('bookings', 'species')
            staffunames = column_as_list('bookings', 'staffuname')
            
            onefound = 0
            for i in range(len(datelist)):
                if selected_date == datelist[i]:
                    ui.label(f"booking: {fnames[i]} {snames[i]} for a {species_list[i]} booked by staff member {staffunames[i]}").classes("card w-50 whiteglow")
                    onefound += 1
                elif datelist[i] == "":
                    break
            
            if onefound == 0:
                ui.label("no bookings for this date").classes("card w-50 whiteglow")    
        
        
@ui.page("/invoices/create")
def create_invoice():
    top(islogin=False)
    ui.space()
    with ui.column().classes("w-full items-center"):
        with ui.card().classes("card width:50% whiteglow"):
            ui.label("customer name")
            with ui.row():
                custid=ui.input("customer ID(blank=new)", validation=lambda v: None if v == "" or v is None else ("must be 12 numbers long and numeric" if not (v.isdigit() and len(v) == 12) else None)).classes("w-50")
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
                creditcard=ui.input("credit(or debit) card number", validation=lambda v: "must be 16 digits long and only contain numbers" if not (len(creditcard.value) == 16 and creditcard.value.isdigit()) else None)
                ui.space().classes("w-9")
                expirydate=ui.input("expiry date", validation=lambda v: "must be in the format mm/yy" if mmyy_format(expirydate.value) == False else None   )
            ui.space()
        with ui.card().classes("w-85 whiteglow items-center justify-center"):
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
            purchases = ui.select(purchaseoptions, with_input=True,value="medicine").classes("w-50 whiteglow").props("outlined color=black")
            
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
                purchaselist.clear()
                purchaseslabel.set_text("current purchases: none")
            
            ui.button("Add to list", on_click=lambda: add_purchase(purchases, purchaseslabel)).classes("btn w-30")
            ui.button("Make Invoice", color="black", on_click=lambda:handle_invoice_submit(custid.value, fname.value, sname.value, pnum.value, email.value, creditcard.value, expirydate.value, ",".join(purchaselist))).classes("btn w-50 text-white rounded-lg")
            ui.button("Clear Fields", color="red", on_click=clear_fields).classes("btn w-50 text-white rounded-lg")

            def handle_invoice_submit(custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist):
                con=sqlite3.connect("gmvets.db")
                c=con.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS invoices (custid TEXT, fname TEXT, sname TEXT, pnum TEXT, email TEXT, creditcard TEXT, expirydate TEXT, purchaselist TEXT)")
                c.execute("INSERT INTO invoices (custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist))
                con.commit()
                con.close()
                clear_fields()
                ui.notify("Invoice created", color="green")
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

        with ui.card().classes("w-96 rounded-lg whiteglow items-center p-8"):
        

            ui.button("Make An Invoice", color="black", on_click=moving_to_invoices_create).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Read Invoices", color="black", on_click=moving_to_invoices_read).classes("btn w-50 text-white rounded-lg")

@ui.page("/booking")
def booking():
    global species
    global usernameval
    top(islogin=False)
    def set_species(e):
        global species
        species = e.value
        ui.notify("species changed")
    
    
    

    def formsubmit(custid, species, fname, sname, pnum, email, petname, petinfo, staffuname, date):
        if custid == "" or custid is None:
            custid = functiontomakecustomerid(custid, "fname", "sname", "petname")
        
        c = sqlite3.connect("gmvets.db")
        cur = c.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS bookings(customerid TEXT,species TEXT,fname TEXT,sname TEXT,pnum TEXT,email TEXT,petname TEXT, date TEXT,petinfo TEXT, staffuname TEXT)")
        
        cur.execute("INSERT INTO bookings(customerid,species,fname,sname,pnum,email,petname,date,petinfo, staffuname) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (custid, species, fname, sname, pnum, email, petname, date, petinfo, staffuname))
        c.commit()
        c.close()
        ui.notify("booking added",color="green")
        clear_booking_fields()
    
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
        with ui.card().classes("card width:50% whiteglow"):
            
            ui.label(f"customer name")
            with ui.row():
                custid=ui.input("customer ID(blank=new)", validation=lambda v: "must be 12 numbers long" if not (len(custid.value)) == 12 and custid.value.isdigit() or custid.value=="" or custid==None else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")
                fname=ui.input("forename", validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not range_check(fname.value, 3, 15) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")   
                sname=ui.input("surname",  validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not range_check(sname.value, 3, 15) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")   
                pnum=ui.input("phone number", validation=lambda v: "must be 11 digits long and only contain numbers" if not (len(pnum.value) == 11 and pnum.value.isdigit()) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")
                email=ui.input("email address", validation=lambda v: "must contain an @ and a . " if not ("@" in email.value and "." in email.value) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")
        ui.space()
        with ui.card().classes("card width:50% whiteglow"):
            ui.label("pet name")
            with ui.row():
                petname=ui.input("name")
                ui.space().classes("w-9")   
                
                ui.select(["cat","dog","rabbit","other"], label="species", on_change=set_species).classes("w-50")
            petinfo=ui.textarea("notes include any other relevant information\n here").classes("w-full")
        with ui.card().classes("card width:50% whiteglow"):
            ui.label ("booking info")
            with ui.column():
                date=ui.date_input(value=f"{currentdate}")
        with ui.card().classes("card whiteglow width:50%"):
            ui.label("staff ID")
            staffuname=ui.input("enter user name", )
        def functiontomakecustomerid(custid,fname, sname, petname):
            firstnamelist = column_as_list("bookings", "fname")
            lastnamelist = column_as_list("bookings", "sname")  
            petnamelist = column_as_list("bookings", "petname")
            custidlist= column_as_list("bookings", "customerid")
            for i in range(len(firstnamelist)):#could have put any of the list variables as they are all the same length
                if fname == firstnamelist[i] and sname == lastnamelist[i] and petname == petnamelist[i]:
                    custid = custidlist[i]
                    break
                else:
                    i+=1
            if custid == "" or custid is None:
                custid = f"{random.randint(100000000000, 999999999999)}"
            return custid
        name=app.storage.user.get("username", "unknown user")
        def clear_booking_fields():
            global species
            custid.set_value("")
            species=""
            fname.set_value("")
            sname.set_value("")
            pnum.set_value("")
            email.set_value("")
            petname.set_value("")
            petinfo.set_value("")
            staffuname.set_value("")
        with ui.card().classes("card width:50%").classes("whiteglow"):
            ui.button("submit",color="black",on_click=lambda: formsubmit(custid.value,species,fname.value,sname.value,pnum.value,email.value,petname.value,petinfo.value,name,date.value,)).classes("btn").props("rounded")
            ui.button("clear",color="red",on_click=clear_booking_fields).classes("btn")

        
            


@ui.page("/main_menu")
def main():
    
    top(islogin=False)   
    
    with ui.column().classes("w-full h-screen items-center justify-center"):

        with ui.card().classes("w-96 whiteglow rounded-lg items-center p-8") :
        
            ui.button("Make A Booking", color="black", on_click=moving_to_booking).classes("btn w-50  text-white rounded-lg")
        
            ui.space()
        
            ui.button("Invoices", color="black", on_click=moving_to_invoices ).classes("btn w-50  text-white rounded-lg")
        
            ui.space()
        
            ui.button("Calendar", color="black",on_click=moving_to_calendar).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Reports", color="black", on_click=moving_to_report).classes("btn w-50 text-white rounded-lg")
            
            ui.space()

            ui.button("Settings", color="black", on_click=moving_to_settings).classes("btn w-50 text-white rounded-lg")

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
    
    
    def clear_fields():
        username.value=""
        password.value=""
    def handle_submit():
        global usernameval

        # simple validation
        if not username.value or not password.value:
            ui.notify('Please enter username and password', color='red')
            return

        try:
            conn = sqlite3.connect("gmvets.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
            # check credentials
            cur.execute("SELECT 1 FROM users WHERE username = ? AND password = ?", (username.value, password.value))
            row = cur.fetchone()
            cur.close()
            conn.close()

            if row:
                moving()
                
                app.storage.user['username'] = username.value
            else:
                ui.notify('Invalid username or password — please try again', color='red')
                clear_fields()
        except sqlite3.Error as e:
            ui.notify(f'Database error: {e}', color='red')
            clear_fields()
        
        
    
    
    
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
ui.add_head_html("""
<script>// theme definitions
const THEMES = {
  default: { background: 'radial-gradient(circle, #0A0654 0%,#0C0765 20%, #000000 100%)', card:'#f0f0f0', text:'#000000' },
  glowing: { background: 'radial-gradient(circle,#333333 25%, #0b0f1a 100%)', card:'#f0f0f0', text:'#000000' },
  ocean:   { background: 'radial-gradient(circle,#2b7a78,#0b3d4a)', card:'#f0f0f0', text:'#032b36' },
  sepia:   { background: 'radial-gradient(circle,#fdf6e3,#fceac9)', card:'#808000', text:'#5b2a06' },
  dark:    { background: 'radial-gradient(circle, #1a1a1a 0%, #000000 100%)', card:'#eeeeee', text:'#ffffff' }
};
function applyTheme(name){
  const t = THEMES[name] || THEMES.default;
  const r = document.documentElement.style;
    r.setProperty('--background', t.background); // changes background
    r.setProperty('--card', t.card); // changes card color
    r.setProperty('--text', t.text); // changes text color
    localStorage.setItem('gmvets_theme', name); // saves theme to browser local storage
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
            theme = ui.select(['default', 'glowing', 'ocean', 'sepia', 'dark'], value='default').classes('w-48').props('outlined color=white options-dark')
            ui.space().classes('h-4')
        ui.row()
        ui.button('Apply', on_click=lambda: ui.run_javascript(f"applyTheme('{theme.value}');")).classes('btn')
ui.run(storage_secret="mysecretkey")