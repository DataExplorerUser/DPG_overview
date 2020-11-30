from dearpygui.core import *
from dearpygui.simple import *

# Main menu bar
with window("Main"):
    add_text('Application 1')
    add_text('Close app to continue')
    print('Application 1 running...')

start_dearpygui(primary_window="Main")