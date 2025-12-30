# ==========================================================
# PHASE 07: NETWORKING (CAPSTONE)
# Title: OLED World Clock Dashboard
# Goal: Display live internet time on your screen.
# ==========================================================

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import network
import ntptime
import time

# --- CONFIG ---
SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_PASSWORD"
TIMEZONE_OFFSET = -5 # e.g., -5 for EST (adjust to your area)

# --- HARDWARE ---
i2c = I2C(0, sda=Pin(16), scl=Pin(17))
oled = SSD1306_I2C(128, 64, i2c)

def connect_and_sync():
    oled.fill(0)
    oled.text("Connecting...", 0, 0)
    oled.show()
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    while not wlan.isconnected():
        time.sleep(1)
        
    ntptime.settime()
    oled.fill(0)
    oled.text("Synced!", 0, 0)
    oled.show()
    time.sleep(1)

def main():
    connect_and_sync()
    
    while True:
        # Get UTC time
        utc = time.time()
        # Apply offset (seconds)
        local = utc + (TIMEZONE_OFFSET * 3600)
        t = time.localtime(local)
        
        oled.fill(0)
        # Header
        oled.fill_rect(0, 0, 128, 12, 1)
        oled.text("WORLD CLOCK", 25, 2, 0)
        
        # Date
        date_str = f"{t[0]}/{t[1]:02d}/{t[2]:02d}"
        oled.text(date_str, 30, 20, 1)
        
        # Time (BIG)
        time_str = f"{t[3]:02d}:{t[4]:02d}:{t[5]:02d}"
        oled.text(time_str, 30, 40, 1)
        
        oled.show()
        time.sleep(1)

if __name__ == "__main__":
    main()
