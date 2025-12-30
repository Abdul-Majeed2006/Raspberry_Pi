# ==========================================================
# LESSON 01: THE CONNECTOR
# ==========================================================
# Goal: Connect to Wi-Fi securely using 'secrets.py'.
# Features:
# - LED Status: Slow Blink (Connecting), Solid On (Connected).
# - Auto-Retry: Won't crash if the router is unplugged.
# ==========================================================

import network
import time
import secrets # Imports your SSID/PASSWORD
import machine

# --- CONFIGURATION ---
LED_PIN = "LED" # Onboard LED
MAX_RETRIES = 20

def blink_led(led, delay):
    led.toggle()
    time.sleep(delay)

def connect_to_wifi():
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    led.value(0)
    
    wlan = network.WLAN(network.STA_IF) # Station Mode (Client)
    wlan.active(True)
    wlan.config(pm=0xa11140) # Disable Power Saving (Fixes some latency issues)

    # Check if already connected
    if wlan.isconnected():
        print(">>> ALREADY CONNECTED: ", wlan.ifconfig()[0])
        led.value(1)
        return wlan

    print(f"Connecting to SSID: {secrets.SSID}...")
    wlan.connect(secrets.SSID, secrets.PASSWORD)

    # Wait for connection
    retries = 0
    while not wlan.isconnected() and retries < MAX_RETRIES:
        print(".", end="")
        blink_led(led, 0.5) # Fast blink while trying
        retries += 1
    
    print("\n")
    
    # Final Status Check
    if wlan.isconnected():
        print(">>> SUCCESS! CONNECTED.")
        print(">>> IP ADDRESS:", wlan.ifconfig()[0])
        led.value(1) # Solid ON
        return wlan
    else:
        print("!!! FAILURE: Could not connect.")
        print("Check your SSID/PASSWORD in secrets.py")
        led.value(0) # Off
        return None

if __name__ == "__main__":
    wlan = connect_to_wifi()
