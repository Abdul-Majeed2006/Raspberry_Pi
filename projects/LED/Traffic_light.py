# ==========================================================
# FINAL PROJECT: THE INTELLIGENT TRAFFIC LIGHT (PRO MODE)
# Goal: Build a professional 4-phase intersection with 
# distinct audio cues and dynamic timing.
# ==========================================================

from machine import Pin, PWM, ADC
from time import sleep

# ----------------------------------------------------------
# 1. HARDWARE INITIALIZATION
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)
knob = ADC(Pin(26))
buzzer = PWM(Pin(9))

gamma = 2.8

# ----------------------------------------------------------
# 2. CORE LOGIC FUNCTIONS
# ----------------------------------------------------------

def set_rgb_gamma(r_percent, g_percent, b_percent):
    """Sets the RGB color using 0-100 scale with Gamma Correction."""
    r_duty = int(((r_percent / 100) ** gamma) * 65535)
    g_duty = int(((g_percent / 100) ** gamma) * 65535)
    b_duty = int(((b_percent / 100) ** gamma) * 65535)
    
    red_led.duty_u16(r_duty)
    green_led.duty_u16(g_duty)
    blue_led.duty_u16(b_duty)

# ----------------------------------------------------------
# 3. THE MAIN CONTROLLER
# ----------------------------------------------------------
print("SYSTEM BOOT: 4-Phase Smart Intersection active.")

try:
    while True:
        # PHASE 1: RED (STOP) - 5 Seconds
        # --------------------------------------------------
        print("STATUS: Red Light (STOP)")
        set_rgb_gamma(100, 0, 0)
        for _ in range(5):
            buzzer.freq(400)    # Low freq "Safe" tone
            buzzer.duty_u16(8000)
            sleep(0.1)
            buzzer.duty_u16(0)
            sleep(0.9)

        # PHASE 2: YELLOW (READY TO START) - 1.5 Seconds
        # --------------------------------------------------
        # Red and Green together make Yellow.
        print("STATUS: Yellow Light (READY TO START)")
        set_rgb_gamma(100, 100, 0)
        for _ in range(3):
            buzzer.freq(1500)   # Quick pulse to catch attention
            buzzer.duty_u16(12000)
            sleep(0.1)
            buzzer.duty_u16(0)
            sleep(0.4)

        # PHASE 3: GREEN (GO) - Dynamic Time
        # --------------------------------------------------
        knob_val = knob.read_u16() 
        green_timer = 1.0 + (knob_val / 65535) * 9.0
        print(f"STATUS: Green Light (GO) for {green_timer:.1f}s")
        set_rgb_gamma(0, 100, 0)
        
        # Audio removed as requested - silent travel phase.
        buzzer.duty_u16(0)
        sleep(green_timer)

        # PHASE 4: YELLOW (WARNING TO STOP) - 2 Seconds
        # --------------------------------------------------
        print("STATUS: Yellow Light (WARNING TO STOP)")
        set_rgb_gamma(100, 100, 0)
        for _ in range(4):
            buzzer.freq(3000)   # High freq "Urgent" pulses
            buzzer.duty_u16(15000)
            sleep(0.1)
            buzzer.duty_u16(0)
            sleep(0.4)

except KeyboardInterrupt:
    set_rgb_gamma(0, 0, 0)
    buzzer.duty_u16(0)
    print("\nSYSTEM SHUTDOWN: Intersection disengaged.")
