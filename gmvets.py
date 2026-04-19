from turtle import title

from nicegui import ui, app


import sqlite3

import random

import time

from validation import mmyy_format, iscreditcard, isemail, range_check, verify_password, password_hash

class User:
    def __init__(self, username):
        self.username = username
        
        #when a user object is created it checks if the username exists and retrieves full profile if so
        usernames = column_as_list("users", "username")
        for i in range(len(usernames)):
            if self.username == usernames[i]:
                ui.add_css("""
                           text{ size: 20px;}""")
                emails = column_as_list("user_profiles", "email")
                self.email = emails[i]
                pnums= column_as_list("user_profiles", "phone")
                self.pnum = pnums[i]
                genders= column_as_list("user_profiles", "gender")
                self.gender = genders[i]
                wages= column_as_list("user_profiles", "wage")
                self.wage= wages[i]
                paid= column_as_list("user_profiles", "paid")
                self.paid = paid[i]
                break
            elif i == len(usernames)-1:
                ui.notify("user not found", color="red")
            else:
                pass
    def display_profile(self):
        with ui.column().classes("w-full items-center justify-center"):
            with ui.card().classes("w-50 whiteglow items-center justify-center"):
                 ui.label(f"username: {self.username}\n\n").classes("text-3xl")
                 
                 ui.separator().classes("w-48")

                 
                 ui.label(f"email: {self.email}")
                 
                 ui.separator().classes("w-48")
                 
                 ui.label(f"phone number: {self.pnum}")
                 
                 ui.separator().classes("w-48")
                 
                 ui.label(f"gender: {self.gender}")
                 
                 ui.separator().classes("w-48")
                 
                 ui.label(f"wage: {self.wage}")
                 
                 ui.separator().classes("w-48")
                 
                 ui.label(f"paid: {self.paid}")        



#non-page functions
def argsfunction(*args):#demonstrating that i can use args and kwargs, this function just adds up all the arguments given to it and returns the total, if any argument isn't an integer it returns an error message
    total = 0
    for arg in args:
        try:
            total += int(arg)
        except ValueError:
            return "Error: One or more arguments are not integers"
    return total
def add_numbers(a: int, b: int) -> int:#just proof i can use type hints
    return a + b

def column_as_list( table, column):#returns column from a given table as a list of strings
    conn = sqlite3.connect('gmvets.db')

    cur = conn.cursor()
    cur.execute(f"SELECT {column} FROM {table}")

    vals = ["" if v[0] is None else str(v[0]) for v in cur.fetchall()]

    conn.close()
    return vals
def unused_length_check(length, var):#i didn't need this function but it demonstrates that i can do it i just prefer inline length checks or to use a range check
    if len(var) < length:
        return False
    else:
        return True
def type_check_to_demonstrate_knowledge(value, expected_type):#i didn't end up using this function but it demonstrates my knowledge of type checking.
    if expected_type == "string":    
        return isinstance(value, str)
    elif expected_type == "integer":
        return isinstance(value, int)
    elif expected_type == "float":
        return isinstance(value, float)
    elif expected_type == "boolean":
        return isinstance(value, bool)
    else:
        raise ValueError("Unsupported type specified")




def handle_change(input1):
    result=input1.value
    return result
   
def is_date(datestr):
    try:
        day,month,year = datestr.split("/")
    # verifies date is formatted dd/mm/yyyy 
        if len (day) != 2 or len(month) != 2 or len(year) != 4 or len(year)!=2 or not day.isdigit() or not month.isdigit() or not year.isdigit():
            return False
        else:
            return True
    except ValueError:
        return False
