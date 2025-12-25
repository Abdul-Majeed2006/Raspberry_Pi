from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import random

# --- Lesson 04: The Blinking Eye ---
# Goal: Use 'States' (Open/Closed) and Randomness to create an 'Alive' robot face.

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

#positions
x = 64
x_min = 59
x_max = 69

y = 32
y_min = 22
y_max = 42

# Speed/Direction variables (Independent brains)
v_x = 1
v_y = 0  # Changed from 0 so it actually moves up and down!

def draw_eye(is_open):
    # This line is "Yelling" at Python to let us change these variables!
    # Without this, Python treats x and v_x as Read-Only.
    global x, v_x, y, v_y
    
    oled.fill(0)
    
    if is_open:
        # 1. Update Position
        x += v_x
        y += v_y
        
        # 2. Bounce Logic (The Fence)
        if x < x_min or x > x_max:
            v_x = v_x * -1
        if y < y_min or y > y_max:
            v_y = v_y * -1

        # 3. Draw the Pupil at the new (x, y)
        # External Socket
        oled.ellipse(64, 32, 35, 22, 1)
        # Moving Pupil
        oled.ellipse(x, y, 12, 12, 1, True)
    else:
        # Closed Eye State
        oled.hline(30, 32, 68, 1)
        oled.text("Zzz...", 80, 15, 1)
        
    oled.show()

# Main Loop
print("Starting AI Vision...")
while True:
    try:
        # HEARTBEAT LOOP: Run tracking for 100 frames while open
        # This makes the eye look around smoothly before it blinks.
        for i in range(100):
            draw_eye(True)
            time.sleep(0.01) # Very fast heartbeat
            
        # BLINK State (Happens after the for loop finishes)
        draw_eye(False)
        time.sleep(0.12) # Quick shut
        
    except KeyboardInterrupt:
        oled.fill(0)
        oled.show()
        print("AI Vision Terminated.")
        break