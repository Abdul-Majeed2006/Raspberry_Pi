# ==========================================================
# MASTERY PROJECT 7: THE SOUND-LINKED COLOR PICKER
# Goal: Use Knob 1 for Red, Knob 2 for Blue, and link 
# the Green LED's brightness to the Buzzer's Pitch.
# ==========================================================

from machine import Pin, PWM, ADC
import time

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

knob_1 = ADC(Pin(26))
knob_2 = ADC(Pin(27))

buzzer = PWM(Pin(9))

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
# 2. THE MULTI-VARIABLE MIXER
# ----------------------------------------------------------
print("SYSTEM: Sound-Linked Color Picker Active.")
print("Knob 1: Red | Knob 2: Blue | Sound Pitch -> Green")

try:
    while True:
        # STEP A: Read the Knobs
        k1_raw = knob_1.read_u16()
        k2_raw = knob_2.read_u16()
        
        # STEP B: Normalize Red and Blue to 0-100%
        red_p  = (k1_raw / 65535) * 100
        blue_p = (k2_raw / 65535) * 100
        
        # STEP C: Set the Buzzer Pitch based on Knob 1 + 2 combined
        # (Combining them makes for more complex soundscapes!)
        pitch = 500 + ((k1_raw + k2_raw) / 131070) * 3000
        buzzer.freq(int(pitch))
        buzzer.duty_u16(5000) # Soft volume
        
        # STEP D: Link Green intensity to the Pitch
        # The higher the pitch, the brighter the green!
        green_p = ((pitch - 500) / 3000) * 100
        
        # STEP E: Final Output
        set_rgb_gamma(red_p, green_p, blue_p)
        
        # Print the "Mix Recipe"
        print(f"MIX: R:{int(red_p)}% G:{int(green_p)}% B:{int(blue_p)}% | Pitch: {int(pitch)}Hz")
        
        time.sleep(0.1)

except KeyboardInterrupt:
    set_rgb_gamma(0, 0, 0)
    buzzer.duty_u16(0)
    print("\nPicking session complete.")
