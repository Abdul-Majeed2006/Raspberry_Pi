# ==========================================================
# ROBOTICS PROJECT 1: MOTOR SPEED CONTROL (REFINED)
# Goal: Mastering the "Soft-Start" for geared axles.
#
# ENGINEERING INSIGHT:
# "Mechanical Inertia." Because your motors move geared 
# axles, starting at 100% power can skip gear teeth or slip 
# the glue. We use RAMPING to overcome inertia gently.
# ==========================================================

from machine import Pin, PWM
from time import sleep

# --- HARDWARE CONFIGURATION ---
# ENA = Front Speed | ENB = Back Speed
# We define them here to control the "Pulse" of the car.
ena = PWM(Pin(15))
ena.freq(1000)

# Direction Pins (Front Axle)
in1 = Pin(14, Pin.OUT)
in2 = Pin(13, Pin.OUT)

def set_axle_speed(speed, direction="forward"):
    """
    Sets the Front Axle state.
    Speed: 0 to 65535
    Direction: "forward", "backward", "stop"
    """
    if direction == "forward":
        in1.value(1); in2.value(0)
    elif direction == "backward":
        in1.value(0); in2.value(1)
    else:
        in1.value(0); in2.value(0)
    
    ena.duty_u16(speed)

try:
    print("--- INERTIA TEST: SOFT START ---")
    # Ramp up slowly (2 seconds)
    for s in range(0, 65535, 1000):
        set_axle_speed(s, "forward")
        sleep(0.02)
        
    print("Cruising at 100% power...")
    sleep(2)
    
    # Ramp down slowly
    for s in range(65535, 0, -1000):
        set_axle_speed(s, "forward")
        sleep(0.01)

    set_axle_speed(0, "stop")
    print("Test Complete. Axle Securing.")

except KeyboardInterrupt:
    set_axle_speed(0, "stop")
    print("\nEmergency Stop.")
