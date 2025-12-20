# ==========================================================
# PROJECT: THE ANALOG DIMMER & SAFETY ALARM
# Goal: Use physical knobs (ADC) to control LED brightness (PWM) 
# and use conditional logic to trigger a buzzer.
# ==========================================================

from machine import Pin, PWM, ADC
from time import sleep

# ----------------------------------------------------------
# 1. HARDWARE INITIALIZATION
# ----------------------------------------------------------
# LEDs use PWM so we can slide their brightness from 0 to 65535.
red_led   = PWM(Pin(21), freq=1000, duty_u16=0)
blue_led  = PWM(Pin(20), freq=1000, duty_u16=0)
green_led = PWM(Pin(22), freq=1000, duty_u16=0)

# Knobs use ADC (Analog-to-Digital Converter).
# They translate a physical position into a number between 0 and 65535.
knob_1 = ADC(Pin(26)) 
knob_2 = ADC(Pin(27)) 

# The buzzer is ready for sound effects if the "Safety Alarm" triggers.
buzzer = PWM(Pin(9)) 

# ----------------------------------------------------------
# 2. THE ANALOG ENGINE
# ----------------------------------------------------------
while True:
    try:
        # STEP A: Read the physical state of the knobs
        # --------------------------------------------------
        val = knob_1.read_u16()   # Get value of Knob 1 (0 to 65535)
        val_2 = knob_2.read_u16() # Get value of Knob 2 (0 to 65535)
        
        # STEP B: Direct Mapping
        # --------------------------------------------------
        # Because both ADC and PWM use the same 0-65535 range,
        # we can pass the knob value directly to the LED brightness.
        red_led.duty_u16(val)
        blue_led.duty_u16(val_2)
        
        # STEP C: Complex Conditional Logic (The Safety Alarm)
        # --------------------------------------------------
        # We only want the buzzer to sound if BOTH knobs are turned 
        # nearly all the way up (above 65,000).
        if val > 65000 and val_2 > 65000:
            buzzer.freq(800)      # Set pitch to 800Hz
            buzzer.duty_u16(30000) # Turn Volume to ~50%
        else:
            # If even one knob is below 65000, keep the buzzer silent.
            buzzer.duty_u16(0)     
            
        # STEP D: Loop Stability
        # --------------------------------------------------
        # We wait a tiny amount of time to prevent the CPU from
        # running at 100% speed, which keeps the system stable.
        sleep(0.1)
        
    except KeyboardInterrupt:
        # SAFETY: Always turn OFF hardware when the program stops!
        red_led.duty_u16(0)
        blue_led.duty_u16(0)
        buzzer.duty_u16(0)
        print("\nAnalog Control System Disengaged.")
        break
