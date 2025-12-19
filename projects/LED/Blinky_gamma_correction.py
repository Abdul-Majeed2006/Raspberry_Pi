# ==========================================================
# PROJECT: THE BREATHING LED (GAMMA CORRECTION)
# Goal: Use mathematics to match LED brightness to human perception.
# ==========================================================

from machine import Pin, PWM
from time import sleep

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000, duty_u16=0)
blue_led  = PWM(Pin(20), freq=1000, duty_u16=0)

# Gamma Coefficient: 2.8 is the "Magic Number" for human eyes.
# It curves the signal so the fade looks smooth and natural.
gamma = 2.8

# ----------------------------------------------------------
# 2. THE BREATHING ENGINE
# ----------------------------------------------------------
while True:
    try:
        # Phase 1: RED LED - Breathing In and Out
        # --------------------------------------------------
        print("ACTION: Red LED Breathing...")
        
        # Fade UP (0 to 100)
        for i in range(101):
            # The Formula: (Percent ** Gamma) * Max_Value
            corrected_val = int(((i / 100) ** gamma) * 65535)
            red_led.duty_u16(corrected_val)
            sleep(0.01)
            
        # Fade DOWN (100 to 0)
        for i in range(100, -1, -1):
            corrected_val = int(((i / 100) ** gamma) * 65535)
            red_led.duty_u16(corrected_val)
            sleep(0.01)

        # Phase 2: BLUE LED - Breathing In and Out
        # --------------------------------------------------
        print("ACTION: Blue LED Breathing...")
        
        # Fade UP
        for i in range(101):
            corrected_val = int(((i / 100) ** gamma) * 65535)
            blue_led.duty_u16(corrected_val)
            sleep(0.01)
            
        # Fade DOWN
        for i in range(100, -1, -1):
            corrected_val = int(((i / 100) ** gamma) * 65535)
            blue_led.duty_u16(corrected_val)
            sleep(0.01)

    except KeyboardInterrupt:
        # SAFETY: Always turn OFF the lights when stopping!
        red_led.duty_u16(0)
        blue_led.duty_u16(0)
        print("\nBreathing System Disengaged.")
        break