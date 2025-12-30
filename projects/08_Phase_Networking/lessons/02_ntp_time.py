# ==========================================================
# LESSON 02: THE TIME KEEPER (NTP)
# ==========================================================
# Goal: Sync the Pico's internal clock with the Internet.
# Why: Onboard clocks drift. NTP (Network Time Protocol) is
#      the gold standard for keeping time.
# ==========================================================

import machine
import time
import ntptime # Built-in MicroPython Library
import network
import secrets

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(secrets.SSID, secrets.PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print("Wi-Fi Connected. IP:", wlan.ifconfig()[0])

def main():
    # 1. We MUST have internet to get time
    connect_wifi()
    
    print("\n--- SYNCING TIME ---")
    print("Old Time:", time.localtime())
    
    # 2. The Magic Line
    # Contacts a server like pool.ntp.org and sets hardware clock
    try:
        ntptime.settime()
        print(">>> SUCCESS: Time Synced with NIST/Google.")
    except Exception as e:
        print("!!! ERROR: Could not sync time.", e)
        
    # 3. Timezone Adjustment (UTC -> Local)
    # MicroPython uses UTC by default.
    # Ex: UTC-5 (EST)
    UTC_OFFSET = -5 * 3600 
    
    print("\n--- CLOCK RUNNING ---")
    while True:
        # Get UTC (synced)
        t = time.time()
        
        # Apply Offset
        local_t = t + UTC_OFFSET
        
        # Format
        # (year, month, day, hour, min, sec, weekday, yearday)
        tm = time.localtime(local_t)
        
        # "YYYY-MM-DD HH:MM:SS"
        time_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
            tm[0], tm[1], tm[2], tm[3], tm[4], tm[5]
        )
        
        print(f"\rLocal Clock: {time_str}", end="")
        time.sleep(1)

if __name__ == "__main__":
    main()
