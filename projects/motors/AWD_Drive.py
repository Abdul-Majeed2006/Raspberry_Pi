# ==========================================================
# ROBOTICS PROJECT 2: SYNCHRONIZED AWD (REFINED)
# Goal: Professional Drive Library for geared axles.
#
# ENGINEERING INSIGHT:
# "Current Draw & Voltage Sag." Driving two motors at 100% 
# consumes significant power. If your Pico resets when you 
# start the motors, it's because the battery voltage "sagged" 
# below the limit. Use AWD_System to manage load.
# ==========================================================

from machine import Pin, PWM
from time import sleep

class AWD_System:
    def __init__(self):
        # Front Axle
        self.f_ena = PWM(Pin(15))
        self.f_in1 = Pin(14, Pin.OUT)
        self.f_in2 = Pin(13, Pin.OUT)
        
        # Back Axle
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
        mode: "4WD" (All wheels), "FWD" (Front Only), "RWD" (Rear Only)
        """
        # 1. Logic Gates
        f1, f2 = (1, 0) if direction == "forward" else (0, 1)
        b1, b2 = (1, 0) if direction == "forward" else (0, 1)

        if direction == "stop":
            f1, f2, b1, b2, speed = 0, 0, 0, 0, 0

        # 2. Power Distribution
        f_speed = speed if mode in ["4WD", "FWD"] else 0
        b_speed = speed if mode in ["4WD", "RWD"] else 0

        # 3. Synchronize Output
        self.f_in1.value(f1); self.f_in2.value(f2)
        self.b_in3.value(b1); self.b_in4.value(b2)
        self.f_ena.duty_u16(f_speed)
        self.b_enb.duty_u16(b_speed)

    def stop(self):
        self.drive(0, "stop")

# --- NAVIGATION SANDBOX ---
truck = AWD_System()

try:
    print("--- AWD MISSION START ---")
    
    print("Phase 1: 4WD Torque (Climbing)...")
    truck.drive(40000, "forward", "4WD")
    sleep(2)
    
    print("Phase 2: RWD Cruise (Savings mode)...")
    truck.drive(30000, "forward", "RWD")
    sleep(2)
    
    truck.stop()
    print("Mission Complete. Motors Coasting.")

except KeyboardInterrupt:
    truck.stop()
