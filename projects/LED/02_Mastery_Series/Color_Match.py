# ==========================================================
# MASTERY PROJECT 8: THE COLOR MATCH CHALLENGE
# Goal: Find the "Hidden Color" chosen by the Pico.
# Use Knob 1 for Hue and Knob 2 for Brightness.
# The Buzzer will beep faster as you get closer!
#
# ENGINEERING INSIGHT:
# This project introduces "Proximity Feedback Loops." 
# Engineers use these to help humans or machines "home in" 
# on a target. By calculating the "Error" (the distance 
# from the goal) and turning it into sound, we create 
# a real-time guidance system.
# ==========================================================

from machine import Pin, PWM, ADC
import time
import random
import math

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

knob_1 = ADC(Pin(26)) # Hue
knob_2 = ADC(Pin(27)) # Brightness

buzzer = PWM(Pin(9))

gamma = 2.8

def set_rgb_gamma(r_p, g_p, b_p):
    r_duty = int((max(0, r_p / 100) ** gamma) * 65535)
    g_duty = int((max(0, g_p / 100) ** gamma) * 65535)
    b_duty = int((max(0, b_p / 100) ** gamma) * 65535)
    
    red_led.duty_u16(r_duty)
    green_led.duty_u16(g_duty)
    blue_led.duty_u16(b_duty)

def get_hue_color(hue_percent):
    """Translates 0-100% into RGB percentages."""
    angle = (hue_percent / 100) * 6.28  # 0 to 2*PI
    r = (math.sin(angle) + 1) * 50
    g = (math.sin(angle + 2.1) + 1) * 50
    b = (math.sin(angle + 4.2) + 1) * 50
    return r, g, b

# ----------------------------------------------------------
# 2. GAME SETUP
# ----------------------------------------------------------
# Generate a random target Hue and Brightness
target_hue = random.randint(0, 100)
target_bright = random.randint(20, 100)

print(f"SYSTEM: Target Color Generated. Searching...")

last_beep = time.ticks_ms()

try:
    while True:
        # A: Read current Knob inputs
        k1 = (knob_1.read_u16() / 65535) * 100
        k2 = (knob_2.read_u16() / 65535) * 100
        
        # B: Show the user's current color
        r_base, g_base, b_base = get_hue_color(k1)
        scale = k2 / 100
        set_rgb_gamma(r_base * scale, g_base * scale, b_base * scale)
        
        # C: Calculate "The Error" (How far are we from target?)
        hue_err = abs(k1 - target_hue)
        brt_err = abs(k2 - target_bright)
        total_err = (hue_err + brt_err) / 2
        
        # D: VICTORY LOGIC
        if total_err < 3: # If error is less than 3%
            print("MATCH FOUND! Congratulations.")
            # Victory Sound
            for f in range(1000, 3000, 200):
                buzzer.freq(f)
                buzzer.duty_u16(10000)
                time.sleep(0.05)
            buzzer.duty_u16(0)
            break
            
        # E: PROXIMITY AUDIO (Geiger Counter)
        # The closer you are (lower error), the shorter the beep delay.
        beep_delay = 50 + (total_err * 20) # 50ms to 2000ms delay
        
        if time.ticks_diff(time.ticks_ms(), last_beep) > beep_delay:
            # Chirp!
            buzzer.freq(800)
            buzzer.duty_u16(5000)
            time.sleep(0.01)
            buzzer.duty_u16(0)
            last_beep = time.ticks_ms()
            
        time.sleep(0.05)

except KeyboardInterrupt:
    set_rgb_gamma(0, 0, 0)
    buzzer.duty_u16(0)
    print("\nGame Stopped.")