def moving(page):
    ui.navigate.to(f"/{page}")





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

            with ui.button(on_click=lambda:moving(page="main_menu")).classes(" card  w-full items-center justify-center whiteglow",):
                ui.image("https://i.ibb.co/cSPStcvF/gmvets-final-removebg-preview.jpg").classes("w-19 h-15 absolute left-4 top-1/2 -translate-y-1/2 vertical-align:middle")
                with ui.row().classes("w-full justify-center items-center"):
                    ui.label("Greenmount Vets").classes("text-black text-5xl font-bold")

            with ui.column().classes("w-full h-10 items-center justify-center"):

                with ui.card().classes("ribbon vw-75 items-center justify-center  whiteglow"):
                    ui.label("Healing Paws, Healing Hearts").classes("text-black")

        else: #if user is not logged in show this version of the top bar

             with ui.button().classes(" card  w-full items-center justify-center whiteglow").on_click(lambda:moving(page="main_menu")):

                ui.image("https://i.ibb.co/cSPStcvF/gmvets-final-removebg-preview.jpg").classes("w-19 h-15 absolute left-4 top-1/2 -translate-y-1/2 vertical-align:middle")

                with ui.row().classes("w-full justify-center items-center"):

                    ui.label("Greenmount Vets").classes("text-black text-5xl font-bold")

             with ui.column().classes("w-full h-10 items-center justify-center"):

                with ui.card().classes("ribbon vw-75 items-center justify-center whiteglow"):
                    ui.label("Healing Paws, Healing Hearts").classes("text-black")

@ui.page("/reports/busiest_dates")
def busiest_dates():
    top(islogin=False)
    ui.space()

    with ui.column().classes("w-full items-center justify-center"):
        with ui.card().classes("w-95 items-center justify-center whiteglow"):
            ui.label("busiest dates").classes("text-3xl")
            ui.separator()
            conn = sqlite3.connect("gmvets.db")
            cur = conn.cursor()
            cur.execute("""
                SELECT date, customerid, fname, sname, species, petname, pnum, email, petinfo, staffuname
                FROM bookings
                WHERE date IS NOT NULL AND TRIM(date) != ''
                ORDER BY date ASC, fname ASC, sname ASC
            """)#line 122 selects all data,line 123 selects the table, line 124 performs a presence check on date, line 125 orders the data by date and then by name to ensure appointments on the same date are grouped together and ordered alphabetically

            bookingrows = cur.fetchall()
            conn.close()

            if len(bookingrows) == 0:
                ui.label("no bookings found").classes("text-lg")

            else:
                busiestdates = {}
                for bookingrow in bookingrows: # go through each booking row and group them by date
                    bookingdate = bookingrow[0]

                    if bookingdate not in busiestdates:
                        busiestdates[bookingdate] = []
                    appointmenttext = (

                        f"{bookingdate}\n"

                        f"customer id: {bookingrow[1]}\n"

                        f"name: {bookingrow[2]} {bookingrow[3]}\n"

                        f"species: {bookingrow[4]}\n"

                        f"pet name: {bookingrow[5]}\n"

                        f"phone: {bookingrow[6]}\n"

                        f"email: {bookingrow[7]}\n"

                        f"pet info: {bookingrow[8]}\n"

                        f"staff member: {bookingrow[9]}"
                    )
                    busiestdates[bookingdate].append(appointmenttext)

                #sorts busiest date items
                sortedbusiestdates = sorted(busiestdates.items(), key=lambda dategroup: (-len(dategroup[1]), dategroup[0]))

                tablecolumns = [
                    {"name": "dateandcount", "label": "date and count", "field": "dateandcount", "align": "left"},

                    {"name": "appointmentinfo", "label": "appointments", "field": "appointmentinfo", "align": "left"},
                ]

                tablerows = []

                for dategroup in sortedbusiestdates: # build a table row for each grouped date

                    bookingdate = dategroup[0]

                    appointments = dategroup[1]

                    bookingcount = len(appointments)

                    tablerows.append(
                        {

                            "date": bookingdate,

                            "dateandcount": f"{bookingdate}: {bookingcount}",

                            "appointmentinfo": "\n\n".join(appointments),
                        }
                    )
                ui.table(columns=tablecolumns, rows=tablerows, row_key="date").classes("w-full").style("white-space: pre-line;")
@ui.page("/profile")
def profile():
    top(islogin=False)
    ui.space()
    username=app.storage.user.get("username", "unknown user")
    userfull:User=User(username)
    userfull.display_profile()
