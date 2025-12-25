# ==========================================================
# MASTERY PROJECT 9: THE F1 ENGINE SIMULATOR
# Goal: Build a high-performance racing engine.
# Knob 1 = Accelerator (RPM: 1,000 to 18,000)
# Listen to the "Engine" and watch the "Shift Lights"!
#
# ENGINEERING INSIGHT:
# This project is a "Safety Telemetry Simulation." Engineers use 
# visual and audio cues to communicate complex data (RPM) to a 
# human operator instantly. The multi-stage shift lights teach 
# how to design "Predictive Warning Systems"—alerting the user 
# *before* an emergency (the rev limiter) happens.
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
# 2. RACING LOOP
# ----------------------------------------------------------
print("SYSTEM: F1 Engine Control Unit (ECU) Online.")
print("INSTRUCTION: Floor it to test the Shift Lights!")

try:
    while True:
        # STEP A: Read "Throttle" from Knob
        # Map 0-65535 to 1,000-18,000 RPM
        raw_val = knob.read_u16()
        rpm = 1000 + (raw_val / 65535) * 17000
        
        # Determine "Stress Level" (0.0 to 1.0)
        stress = (rpm - 1000) / 17000
        
        # STEP B: Engine Sound (Frequency modulation)
        # Higher RPM = Higher Pitch
        engine_pitch = 100 + (stress * 1200)
        buzzer.freq(int(engine_pitch))
        buzzer.duty_u16(5000) # Soft engine thrum
        
        # STEP C: Shift Light Logic
        if stress < 0.6:
            # Low RPM: Solid Green
            set_rgb_gamma(0, 100, 0)
        elif stress < 0.85:
            # Medium RPM: Solid Yellow (Red + Green)
            set_rgb_gamma(100, 80, 0)
        else:
            # REV LIMITER: Flashing Red!
            set_rgb_gamma(100, 0, 0)
            time.sleep(0.02)
            set_rgb_gamma(0, 0, 0)
            time.sleep(0.02)
            
        print(f"RPM: {int(rpm):5} | {'!!!SHIFT!!!' if stress > 0.85 else 'Accelerating'}", end="\r")
        
        time.sleep(0.05)

except KeyboardInterrupt:
    set_rgb_gamma(0, 0, 0)
    buzzer.duty_u16(0)
    print("\nECU Shutdown Successfully.")
