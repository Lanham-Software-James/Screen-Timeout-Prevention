from pynput.mouse import Controller
from pynput import keyboard
from time import sleep, localtime, strftime, time
from math import cos, floor, sin, radians

class MouseMovement: 
  # Constructor
  def __init__(self, radius):
    self.run = True
    self.mouse = Controller()
    self.radius = radius

  # Function used to process key releases
  def on_release(self, key):
    if key == keyboard.Key.ctrl_l:
        self.end_clock()
        # Stop control loop
        self.run = False
        
        # Stop listener
        return False
    
  def start_clock(self):
    self.start_time =  time()
    tmp_time = localtime( self.start_time )
    print('Started at {0}\n'.format( strftime( "%I:%M:%S %p", tmp_time )))
    
  def end_clock(self):
    self.end_time =  time()
    tmp_time = localtime( self.end_time )
    self.elapsed_time = self.end_time - self.start_time

    seconds = round( self.elapsed_time )

    
    hours = floor( seconds/3600 )
    minutes = floor( (seconds - hours*3600)/60 )
    seconds = (seconds - (hours*3600 + minutes*60))
    

    print('Ended at {0}'.format( strftime( "%I:%M:%S %p", tmp_time )))
    print('Time away from keyboard {0} hrs {1} mins {2} secs\n'.format( hours, minutes, seconds ))
  
  # Function used to start the mouse movement
  def start(self):
    print("\nAFK mode started. Please press left-control to return to work.")
    self.start_clock()    

    # Listening for key release events
    listener = keyboard.Listener(
      
      on_release=self.on_release)
    listener.start()
    
    # Main control loop
    while self.run:
      for angle_deg in range(0, 360):
        angle_rad = radians(angle_deg)
        self.mouse.position = (
          100 + self.radius * cos(angle_rad),
          100 + self.radius * sin(angle_rad)
        )
        sleep(0.0025)

# Script
mouse_move = MouseMovement(50)
mouse_move.start()