@ui.page("/reports/staff_bookings_and_sales")
def staff_bookings_and_sales():
    top(islogin=False)

    def count_bookings_for_staff_member():

        #retrieves usernames of all stafff who have made a booking
        staffbookings = column_as_list("bookings", "staffuname")

        if len(staffbookings) == 0:
            ui.label("no bookings found").classes("card w-50 whiteglow")

        else:

            shownstaff = []

            for j in range(len(staffbookings)): # go through each booking staff name to count totals per staff member

                if staffbookings[j] == "":
                    continue

                onefound = False


                for k in range(len(shownstaff)): # check if this staff member has already been counted


                    if staffbookings[j] == shownstaff[k]:

                        onefound = True

                        break

                if onefound == False:
                    staffbookingcount = 0

                    for i in range(len(staffbookings)): # count how many bookings belong to this staff member

                        if staffbookings[j] == staffbookings[i]:
                            staffbookingcount += 1

                    shownstaff.append(staffbookings[j])

                    ui.label(f"{staffbookings[j]}: {staffbookingcount} bookings").classes("card w-50 whiteglow")

    def count_sales_for_staff_member():

        #counts sales for staff members by counting how many invoices belong to each staff member
        staffinvoices = column_as_list("invoices", "staffname")

        if len(staffinvoices) == 0:
            ui.label("no invoices found").classes("card w-50 whiteglow")

        else:
            shownstaff = []

            for j in range(len(staffinvoices)): # goes through each employee who's invoice  to count total per staff member

                if staffinvoices[j] == "":
                    continue
                onefound = False

                for k in range(len(shownstaff)): # prevents double count 

                    if staffinvoices[j] == shownstaff[k]:
                        onefound = True
                        break

                if onefound == False:
                    staffinvoicecount = 0

                    for i in range(len(staffinvoices)): # count  invoices belonging to employee

                        if staffinvoices[j] == staffinvoices[i]:
                            staffinvoicecount += 1

                    shownstaff.append(staffinvoices[j])

                    ui.label(f"{staffinvoices[j]}: {staffinvoicecount} invoices").classes("card w-50 whiteglow")

    ui.space()

    with ui.column().classes("w-full items-center justify-center"):

        with ui.card().classes("w-95 items-center justify-center whiteglow"):

            ui.label("staff member bookings and sales").classes("text-3xl")

            ui.separator()

            count_bookings_for_staff_member()

            ui.separator()

            count_sales_for_staff_member()
            
@ui.page("/reports")
def reports():
    top(islogin=False)
    with ui.column().classes("w-full items-center justify-center"):

        ui.space().classes("h-9")

        with ui.card().classes("w-50 items-center justify-center whiteglow"):

            ui.label("reports").classes("text-3xl whiteglow")

            ui.separator()

            ui.space().classes("h-4")

            ui.button("go to calendar", on_click=lambda:moving(page="calendar")).classes("btn w-50 text-white rounded-lg")

            ui.space().classes("h-4")

            ui.button("go to invoices", on_click=lambda:moving(page="invoices")).classes("btn w-50 text-white rounded-lg") 

            ui.space().classes("h-4")

            ui.button("busiest dates", on_click=lambda:moving(page="reports/busiest_dates")).classes("btn w-50 text-white rounded-lg")

            ui.space().classes("h-4")

            ui.button("staff member bookings", on_click=lambda:moving(page="reports/staff_bookings_and_sales")).classes("btn w-50 text-white rounded-lg")
            ui.space().classes("h-4")

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
        
        with ui.card().classes("w-50 whiteglow items-center justify-center"):
        
            results = ui.label()
        
        def handle_change(input1):
        
            # clears previous search results when  new date is selected
            results.set_text("")
            
        
            selecteddate = input1.value
        
           
            # Get all booking data once
            try:
                fnames = column_as_list('bookings', 'fname')
        
                snames = column_as_list('bookings', 'sname')
        
                species_list = column_as_list('bookings', 'species')
        
                staffunames = column_as_list('bookings', 'staffuname')
            
                onefound = False
            except :
                    pass
            for i in range(len(datelist)): # compare a selected date with each booking's date
        
                if selecteddate == datelist[i]:
        
                    results.set_text(f"booking: {fnames[i]} {snames[i]} for a {species_list[i]} booked by staff member {staffunames[i]}")
        
                    onefound = True
        
                elif datelist[i] == "":
        
                    break
            
            if onefound == False:
        
                results.set_text("no bookings for this date")    
        
        
