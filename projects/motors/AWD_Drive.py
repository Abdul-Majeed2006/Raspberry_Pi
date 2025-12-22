# ==========================================================
# MOTOR PROJECT 2: SYNCHRONIZED AWD (CALIBRATED)
# Goal: Fix physical wiring issues in software.
# ==========================================================

from machine import Pin, PWM
from time import sleep

class AWD_System:
    def __init__(self, invert_front=True, invert_back=False):
        # --- CALIBRATION ---
        # If your motor is wired 'backwards', we flip this flag.
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
        # 1. Base Logic (1 or -1)
        dir_mult = 1 if direction == "forward" else -1
        if direction == "stop": dir_mult = 0
        
        # 2. Polarity Masking (The "Virtual Swap")
        f_dir = dir_mult * (-1 if self.inv_f else 1)
        b_dir = dir_mult * (-1 if self.inv_b else 1)
        
        # 3. Hardware Pulse Logic
        f1, f2 = (1, 0) if f_dir == 1 else (0, 1) if f_dir == -1 else (0, 0)
        b1, b2 = (1, 0) if b_dir == 1 else (0, 1) if b_dir == -1 else (0, 0)

        # 4. Power Distribution
        f_speed = speed if mode in ["4WD", "FWD"] else 0
        b_speed = speed if mode in ["4WD", "RWD"] else 0

        # 5. EXECUTION
        # ENGINEERING INSIGHT: 
        # By setting the pins first, we prepare the 'path'. 
        # By setting PWM last, we release the power.
        self.f_in1.value(f1); self.f_in2.value(f2)
        self.b_in3.value(b1); self.b_in4.value(b2)
        
        # Small 1ms stagger to prevent battery dip (The "Sync Fix")
        self.f_ena.duty_u16(f_speed)
        sleep(0.001) 
        self.b_enb.duty_u16(b_speed)

    def stop(self):
        self.drive(0, "stop")

# --- EXECUTION ---
# Based on your test, Front is Inverted, Back is Normal.
truck = AWD_System(invert_front=True, invert_back=False)

try:
    print("--- CALIBRATED AWD TEST ---")
    print("All wheels should spin FORWARD now.")
    truck.drive(45000, "forward", "4WD")
    sleep(3)
    
    truck.stop()
    print("Test Complete.")

except KeyboardInterrupt:
    truck.stop()
