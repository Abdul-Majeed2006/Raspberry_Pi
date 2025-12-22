# ==========================================================
# ROBOTICS UTILITY: SIGNAL VERIFICATION (FINAL)
# Goal: Debugging connections without mechanical stress.
# ==========================================================

from machine import Pin
import time

# Pin Manifest (Match your wires!)
ena = Pin(15, Pin.OUT)
in1 = Pin(14, Pin.OUT)
in2 = Pin(13, Pin.OUT)
enb = Pin(12, Pin.OUT)
in3 = Pin(11, Pin.OUT)
in4 = Pin(10, Pin.OUT)

def verify_all():
    print("--- SYSTEM DIAGNOTICS START ---")
    print("Checking Front Axle (Motor A)...")
    ena.value(1) # Keep Power ON
    in1.value(1); in2.value(0); time.sleep(1) # Forward LED
    in1.value(0); in2.value(1); time.sleep(1) # Backward LED
    ena.value(0); in1.value(0); in2.value(0)
    
    print("Checking Back Axle (Motor B)...")
    enb.value(1) # Keep Power ON
    in3.value(1); in4.value(0); time.sleep(1) # Forward LED
    in3.value(0); in4.value(1); time.sleep(1) # Backward LED
    enb.value(0); in3.value(0); in4.value(0)
    
    print("--- DIAGNOSTICS COMPLETE ---")
    print("Did all four logic LEDs blink in order?")

if __name__ == "__main__":
    verify_all()
