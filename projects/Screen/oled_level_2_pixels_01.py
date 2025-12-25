from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# --- Lesson 01: The Coordinate System ---
# This script lights up the extreme edges of the screen.
# Goal: Understand that (0,0) is top-left and (127,63) is bottom-right.

# I2C setup for GP16 and GP17
i2c = I2C(0, sda=Pin(16), scl=Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

# Clear the screen (z=0 means light OFF)
oled.fill(0)

# Draw individual pixels (x, y, color)
oled.pixel(0, 0, 1)      # Top Left
oled.pixel(127, 0, 1)    # Top Right
oled.pixel(0, 63, 1)     # Bottom Left
oled.pixel(127, 63, 1)   # Bottom Right
oled.pixel(64, 32, 1)    # Center Mass

# Push the virtual sketchpad to the glass
oled.show()
