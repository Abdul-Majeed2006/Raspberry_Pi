# ==========================================================
# PHASE 08: NETWORKING (LESSON 1)
# Title: The Wi-Fi Handshake
# Goal: Connect your Pico W to the Internet.
# ==========================================================

import network
import time

# --- CONFIGURATION ---
SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_PASSWORD"

def connect_wifi():
    # 1. Create a WLAN "Station" object (like a client)
    wlan = network.WLAN(network.STA_IF)
    
    # 2. Activate the Wi-Fi chip
    wlan.active(True)
    
    # 3. Connect
    print(f"Connecting to {SSID}...")
    wlan.connect(SSID, PASSWORD)
    
    # 4. Wait for it to finish
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    # 5. Check result
    if wlan.isconnected():
        print("Successfully Connected!")
        print("IP Address:", wlan.ifconfig()[0])
    else:
        print("Connection Failed. Check your SSID and Password.")

if __name__ == "__main__":
    connect_wifi()
