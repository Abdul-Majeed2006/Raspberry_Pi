# ==========================================================
# PHASE 06: HUMAN INTERFACE (LESSON 2)
# Title: Debouncing & Toggles
# Goal: Make a switch act like a clean "Toggle" (Click ON, Click OFF).
# ==========================================================

from machine import Pin
import time

# --- PINS ---
key = Pin(20, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)

# --- STATE VARIABLES ---
led_is_on = False       # Is the light currently on?
last_key_state = 0      # Was the key pressed last time we checked?

print("Toggle System Ready. Press Key to Swap.")

while True:
    # 1. Read Current State
    current_key_state = key.value()
    
    # 2. DETECT "RISING EDGE" (The exact moment it gets pressed)
    # We only care if it wasn't pressed before (0), but is pressed now (1).
    if current_key_state == 1 and last_key_state == 0:
        print("Rising Edge Detected! Toggling...")
        
        # Swap the LED state
        led_is_on = not led_is_on 
        led.value(led_is_on)
        
        # DEBOUNCE WAIT (The Magic Limit)
        # Mechanical switches "bounce" (click-click-click) purely from physics.
        # We wait 0.2 seconds so we ignore those fake bounces.
        time.sleep(0.2)
        
    # 3. Save state for next loop
    last_key_state = current_key_state
