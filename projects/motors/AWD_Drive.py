# ==========================================================
# MOTOR PROJECT: SYNCHRONIZED AWD (FINAL CALIBRATION)
# Goal: Fixed the inverted back axle in software.
# ==========================================================

from machine import Pin, PWM
from time import sleep

class AWD_System:
    def __init__(self, invert_front=False, invert_back=True):
        # --- CALIBRATION ---
        # Front was reported as Normal. Back was reported as Inverted.
        self.inv_f = invert_front
        self.inv_b = invert_back
        
        # --- FRONT AXLE ---
        self.f_ena = PWM(Pin(15))
        self.f_in1 = Pin(14, Pin.OUT)
        self.f_in2 = Pin(13, Pin.OUT)
        
        # --- BACK AXLE ---
        self.b_enb = PWM(Pin(12))
        self.b_in3 = Pin(11, Pin.OUT)
        self.b_in4 = Pin(10, Pin.OUT)
        
        # Standard Setup
        self.f_ena.freq(1000)
        self.b_enb.freq(1000)
        self.stop()

    def drive(self, speed, direction="forward", mode="4WD"):
        """
        Calculates and sends signals for Sync'd Axle Drive.
        mode: "4WD", "FWD", "RWD"
        """
        # 1. Base Logic (1 or -1 or 0)
        dir_mult = 0
        if direction == "forward": dir_mult = 1
        elif direction == "backward": dir_mult = -1
        
        # 2. Polarity Masking (Corrects wiring mistakes)
        f_dir = dir_mult * (-1 if self.inv_f else 1)
        b_dir = dir_mult * (-1 if self.inv_b else 1)
        
        # 3. Hardware Pulse Logic
        f1, f2 = (1, 0) if f_dir == 1 else (0, 1) if f_dir == -1 else (0, 0)
        b1, b2 = (1, 0) if b_dir == 1 else (0, 1) if b_dir == -1 else (0, 0)

        # 4. Power Distribution
        f_speed = speed if mode in ["4WD", "FWD"] else 0
        b_speed = speed if mode in ["4WD", "RWD"] else 0

        # 5. EXECUTION
        self.f_in1.value(f1); self.f_in2.value(f2)
        self.b_in3.value(b1); self.b_in4.value(b2)
        
        # Small stagger to prevent battery sag
        self.f_ena.duty_u16(f_speed)
        sleep(0.005) 
        self.b_enb.duty_u16(b_speed)

    def stop(self):
        self.drive(0, "stop")

# --- EXECUTION ---
# Calibrated: Front is Normal (False), Back is Inverted (True).
truck = AWD_System(invert_front=False, invert_back=True)

try:
    print("--- CALIBRATED AWD TEST ---")
    print("All wheels should spin FORWARD now.")
    truck.drive(45000, "forward")
    sleep(3)
    
    print("Switching to BACKWARD...")
    truck.drive(45000, "backward")
    sleep(3)
    
    truck.stop()
    print("Test Complete.")

except KeyboardInterrupt:
    truck.stop()
