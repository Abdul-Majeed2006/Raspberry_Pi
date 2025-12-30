from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# --- Lesson 02: Geometric Shapes ---
# This script demonstrates how to build a basic User Interface (UI)
# using lines and rectangles.

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

# Clear screen
oled.fill(0)

# 1. THE HEADER BAR
# Parameters: (x, y, width, height, color)
oled.fill_rect(0, 0, 128, 12, 1)      # Draw a solid white bar
oled.text("TRUCK STATUS", 15, 2, 0)   # Draw black text on top (color=0)

# 2. THE STATUS BOX
# Parameters: (x, y, width, height, color)
oled.rect(10, 20, 108, 30, 1)         # Draw an empty outline
oled.text("STOPPED", 35, 30, 1)       # White text inside

# 3. DECORATIVE LINE
# Parameters: (x1, y1, x2, y2, color)
oled.line(0, 60, 127, 60, 1)          # Bottom underline

oled.show()
