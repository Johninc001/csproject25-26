
from nicegui import ui 

import sqlite3

#functions

def top(current_page):
        with ui.card().classes(" card  w-full items-center justify-center ").style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);"):

            ui.label(f'{current_page}  Greenmount Vet').classes('text-black text-4xl font-normal')
@ui.page('/reports')
def reports():
    top(current_page="reports on")

@ui.page('/calendar')
def calendar():
    top(current_page="calendar of")

@ui.page('/invoices')
def invoice():
    current_page="invoices of"
    top(current_page)
@ui.page('/booking')
def booking():
    current_page ="booking form for"
    top(current_page)
@ui.page('/main_menu')
def main():
    current_page="main menu of"
    
    top(current_page)   
    
    with ui.column().classes('w-full h-screen items-center justify-center'):

        with ui.card().classes('w-96 rounded-lg  bg-gray-100 items-center p-8').style("box-shadow: 5px 5px 15px 0px rgba(255,255,240, 0.625);") :
        
            ui.label("menu").classes("underline underline-offset-auto text-2xl text-black")

            ui.button("make a booking", color="black").classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("invoices", color="black").classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("calendar", color="black").classes("btn w-50 text-white rounded-lg")
        
            ui.space()
        
            ui.button("reports", color="black").classes("btn w-50 text-white rounded-lg")
            

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
    background: radial-gradient(circle, #0A0654 0%,#0C0765 20%, #0B3007 100% );
    font-family: "DM Sans", sans-serif;
}
''', shared=True) 
    
    def moving():
        ui.navigate.to('/main_menu')
    
    def handle_submit():
        usernameval=username.value
    
        passwordval=password.value
        
        ct=sqlite3.connect("username_password.db")
    
        cur=ct.cursor()
    
        cur.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
    
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (f"{usernameval}      ", f"{passwordval}"))
    
        ct.commit
    
        cur.execute('SELECT * FROM users')
    
        rows = cur.fetchall()
    
        for row in rows:
    
            if rows != ():
    
                ui.label(row)
    
        cur.close()
    
        ct.close()
    
        moving()
        
        
    
    current_page="login to"
    
    top(current_page)
    
    with ui.column().classes('w-full h-screen items-center justify-center'):
        
        with ui.card().classes('w-96 shadow-xl bg-gray-100 items-center p-8'):
        
            ui.label('login').classes('text-2xl mb-4')
        
            username = ui.input('username').classes('w-full')
        
            ui.separator().classes('w-full border-gray-400 my-4')
        
            password = ui.input('password', password=True).classes('w-full')
        
            ui.space().classes('h-8')

            ui.button("submit", color="black", on_click=handle_submit).classes("btn text-white rounded-lg")

ui.run()