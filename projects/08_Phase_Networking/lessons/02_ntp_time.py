# ==========================================================
# PHASE 07: NETWORKING (LESSON 2)
# Title: NTP Time (The World Clock)
# Goal: Ask the Internet for the current time.
# ==========================================================

import network
import ntptime
import time

# --- PICO W WIFI SETUP ---
SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_PASSWORD"

def sync_time():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    # Wait for connection
    while not wlan.isconnected():
        time.sleep(1)
        
    print("Connected! Fetching network time...")
    
    # ntptime.settime() pings an NTP server and sets the Pico's clock
    try:
        ntptime.settime()
        print("System time synchronized!")
    except:
        print("NTP Error: Could not reach time server.")

def show_time():
    # localtime() returns a tuple: (year, month, day, hour, min, sec, weekday, yearday)
    t = time.localtime()
    print(f"Date: {t[0]}-{t[1]}-{t[2]}")
    print(f"Time (UTC): {t[3]}:{t[4]}:{t[5]}")

if __name__ == "__main__":
    sync_time()
    while True:
        show_time()
        time.sleep(5)
