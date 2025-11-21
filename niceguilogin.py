from nicegui import ui
ui.add_head_html('''
<link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">
''', shared=True)
ui.add_head_html('''
<link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.10/dist/full.min.css" rel="stylesheet" />
''', shared=True)
#                            css
# i have put each item in an individual  ui.add css so it is easier to see
ui.add_css('''body{}''')

with ui.element("div").classes("w3-container w3-red  "):
    ui.label("login").classes("text-center h-20 w-40")
    ui.input("username")
    ui.input("password", password=True)
    ui.button("submit").classes("btn-secondary w-40")
ui.run()
