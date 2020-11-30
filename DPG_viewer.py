from dearpygui.core import *
from dearpygui.simple import *
from pathlib import Path
import types

global application_selected

application_selected = ''

def select_app(sender, data):
    global application_selected
    application_selected = sender
    print('Application selected:', application_selected)
    stop_dearpygui()

def demo_menu():

    # Create the demo menu
    add_additional_font("GlacialIndifference-Regular.otf", 50)
    set_main_window_pos(1200,0)
    set_main_window_size(400,300)

    with window('Demo menu'):
        add_button('Application 1', callback=select_app)
        add_button('Application 2', callback=select_app)
        add_button('Stop demo', callback=select_app)

    # run dearpygui for the demo menu and stop dearpygui once the user has selected an app
    start_dearpygui(primary_window='Demo menu')

def start_program(file_path): # start one of the demo programs
    p = Path(file_path)
    ns = types.ModuleType(p.name)
    exec(compile(p.read_text(encoding='utf-8'), str(p), 'exec'), ns.__dict__)

demo_menu()
print('Is DPG running:', is_dearpygui_running())
print('Starting new app...')
start_program('demo_1/main.py') 
print('New app finished...')
