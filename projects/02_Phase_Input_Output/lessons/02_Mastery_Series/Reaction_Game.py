# ==========================================================
# MASTERY PROJECT 5: THE REACTION GAME
# Goal: Test your reflexes! Wait for the Green light and 
# turn Knob 1 as fast as you can.
#
# ENGINEERING INSIGHT:
# This project explores "Precision Latency Timing." 
# In high-speed systems (like airbags or fighter jets), 
# milliseconds matter. By using `ticks_ms()` and "Delta 
# Detection" (detecting a change in value), engineers 
# can measure human performance with extreme accuracy.
# ==========================================================

from machine import Pin, PWM, ADC
import time
import random

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

knob = ADC(Pin(26))
buzzer = PWM(Pin(9))

def set_rgb(r, g, b):
    red_led.duty_u16(r)
    green_led.duty_u16(g)
    blue_led.duty_u16(b)

# ----------------------------------------------------------
# 2. GAME LOGIC
# ----------------------------------------------------------
print("SYSTEM: Reaction Game Ready.")
print("INSTRUCTIONS: Wait for GREEN, then turn Knob 1 to the MAXIMUM!")

try:
    while True:
        # A: Prep Phase
        set_rgb(65535, 0, 0) # Red means "Wait..."
        buzzer.duty_u16(0)
        
        # Ensure the knob is at zero before starting
        while knob.read_u16() > 5000:
            print("WAIT: Please turn Knob 1 all the way to the LEFT to start.")
            time.sleep(1)
            
        # Wait a random time between 2 and 5 seconds
        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)
        
        # B: GO Phase!
        set_rgb(0, 65535, 0) # Green means "GO!"
        buzzer.freq(1000)
        buzzer.duty_u16(10000)
        
        start_time = time.ticks_ms() # Capture start time in milliseconds
        
        # DELTA DETECTION: Capture the starting position of the knob
        start_knob_val = knob.read_u16()
        current_knob_val = start_knob_val
        
        # Wait for the user to move the knob by at least 10,000 units
        while abs(current_knob_val - start_knob_val) < 10000:
            current_knob_val = knob.read_u16()
        
        end_time = time.ticks_ms() # Capture end time
        
        # C: Result Phase
        reaction_time = time.ticks_diff(end_time, start_time)
        
        buzzer.duty_u16(0)
        set_rgb(0, 0, 65535) # Blue while showing score
        
        print("-" * 30)
        print(f"REACTION TIME: {reaction_time} ms")
        
        if reaction_time < 200:
            print("RANK: CYBORG 🤖 (God-like speed!)")
        elif reaction_time < 400:
            print("RANK: NINJA 🥷")
        else:
            print("RANK: SLOTH 🦥 (Keep practicing!)")
        print("-" * 30)
        
        time.sleep(3) # Pause before next round

except KeyboardInterrupt:
    set_rgb(0, 0, 0)
    buzzer.duty_u16(0)
    print("\nGame Over.")