@ui.page("/invoices/create")
def create_invoice():
    top(islogin=False)
    ui.space()
    with ui.column().classes("w-full items-center"):
        
        with ui.card().classes("card width:50% whiteglow"):
            ui.label("customer name")
        
            with ui.row():
        
                custid=ui.input("customer ID(blank=new)", validation=lambda v: "must be 12 numbers long" if v and not (len(v) == 12 and v.isdigit()) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")
                fname=ui.input("forename", validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not range_check(fname.value, 3, 15) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")   
                sname=ui.input("surname",  validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not range_check(sname.value, 3, 15) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")   
                pnum=ui.input("phone number", validation=lambda v: "must be 11 digits long and only contain numbers" if not (len(v) == 11 and v.isdigit()) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")
                email=ui.input("email address", validation=lambda v: "must contain an @ and a . " if not isemail(email.value) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")
        
            with ui.row():
                creditcard=ui.input("credit(or debit) card number", validation=lambda v: "must be 16 digits long and only contain numbers" if not (iscreditcard(v)) else None)
                ui.space().classes("w-9")
                expirydate=ui.input("expiry date", validation=lambda v: "must be in the format mm/yy" if mmyy_format(expirydate.value) == False else None   )
        
            ui.space()
        
            staffname=app.storage.user.get("username", "unknown user")
        # purchase section
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
            #end of purchase section

            def clear_fields():#clears all fields in the invoice form and empties purchase list
        
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
        
            ui.button("Make Invoice", color="black", on_click=lambda:handle_invoice_submit(custid.value, fname.value, sname.value, pnum.value, email.value, creditcard.value, expirydate.value, ", ".join(purchaselist), staffname)).classes("btn w-50 text-white rounded-lg")

        
            ui.button("Clear Fields", color="red", on_click=clear_fields).classes("btn w-50 text-white rounded-lg")

            def handle_invoice_submit(custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist, staffname):
        
                #inserts invoice data(creating a new table if it isn't already present) into db  then clears fields 
                con=sqlite3.connect("gmvets.db")
                custid = custid if custid else f"{random.randint(100000000000, 999999999999)}" # generates random customer id if left blank
                c=con.cursor()
        
                c.execute("CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY AUTOINCREMENT, custid TEXT, fname TEXT, sname TEXT, pnum TEXT, email TEXT, creditcard TEXT, expirydate TEXT, purchaselist TEXT, staffname TEXT)")
        
                c.execute("INSERT INTO invoices (custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist, staffname) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist, staffname))

                con.commit()
                con.close()

                clear_fields()

                ui.notify("Invoice created", color="green")


@ui.page("/invoices/read")  
def readinvoice():      
    top(islogin=False)
    ui.space()

    with ui.column().classes("w-full items-center"):
        ui.label("Read Invoices").classes("text-3xl")
        ui.separator().classes("w-96")
        ui.space().classes("h-4")

        def read_and_display_invoices():
            #retrieves invoice data from the db and creates a card for each invoice to display the data 
            con = sqlite3.connect("gmvets.db")
            c = con.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY AUTOINCREMENT, custid TEXT, fname TEXT, sname TEXT, pnum TEXT, email TEXT, creditcard TEXT, expirydate TEXT, purchaselist TEXT, staffname TEXT)")

            c.execute("SELECT id, custid, fname, sname, pnum, email, creditcard, expirydate, purchaselist, staffname FROM invoices ORDER BY id DESC")
            invoicerows = c.fetchall()
            con.close()

            if len(invoicerows) == 0:
                with ui.card().classes("w-70 whiteglow items-center justify-center"):
                    ui.label("no invoices found")

            else:
                invoiceindex = 0

                while invoiceindex < len(invoicerows):#makes the loop repeat as many times as rows in the table
                    
                    with ui.row().classes("w-full justify-center items-stretch"):

                        cardcount = 0

                        while cardcount < 3 and invoiceindex < len(invoicerows):#makes sure invoices are shown in rows of three cards

                            invoice = invoicerows[invoiceindex]

                            purchases=invoice[8].replace(", ", "\n")

                            with ui.card().classes("card whiteglow text-justify").style("width: 30%; min-width: 300px;padding: 1rem;"):

                                with ui.element("strong"):

                                    ui.label(f"Invoice #{invoice[0]}").classes("text-xl")

                                ui.separator()

                                ui.label(f"Customer ID: {invoice[1]}")

                                ui.label(f"Name: {invoice[2]} {invoice[3]}")

                                ui.label(f"Phone: {invoice[4]}")

                                ui.label(f"Email: {invoice[5]}")

                                ui.label(f"Card Number: {invoice[6]}")

                                ui.label(f"Expiry Date: {invoice[7]}")

                                ui.label(f"Purchases: {purchases}")

                                ui.label(f"Staff Member: {invoice[9]}")

                            invoiceindex += 1

                            cardcount += 1

                    ui.space().classes("h-4")

        read_and_display_invoices()


@ui.page("/invoices")
def invoice():
    top(islogin=False)
    ui.space()
    with ui.column().classes("w-full h-screen items-center justify-center"):

        with ui.card().classes("w-96 rounded-lg whiteglow items-center p-8"):
        

            ui.button("Make An Invoice", color="black", on_click=lambda:moving(page="invoices/create")).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Read Invoices", color="black", on_click=lambda:moving(page="invoices/read")).classes("btn w-50 text-white rounded-lg")

            ui.space()


@ui.page("/booking")
def booking():

    

    top(islogin=False)

    def set_species(e):
        

        species = e.value

        ui.notify("species changed")
    
    
    


    def form_submit(custid, species, fname, sname, pnum, email, petname, petinfo, staffuname, date):

        if custid == "" or custid is None:
            custid = functiontomakecustomerid(custid, fname, sname, petname)
        
        #handles booking submission by inserting data into the db (creating a new table if notalready present) then clearing all fields
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
                custid=ui.input("customer ID(blank=new)", validation=lambda v: "must be 12 numbers long" if v and not (len(v) == 12 and v.isdigit()) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")
                fname=ui.input("forename", validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not range_check(fname.value, 3, 15) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")   
                sname=ui.input("surname",  validation=lambda v: "must be between 3 and 15 letters long if your name is too long use a shortening" if not range_check(sname.value, 3, 15) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")   
                pnum=ui.input("phone number", validation=lambda v: "must be 11 digits long and only contain numbers" if not (len(v) == 11 and v.isdigit()) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")
                email=ui.input("email address", validation=lambda v: "must contain an @ and a . " if not isemail(email.value) else None).classes("w-50 h-15").style("background-color: #a2a2a2; text-color: black;").props("outlined")
                ui.space().classes("w-9")

        ui.space()

        with ui.card().classes("card width:50% whiteglow"):
            ui.label("pet name")

            with ui.row():
                petname=ui.input("name")
                ui.space().classes("w-9")   
                
                species=ui.select(["cat","dog","rabbit","other"], label="species", on_change=set_species).classes("w-50")

            petinfo=ui.textarea("notes include any other relevant information\n here").classes("w-full")

        with ui.card().classes("card width:50% whiteglow"):
            ui.label ("booking info")

            with ui.column():
                date=ui.date(value=f"{currentdate}").classes("w-50").props("outlined")

        def functiontomakecustomerid(custid,fname, sname, petname):

            #generates a random 12 digit customer id if the user leaves the customer id field blank, this is to allow new customers to be added without needing to generate an id for them manually
            if custid == "" or custid is None:
                custid = f"{random.randint(100000000000, 999999999999)}"
            return custid

        name=app.storage.user.get("username", "unknown user")
        
            
        def clear_booking_fields():


            custid.set_value("")

            species.set_value("")

            fname.set_value("")

            sname.set_value("")

            pnum.set_value("")

            email.set_value("")

            petname.set_value("")

            petinfo.set_value("")
            
        with ui.card().classes("card width:50%").classes("whiteglow"):
            ui.button("submit",color="black",on_click=lambda: form_submit(custid.value,species.value,fname.value,sname.value,pnum.value,email.value,petname.value,petinfo.value,name,date.value)).classes("btn").props("rounded")
            ui.button("clear",color="red",on_click=clear_booking_fields).classes("btn")

        
            


@ui.page("/main_menu")
def main():
    
    top(islogin=False)   
    
    with ui.column().classes("w-full h-screen items-center justify-center"):

        with ui.card().classes("w-96 whiteglow rounded-lg items-center p-8") :
        
            ui.button("Make A Booking", color="black", on_click=lambda:moving(page="booking")).classes("btn w-50  text-white rounded-lg")
        
            ui.space()
        
            ui.button("Invoices", color="black", on_click=lambda:moving(page="invoices")).classes("btn w-50  text-white rounded-lg")
        
            ui.space()
        
            ui.button("Calendar", color="black",on_click=lambda:moving(page="calendar")).classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("Reports", color="black", on_click=lambda:moving(page="reports")).classes("btn w-50 text-white rounded-lg")
            
            ui.space()

            ui.button("Settings", color="black", on_click=lambda:moving(page="settings")).classes("btn w-50 text-white rounded-lg")

            ui.space()

            ui.button("User info", color="black", on_click=lambda:moving(page="profile")).classes("btn w-50 text-white rounded-lg")
#this is the main login
@ui.page("/")
def login():
    
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
        

        # simple validation
        if username.value is None or username.value == "":
            ui.notify('Please enter username', color='red')
            return

        if password.value is None or password.value == "":
            ui.notify('Please enter password', color='red')
            return

        if len(username.value) < 5:
            ui.notify('username must be at least 5 characters long', color='red')
            return

        if " " in username.value:
            ui.notify('username must not contain spaces', color='red')
            return

        if len(password.value) < 8:
            ui.notify('password must be at least 8 characters long', color='red')
            return

        #retrieves saved usernames and compares them to inputted username and password
        passwords=column_as_list("users","password")
        users=column_as_list("users","username")
        usernamefound = 0
        passwordfound = 0

        for i in range(len(users)): # check entered login details against each saved user

            if username.value == users[i]:
                usernamefound = True

                if verify_password(password.value, passwords[i]):
                    passwordfound = True
                break

        if usernamefound == False:
            ui.notify('Username not found', color='red')
            clear_fields()

        elif passwordfound == False:
            ui.notify('Incorrect password', color='red')
            clear_fields()

        else:
            moving(page="main_menu")
            app.storage.user['username'] = username.value
            
            
                

         
        
        clear_fields()
        
        
    
    
    
    top(islogin=True)
    
    with ui.column().classes("w-full h-screen items-center justify-center"):
        
        with ui.card().classes("w-96 whiteglow shadow-xl items-center p-8"):
        
            ui.label("login").classes("text-2xl mb-4")
        
            username = ui.input("username", validation=lambda v: "must be at least 5 characters long and contain no spaces" if not (len(v) >= 5 and " " not in v) else None).classes("w-full")
        
            ui.separator().classes("w-full border-gray-400 my-4")
        
            password = ui.input("password", password=True, validation=lambda v: "must be at least 8 characters long" if not (len(v) >= 8) else None).classes("w-full")
        
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

@ui.page("/settings")
def settings():
    top(islogin=False)
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
ui.run(title="greenmount vets", storage_secret="mysecretkey")

