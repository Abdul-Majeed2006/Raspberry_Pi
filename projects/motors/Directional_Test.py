# ==========================================================
# MOTOR UTILITY: BI-DIRECTIONAL STRESS TEST
# Goal: Verify if both axles can actually move in both directions.
# ==========================================================

from machine import Pin
import time

# --- PINS (FRONT AXLE) ---
ena = Pin(15, Pin.OUT); in1 = Pin(14, Pin.OUT); in2 = Pin(13, Pin.OUT)

# --- PINS (BACK AXLE) ---
enb = Pin(10, Pin.OUT); in3 = Pin(12, Pin.OUT); in4 = Pin(11, Pin.OUT)

def stress_test():
    print("--- DIRECTIONAL STRESS TEST START ---")
    
    # 1. FRONT AXLE ONLY
    print("FRONT AXLE: Forward...")
    ena.value(1); in1.value(0); in2.value(1); time.sleep(1)
    print("FRONT AXLE: Stop...")
    ena.value(0); in1.value(0); in2.value(0); time.sleep(1)
    
    print("FRONT AXLE: BACKWARD...")
    ena.value(1); in1.value(0); in2.value(1); time.sleep(1)
    ena.value(0); in1.value(0); in2.value(0); time.sleep(1)

    # 2. BACK AXLE ONLY
    print("BACK AXLE: Forward...")
    enb.value(1); in3.value(0); in4.value(1); time.sleep(2)
    print("BACK AXLE: Stop...")
    enb.value(0); in3.value(0); in4.value(0); time.sleep(1)
    
    print("BACK AXLE: BACKWARD...")
    enb.value(1); in3.value(1); in4.value(0); time.sleep(2)
    enb.value(0); in3.value(0); in4.value(0)
    
    print("--- TEST COMPLETE ---")

#if __name__ == "__main__":
stress_test()
