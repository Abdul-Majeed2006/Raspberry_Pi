from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.pixel(0, 0, 1)      # Top Left
oled.pixel(127, 0, 1)    # Top Right
oled.pixel(0, 63, 1)     # Bottom Left
oled.pixel(127, 63, 1)   # Bottom Right
oled.show()