# ==========================================================
# MASTERY PROJECT 3: THE DIGITAL METRONOME
# Goal: Turn the Pico into a professional music tool.
# Use the Knob to set BPM (Beats Per Minute) from 40 to 200.
# ==========================================================

from machine import Pin, PWM, ADC
import time

# ----------------------------------------------------------
# 1. HARDWARE SETUP
# ----------------------------------------------------------
red_led   = PWM(Pin(21), freq=1000)
green_led = PWM(Pin(22), freq=1000)
blue_led  = PWM(Pin(20), freq=1000)

knob = ADC(Pin(26))
buzzer = PWM(Pin(9))

# ----------------------------------------------------------
# 2. LOGIC FUNCTIONS
# ----------------------------------------------------------

def trigger_beat(is_first_beat):
    """
    Fires a sound and a light flash. 
    The 'first' beat of every bar is higher pitched and Red.
    """
    if is_first_beat:
        # Downbeat (Red)
        red_led.duty_u16(65535)
        green_led.duty_u16(0)
        buzzer.freq(1500)
    else:
        # Sub-beats (Green)
        red_led.duty_u16(0)
        green_led.duty_u16(65535)
        buzzer.freq(800)
    
    buzzer.duty_u16(10000)
    time.sleep(0.05) # Very short flash/beep
    
    # Reset for the rest of the beat
    buzzer.duty_u16(0)
    red_led.duty_u16(0)
    green_led.duty_u16(0)

# ----------------------------------------------------------
# 3. THE ANALOG RHYTHM LOOP
# ----------------------------------------------------------
print("SYSTEM: Metronome Mode Active.")

beat_count = 0

try:
    while True:
        # STEP A: Calculate BPM from Knob
        # --------------------------------------------------
        # Scaling 0-65535 to 40-200 BPM
        knob_val = knob.read_u16()
        bpm = 40 + (knob_val / 65535) * 160
        
        # MATH: Convert BPM to "Seconds per Beat"
        # Since 60 seconds / BPM = delay
        # e.g. 60 BPM = 1 second delay
        delay = 60 / bpm
        
        # STEP B: Trigger the flash
        # --------------------------------------------------
        is_downbeat = (beat_count % 4 == 0) # Every 4th beat
        trigger_beat(is_downbeat)
        
        print(f"BPM: {int(bpm)} | Delay: {delay:.2f}s")
        
        # STEP C: Wait for the next beat
        # We subtract the 0.05s used in trigger_beat to stay accurate.
        time.sleep(delay - 0.05)
        
        beat_count += 1

except KeyboardInterrupt:
    red_led.duty_u16(0)
    green_led.duty_u16(0)
    buzzer.duty_u16(0)
    print("\nMetronome Disengaged.")
