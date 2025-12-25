from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# I2C Configuration
# SCL -> GP17 (Pin 22)
# SDA -> GP16 (Pin 21)
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# OLED Configuration
WIDTH = 128
HEIGHT = 64

# Initialize OLED
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Simple Test
def test_display():
    # Clear display
    oled.fill(0)
    
    # Draw text
    oled.text("Hello Pico!", 0, 0)
    oled.text("OLED Working", 0, 16)
    oled.text("128x64 I2C", 0, 32)
    
    # Draw a line
    oled.hline(0, 50, 128, 1)
    
    # Show on screen
    oled.show()
    print("OLED test complete!")

if __name__ == "__main__":
    test_display()
