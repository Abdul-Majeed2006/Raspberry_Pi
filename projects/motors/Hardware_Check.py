# ==========================================================
# MOTOR PROJECT: ULTIMATE VERIFICATION (RESET)
# Goal: Confirm hardware health after wiring fix.
# ==========================================================

from machine import Pin
import time

# --- PINS (FRONT AXLE) ---
ena = Pin(15, Pin.OUT)
in1 = Pin(14, Pin.OUT)
in2 = Pin(13, Pin.OUT)

# --- PINS (BACK AXLE) ---
enb = Pin(12, Pin.OUT)
in3 = Pin(11, Pin.OUT)
in4 = Pin(10, Pin.OUT)

def hardware_test():
    print("--- HARDWARE VERIFICATION START ---")
    print("Testing Front Axle (Motor A)...")
    ena.value(1)
    in1.value(1); in2.value(0); time.sleep(1)
    in1.value(0); in2.value(1); time.sleep(1)
    ena.value(0); in1.value(0); in2.value(0)
    
    print("Testing Back Axle (Motor B)...")
    enb.value(1)
    in3.value(1); in4.value(0); time.sleep(1)
    in3.value(0); in4.value(1); time.sleep(1)
    enb.value(0); in3.value(0); in4.value(0)
    
    print("--- VERIFICATION COMPLETE ---")

if __name__ == "__main__":
    hardware_test()
