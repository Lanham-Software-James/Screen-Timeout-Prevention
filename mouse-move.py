from pynput import keyboard
from pynput.mouse import Controller
import time
import math

RADIUS = 50

mouse = Controller()

while 1:
        for angle_deg in range(0, 360):
                angle_rad = math.radians(angle_deg)
                mouse.position = (
                        100 + RADIUS * math.cos(angle_rad),
                        100 + RADIUS * math.sin(angle_rad)
                )
                time.sleep(0.0025)