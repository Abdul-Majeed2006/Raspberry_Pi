# ==========================================================
# PROJECT: THE EMERGENCY SIREN (SIGHT & SOUND)
# Goal: Use PWM to synchronize a dual-color light with a two-tone siren.
#
# ENGINEERING INSIGHT:
# This project teaches "Alert Priority." Engineers design sirens 
# to be "Uncomfortable"—the high-pitched beep and rapid color 
# switching are designed to bypass the human brain's filter 
# and demand immediate attention. This is a lesson in 
# User Interface (UI) design for safety.
# ==========================================================

from machine import Pin, PWM, ADC
from time import sleep

# ----------------------------------------------------------
# 1. HARDWARE INITIALIZATION
# ----------------------------------------------------------
# We use PWM (Pulse Width Modulation) for both the LED and Buzzer.
# As explained in the Technical Notes, PWM allows us to control
# the "Intensity" of light and the "Pitch" of sound.

red_led   = PWM(Pin(21)) # Pin 21 is Red on our physical layout
blue_led  = PWM(Pin(20)) # Pin 20 is Blue on our physical layout
green_led = PWM(Pin(22)) # Pin 22 is Green on our physical layout
buzzer = PWM(Pin(9)) # The Buzzer also uses PWM. 

# The frequencies here determine how "smooth" the light appears.
# 1000Hz is fast enough that the human eye cannot see the flickering.
red_led.freq(1000)
blue_led.freq(1000)
green_led.freq(1000)

# Changing 'freq' on a buzzer changes the Musical Note (Frequency).

# ----------------------------------------------------------
# 2. THE MAIN ENGINE (INFINITE LOOP)
# ----------------------------------------------------------
while True:
    try:
        # Phase 1: RED ALERT
        # --------------------------------------------------
        # We set Red to 100% brightness (65535) and Blue to 0%.
        red_led.duty_u16(65535)
        blue_led.duty_u16(0)
        
        # We set the buzzer to a high frequency (800Hz) for a sharp beep.
        # Duty_u16 determines the VOLUME (32768 is roughly 50% volume).
        buzzer.freq(800)
        buzzer.duty_u16(30000) 
        
        print("PHASE: RED ALERT")
        sleep(0.3) # Hold this state for 0.3 seconds
        
        # Phase 2: BLUE ALERT
        # --------------------------------------------------
        # We flip the states: Red turns OFF, Blue turns ON.
        red_led.duty_u16(0)
        blue_led.duty_u16(65535)
        
        # We change the buzzer to a lower frequency (400Hz) for the "Whoop" sound.
        buzzer.freq(100)
        buzzer.duty_u16(30000)
        
        print("PHASE: BLUE ALERT")
        sleep(0.3) # Hold this state for 0.3 seconds
        
    except KeyboardInterrupt:
        # SAFETY: If the student stops the code, turn everything off!
        red_led.duty_u16(0)
        blue_led.duty_u16(0)
        buzzer.duty_u16(0)
        print("\nSiren System Disengaged.")
        break
