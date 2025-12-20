# ==========================================================
# MASTERY PROJECT 6: THE MOOD LANTERN
# Goal: Use Sine Waves to create smooth, organic color
# breathing effects that cycle automatically.
# ==========================================================

from machine import Pin, PWM
import time
import math

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

gamma = 2.8

def set_rgb_gamma(r_p, g_p, b_p):
    """Sets RGB with 0-100% inputs and Gamma Correction."""
    r_duty = int((max(0, r_p / 100) ** gamma) * 65535)
    g_duty = int((max(0, g_p / 100) ** gamma) * 65535)
    b_duty = int((max(0, b_p / 100) ** gamma) * 65535)
    
    red_led.duty_u16(r_duty)
    green_led.duty_u16(g_duty)
    blue_led.duty_u16(b_duty)

# ----------------------------------------------------------
# 2. THE ORGANIC CYCLE
# ----------------------------------------------------------
print("SYSTEM: Mood Lantern Mode Active.")
print("Enjoy the smooth, mathematical glow...")

counter = 0

try:
    while True:
        # THE MATH:
        # math.sin returns a value between -1.0 and 1.0.
        # We add 1.0 to get 0.0 to 2.0.
        # We divide by 2.0 to get 0.0 to 1.0.
        # Finally, multiply by 100 to get a 0-100 percentage.
        
        # We use different 'offsets' (0, 2, 4) so the colors 
        # don't all peak at the same time. This creates shifting hues.
        r = ((math.sin(counter) + 1) / 2) * 100
        g = ((math.sin(counter + 2) + 1) / 2) * 100
        b = ((math.sin(counter + 4) + 1) / 2) * 100
        
        set_rgb_gamma(r, g, b)
        
        # Increment the counter. Higher numbers = faster flashing.
        counter += 0.05
        
        time.sleep(0.05)

except KeyboardInterrupt:
    set_rgb_gamma(0, 0, 0)
    print("\nLantern Extinguished.")
