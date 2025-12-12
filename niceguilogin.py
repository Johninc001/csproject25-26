
from nicegui import ui


#functions
@ui.page('/other_page')
def main():
    pass    
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
    background: radial-gradient(circle, skyblue 0%, white 100%);
    font-family: "DM Sans", sans-serif;
}
''', shared=True)
    with ui.header().classes('bg-gradient-to-r from-blue-500 via-blue-300 to-blue-500 shadow-lg h-20 flex items-center justify-center'):
        ui.label('login to Greenmount Vet').classes('text-black text-4xl font-normal')

    with ui.column().classes('w-full h-screen items-center justify-center'):
        with ui.card().classes('w-96 shadow-xl bg-gray-100 items-center p-8'):
            ui.label('login').classes('text-2xl mb-4')
        
            username = ui.input('username').classes('w-full')
        
            ui.separator().classes('w-full border-gray-400 my-4')
        
            password = ui.input('password', password=True).classes('w-full')
        
            ui.space().classes('h-8')
        with ui.link('menu', '/other_page').classes('text-blue-600 underline mb-4'):    
            ui.button('submit', on_click=lambda: print(f'Username: {username.value}, Password: {password.value}')).classes('btn btn-secondary w-40')

ui.run()
