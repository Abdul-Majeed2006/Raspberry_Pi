# ==========================================================
# PROJECT: THE RGB COLOR LAB
# Goal: Master Additive Color Theory using Primary Signals.
# ==========================================================

from machine import Pin, PWM
from time import sleep
from random import randint

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
# We initialize all three components of the RGB LED.
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

# HELPER FUNCTION: This makes mixing colors much easier!
# ----------------------------------------------------------
# NOTE FOR LEARNERS: Why 65535 and not 255?
# Standard RGB in software (like CSS or Photoshop) is 8-bit (0-255).
# The Pico's hardware is much more precise (16-bit). 
# This higher resolution (0 to 65535) Allows for ultra-smooth fades.
# If you want to use a standard 0-255 value, just multiply it by 257!
# Example: set_rgb(255 * 257, 0, 0)
# ----------------------------------------------------------
def set_rgb(r, g, b):
    # Each value should be between 0 (off) and 65535 (full).
    red_led.duty_u16(r)
    green_led.duty_u16(g)
    blue_led.duty_u16(b)

# ----------------------------------------------------------
# 2. THE COLOR EXPERIMENT
# ----------------------------------------------------------
try:
    # MISSION 1: Secondary Colors (The Recipes)
    # ------------------------------------------------------
    print("ACTION: Starting Color Recipes...")
    
    print("Recipe: Yellow (Red + Green)")
    set_rgb(65535, 65535, 0)
    sleep(1.5)
    
    print("Recipe: Magenta (Red + Blue)")
    set_rgb(65535, 0, 65535)
    sleep(1.5)
    
    print("Recipe: Cyan (Green + Blue)")
    set_rgb(0, 65535, 65535)
    sleep(1.5)
    
    print("Recipe: White (All together)")
    set_rgb(65535, 65535, 65535)
    sleep(1.5)

    # MISSION 2: Random Mixing (The Party Mode)
    # ------------------------------------------------------
    print("\nACTION: Entering Random Mixing Mode...")
    while True:
        # 'randint' picks a random number in our PWM range.
        r = randint(0, 65535)
        g = randint(0, 65535)
        b = randint(0, 65535)
        
        set_rgb(r, g, b)
        sleep(0.5)

except KeyboardInterrupt:
    # SAFETY: Always turn everything OFF when we stop the code.
    set_rgb(0, 0, 0)
    print("\nColor Lab Disengaged.")
