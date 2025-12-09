from nicegui import ui



#functions
@ui.page('/main_menu')
def main_menu():
    

#header
    @ui.page('/')
    def page():
        def func(username, password):
            ui.navigate.to("/main_menu")
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
        card{
        font-family: "DM Sans", sans-serif;
        }
        ''', shared=True)
        ui.add_css('''
        .glow-on-hover {
        width: 220px;
        height: 50px;
        border: none;
        outline: none;
        color: #fff;
        background: #111;
        cursor: pointer;
        position: relative;
        z-index: 0;
        border-radius: 10px;
    }

    .glow-on-hover:before {
        content: '';
        background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
        position: absolute;
        top: -2px;
        left:-2px;
        background-size: 400%;
        z-index: -1;
        filter: blur(5px);
        width: calc(100% + 4px);
        height: calc(100% + 4px);
        animation: glowing 20s linear infinite;
        opacity: 0;
        transition: opacity .3s ease-in-out;
        border-radius: 10px;
    }

    .glow-on-hover:active {
        color: #000
    }

    .glow-on-hover:active:after {
        background: transparent;
    }

    .glow-on-hover:hover:before {
        opacity: 1;
    }

    .glow-on-hover:after {
        z-index: -1;
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        background: #111;
        left: 0;
        top: 0;
        border-radius: 10px;
    }

    @keyframes glowing {
        0% { background-position: 0 0; }
        50% { background-position: 400% 0; }
        100% { background-position: 0 0; }
    }
        ''')
        with ui.card().classes('card flex w-full items-center '):
        
            ui.label('login to Greenmount Vet').classes('inline-block text-black text-4xl font-normal')

    #this is the main login, currently does't do anything but print the username and password to the console

        with ui.column().classes('w-full h-screen items-center justify-center'):
            with ui.card().classes('w-96 shadow-xl bg-gray-100 items-center p-8'):
                ui.label('login').classes('text-2xl mb-4')

                username = ui.input('username').classes('w-full')

                ui.separator().classes('w-full border-gray-400 my-4')

                password = ui.input('password', password=True).classes('w-full')

                ui.space().classes('h-8')
                
                ui.button("submit", on_click=lambda: func(username.value,password.value)).classes("align-items:center btn, glow-on-hover")
                
ui.run()
