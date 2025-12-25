# ==========================================================
# PHASE 06: HUMAN INTERFACE (LESSON 3)
# Title: The Eye Controller
# Goal: Use 2 Keys to look Left and Right!
# ==========================================================

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# --- PINS ---
# Keys (Using GP20 and GP21)
KEY_LEFT = Pin(20, Pin.IN, Pin.PULL_DOWN)
KEY_RIGHT = Pin(21, Pin.IN, Pin.PULL_DOWN)

# Screen
i2c = I2C(0, sda=Pin(16), scl=Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

# --- EYE STATE ---
pupil_x = 64  # Center
pupil_y = 32
eye_speed = 4

def draw_eye(x, y):
    oled.fill(0)
    # Socket
    oled.ellipse(64, 32, 35, 22, 1)
    # Pupil
    oled.ellipse(x, y, 12, 12, 1, True)
    oled.show()

print("Eye Controller Ready. Left/Right to Look.")

while True:
    # 1. Read Inputs
    move_left = KEY_LEFT.value()
    move_right = KEY_RIGHT.value()
    
    # 2. Update Logic
    if move_left == 1:
        pupil_x -= eye_speed
        # Limit (Don't fall out of eye)
        if pupil_x < 40: pupil_x = 40
            
    if move_right == 1:
        pupil_x += eye_speed
        # Limit
        if pupil_x > 88: pupil_x = 88
        
    # 3. Draw
    draw_eye(int(pupil_x), int(pupil_y))
    
    # Fast update for smooth movement
    # (No debounce needed because we WANT continuous movement while holding)
    time.sleep(0.01)
