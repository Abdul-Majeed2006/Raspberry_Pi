# ==========================================================
# MOTOR PROJECT 1: MOTOR SPEED CONTROL (CALIBRATED)
# ==========================================================

from machine import Pin, PWM
from time import sleep

# --- HARDWARE CONFIG ---
# FRONT IS INVERTED (User hardware report)
INVERT_FRONT = True

ena = PWM(Pin(15))
ena.freq(1000)
in1 = Pin(14, Pin.OUT)
in2 = Pin(13, Pin.OUT)

def set_axle_speed(speed, direction="forward"):
    # Apply Inversion logic
    if direction == "forward":
        # If inverted, forward code actually sends backward pins
        if INVERT_FRONT:
            in1.value(0); in2.value(1)
        else:
            in1.value(1); in2.value(0)
    elif direction == "backward":
        if INVERT_FRONT:
            in1.value(1); in2.value(0)
        else:
            in1.value(0); in2.value(1)
    else:
        in1.value(0); in2.value(0)
    
    ena.duty_u16(speed)

try:
    print("--- CALIBRATED ACCELERATOR ---")
    for s in range(0, 50000, 2000):
        set_axle_speed(s, "forward")
        sleep(0.05)
    
    sleep(1)
    set_axle_speed(0, "stop")
    print("Test Complete.")

except KeyboardInterrupt:
    set_axle_speed(0, "stop")
