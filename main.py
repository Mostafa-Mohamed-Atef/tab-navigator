import evdev
from evdev import *
import pyautogui as pp

device = InputDevice('/dev/input/event5')

SWIPE_THRESHOLD = 50
current_position = None
start_position = None

def switch_tabs(direction):
    if direction == 'left':
        pp.hotkey('alt','shift','tab')
    elif direction == 'right':
        pp.hotkey('alt','tab')

for event in device.read_loop():
    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if absevent.event.code == ecodes.ABS_X:
            current_position = absevent.event.value
            
            if start_position is None:
                start_position = current_position

            if current_position - start_position > SWIPE_THRESHOLD:
                switch_tabs("right")
                start_position = None
            elif start_position - current_position > SWIPE_THRESHOLD:
                switch_tabs("left")
                start_position = None
        elif absevent.event.code == ecodes.ABS_Y:
            start_position = None