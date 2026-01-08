
from nicegui import ui 

import sqlite3

import time
#functions



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
        with ui.card().classes(" card  w-full items-center justify-center ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            
            ui.label(' Greenmount Vet').classes('text-black text-4xl font-normal')
        with ui.card().classes("ribbon vw-75 items-center justify-center ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):
            ui.label("healing paws, healing hearts")
@ui.page('/reports')
def reports():
    top()
@ui.page('/calendar')
def calendar():
    top()
    
    try:
        c_time=time.localtime()
    except:
        ui.alert("error obtaining the time")
    try:    
        current_date = time.strftime("%Y-%m-%d", c_time)  
    except:
        ui.alert("error obtaining the date ")
    ui.date(value=f"{current_date}", on_change=lambda e: result.set_text(e.value))
    result = ui.label()
@ui.page('/invoices')
def invoice():
    top()
@ui.page('/booking')
def booking():
    top()
    ui.space()
    with ui.column().classes("w-full items-center"):
        with ui.card().classes("card width:50%"):
            ui.label("customer name")
            with ui.row():
                ui.input("forename")
                ui.space().classes("w-9")   
                ui.input("surname") 
        ui.space()
        with ui.card().classes("card width:50%"):
            ui.label("customer name")
            with ui.row():
                ui.input("name")
                ui.space().classes("w-9")   
                ui.input("species") 

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

    ui.add_head_html('''
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;500;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css" rel="stylesheet" />
''', shared=True)

#                                   css
#i have put each item in an individual  ui.add css so it is more readable
    ui.add_css('''
body {
    background: radial-gradient(circle, #0A0654 0%,#0C0765 20%, #001f00 100% );
    font-family: "DM Sans", sans-serif;
}
''', shared=True) 
    
    def moving():
        ui.navigate.to('/main_menu')
    
    def handle_submit():
        usernameval=username.value
    
        passwordval=password.value
        
        ct=sqlite3.connect("username_password.db")
        try:
            cur=ct.cursor()

            cur.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')

            cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (f"{usernameval}", f"{passwordval}"))

            ct.commit

            cur.execute('SELECT * FROM users')

            rows = cur.fetchall()

            for row in rows:

                if rows != ():

                    ui.label(row)

            cur.close()

            ct.close()
        except:    
            moving()
        
        
    
    
    
    top()
    
    with ui.column().classes('w-full h-screen items-center justify-center'):
        
        with ui.card().classes('w-96 shadow-xl bg-gray-100 items-center p-8'):
        
            ui.label('login').classes('text-2xl mb-4')
        
            username = ui.input('username').classes('w-full')
        
            ui.separator().classes('w-full border-gray-400 my-4')
        
            password = ui.input('password', password=True).classes('w-full')
        
            ui.space().classes('h-8')

            ui.button("submit", color="black", on_click=handle_submit).classes("btn text-white rounded-lg")

ui.run()