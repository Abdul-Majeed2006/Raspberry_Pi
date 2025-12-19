# ==========================================================
# MASTERY PROJECT 1: THE RAINBOW HUE WHEEL
# Goal: Use Knob 1 to slide through the entire color spectrum 
# and Knob 2 to control the overall brightness.
# ==========================================================

from machine import Pin, PWM, ADC
from time import sleep

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

knob_hue        = ADC(Pin(26)) # Controls the Color
knob_brightness = ADC(Pin(27)) # Controls the Intensity

gamma = 2.8

# ----------------------------------------------------------
# 2. COLOR TRANSFORM LOGIC
# ----------------------------------------------------------

def get_hue_color(hue_percent):
    """
    Translates a 0-100 percentage into a specific RGB mix.
    This mimics a 'Color Wheel' rotation.
    """
    if hue_percent < 33: # Red to Green phase
        r = 100 - (hue_percent * 3)
        g = hue_percent * 3
        b = 0
    elif hue_percent < 66: # Green to Blue phase
        r = 0
        g = 100 - ((hue_percent - 33) * 3)
        b = (hue_percent - 33) * 3
    else: # Blue back to Red phase
        r = (hue_percent - 66) * 3
        g = 0
        b = 100 - ((hue_percent - 66) * 3)
    
    return r, g, b

def set_master_color(r_p, g_p, b_p, brightness_p):
    """Applies gamma correction and brightness scaling to the LEDs."""
    master_scale = (brightness_p / 100)
    
    # We use max(0, ...) to prevent tiny floating-point errors (like -0.0000001)
    # from turning into complex numbers during the power calculation.
    r_duty = int((max(0, (r_p * master_scale) / 100) ** gamma) * 65535)
    g_duty = int((max(0, (g_p * master_scale) / 100) ** gamma) * 65535)
    b_duty = int((max(0, (b_p * master_scale) / 100) ** gamma) * 65535)
    
    red_led.duty_u16(r_duty)
    green_led.duty_u16(g_duty)
    blue_led.duty_u16(b_duty)

# ----------------------------------------------------------
# 3. THE RAINBOW LOOP
# ----------------------------------------------------------
print("SYSTEM: Rainbow Hue Wheel Active.")

try:
    while True:
        # STEP A: Read Inputs
        hue_raw = knob_hue.read_u16()
        br_raw  = knob_brightness.read_u16()
        
        # STEP B: Normalize to 0-100% for easier logic
        hue_p = (hue_raw / 65535) * 100
        br_p  = (br_raw / 65535) * 100
        
        # STEP C: Calculate the Color Mix
        r, g, b = get_hue_color(hue_p)
        
        # STEP D: Apply the result
        set_master_color(r, g, b, br_p)
        
        sleep(0.02) # Fast update for smooth "liquify" effect

except KeyboardInterrupt:
    set_master_color(0, 0, 0, 0)
    print("\nRainbow System Disengaged.")
