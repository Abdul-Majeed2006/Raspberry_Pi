# ==========================================================
# MASTERY PROJECT 2: THE COMBINATION SAFE
# Goal: Find the two secret 'Analog Codes' using the knobs 
# to unlock the safe (Green Light + Victory Chirp).
# ==========================================================

from machine import Pin, PWM, ADC
from time import sleep

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

knob_1 = ADC(Pin(26))
knob_2 = ADC(Pin(27))

buzzer = PWM(Pin(9))

# SECRET CODES (Change these to whatever you want!)
# These are the 0-65535 values the student must find.
CODE_1 = 25000 
CODE_2 = 48000
MARGIN = 2000 # How close they need to be to "count"

# ----------------------------------------------------------
# 2. HELPER FUNCTIONS
# ----------------------------------------------------------

def set_rgb(r, g, b):
    red_led.duty_u16(r)
    green_led.duty_u16(g)
    blue_led.duty_u16(b)

# ----------------------------------------------------------
# 3. GAME LOOP (STATE MACHINE)
# ----------------------------------------------------------
print("SYSTEM: Combination Safe Locked. Find the codes!")
print("PRO-TIP: Turn both knobs to ZERO to re-lock the safe.")

is_locked = True

try:
    while True:
        # A: Read the current dial positions
        dial_1 = knob_1.read_u16()
        dial_2 = knob_2.read_u16()
        
        # B: Check for 'The Reset' (Both knobs at zero to lock)
        if dial_1 < 1000 and dial_2 < 1000:
            if not is_locked:
                print("STATUS: SAFE LOCKED.")
                is_locked = True
                set_rgb(65535, 0, 0) # Back to Red
                sleep(1.0)
        
        # C: Check if dials match the code
        match_1 = abs(dial_1 - CODE_1) < MARGIN
        match_2 = abs(dial_2 - CODE_2) < MARGIN
        
        if is_locked:
            if match_1 and match_2:
                # VICTORY: Unlock the safe!
                print("STATUS: UNLOCKED!")
                is_locked = False
                set_rgb(0, 65535, 0) # Solid Green
                
                # Victory Fanfare
                for freq in [1000, 1500, 2000]:
                    buzzer.freq(freq)
                    buzzer.duty_u16(10000)
                    sleep(0.1)
                buzzer.duty_u16(0)
                
            elif match_1 or match_2:
                # If one dial is close, show Yellow and give a 'click' sound
                set_rgb(30000, 30000, 0)
                
                # Simulated 'Tumbler Click'
                buzzer.freq(400)
                buzzer.duty_u16(5000)
                sleep(0.02)
                buzzer.duty_u16(0)
            else:
                # Standard Locked state - Solid Red
                set_rgb(65535, 0, 0)
                buzzer.duty_u16(0)
        else:
            # If already UNLOCKED, keep it Green
            set_rgb(0, 65535, 0)
            
        sleep(0.05)

except KeyboardInterrupt:
    set_rgb(0, 0, 0)
    buzzer.duty_u16(0)
    print("\nSecurity System Offline.")
