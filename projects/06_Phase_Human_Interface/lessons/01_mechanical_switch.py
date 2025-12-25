# ==========================================================
# PHASE 06: HUMAN INTERFACE (LESSON 1)
# Title: The Mechanical Switch (Pull-Down Logic)
# Goal: Use a mechanical key to turn on an LED.
# ==========================================================

from machine import Pin
import time

# --- CONFIGURATION ---
# The Mechanical Switch
# We use Pin 20 (You can change this)
KEY_PIN = 20

# The Onboard LED (To test if it works)
LED_PIN = 25 # "LED" for Pico W

# --- SETUP ---
# 1. Setup the LED as an OUTPUT
led = Pin(LED_PIN, Pin.OUT)

# 2. Setup the Key as an INPUT
# Critical: We use Pin.PULL_DOWN
# This tells the Pico: "If nothing is connected, assume the signal is 0 (Low)"
# Without this, the pin would "float" and randomly trigger!
key = Pin(KEY_PIN, Pin.IN, Pin.PULL_DOWN)

print("System Ready. Press the Key!")

# --- MAIN LOOP ---
while True:
    # 1. Read the switch (0 or 1)
    # If using PULL_DOWN:
    #   - Not Pressed = 0 (Connection to Ground inside chip)
    #   - Pressed     = 1 (Connection to 3.3V)
    state = key.value()
    
    if state == 1:
        print("CLICK! (Key Pressed)")
        led.value(1) # Light on
    else:
        led.value(0) # Light off
        
    # Small delay to save power
    time.sleep(0.05)
