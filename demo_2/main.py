from dearpygui.core import *
from dearpygui.simple import *

# Main menu bar
with window("Main"):
    add_text('Application 2')
    print('Application 2 running...')

start_dearpygui(primary_window="Main")