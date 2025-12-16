
from nicegui import ui


#functions
def top(current_page):
        with ui.card().classes(" card w-full items-center justify-center "):
            ui.label(f'{current_page}  Greenmount Vet').classes('text-black text-4xl font-normal')
@ui.page('/main_menu')
def main():
    current_page="main menu of"
    top(current_page)   
#this is the main login, currently does't do anything but print the username and password to the console
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
    background: radial-gradient(circle, skyblue 0%, black 100%);
    font-family: "DM Sans", sans-serif;
}
''', shared=True) 

    def handle_submit():
        ui.navigate.to('/main_menu')
    current_page="login to"
    top(current_page)
    with ui.column().classes('w-full h-screen items-center justify-center'):
        
        with ui.card().classes('w-96 shadow-xl bg-gray-100 items-center p-8'):
            ui.label('login').classes('text-2xl mb-4')
        
            username = ui.input('username').classes('w-full')
        
            ui.separator().classes('w-full border-gray-400 my-4')
        
            password = ui.input('password', password=True).classes('w-full')
        
            ui.space().classes('h-8')

            ui.button('submit', on_click=handle_submit).classes('btn-one w-40')

ui.run()
