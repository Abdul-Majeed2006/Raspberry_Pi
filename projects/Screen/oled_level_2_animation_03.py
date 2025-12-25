from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# --- Lesson 03: The Animation Loop ---
# This script uses math and a 'While' loop to create a bouncing box.
# Goal: Learn the Clear-Update-Draw-Show cycle.

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

# Position variables
x = 0
y = 0 

# Speed/Direction variables (Independent brains)
velocity_x = 1
velocity_y = 2

# The infinite Game Loop
while True:
    try:
        # 1. CLEAR the old drawing
        oled.fill(0)
        
        # 2. UPDATE positions
        x += velocity_x
        y += velocity_y
        
        # 3. COLLISION DETECTION (Bouncing off walls)
        # Horizontal Walls
        if x > 118 or x < 0:
            velocity_x *= -1   # Flip direction
            
        # Vertical Walls
        if y > 54 or y < 0:
            velocity_y *= -1   # Flip direction
            
        # 4. DRAW the new frame
        # Draw a 10x10 square at the new (x, y)
        oled.fill_rect(x, y, 10, 10, 1)
        
        # 5. SHOW the frame on the glass
        oled.show()
        
        # 6. WAIT (Timing control)
        time.sleep(0.005) 
        
    except KeyboardInterrupt:
        # Safety: Clear screen and stop if user presses CTRL+C
        oled.fill(0)
        oled.show()
        break
