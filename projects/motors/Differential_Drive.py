# ==========================================================
# ROBOTICS PROJECT 2: DIFFERENTIAL DRIVE
# Goal: Create a high-level navigation library to control 
# a 2-wheeled robot chassis.
#
# ENGINEERING INSIGHT:
# "Abstraction." In complex robotics, we don't want to think 
# about IN1/IN2 every time we want to move. We create a 
# "Drive Layer" so we can just say robot.forward(). 
# ==========================================================

from machine import Pin, PWM
from time import sleep

class Robot:
    def __init__(self):
        # --- Motor A (Left) ---
        self.ena = PWM(Pin(15))
        self.in1 = Pin(14, Pin.OUT)
        self.in2 = Pin(13, Pin.OUT)
        
        # --- Motor B (Right) ---
        self.enb = PWM(Pin(12))
        self.in3 = Pin(11, Pin.OUT)
        self.in4 = Pin(10, Pin.OUT)
        
        # Initialization
        self.ena.freq(1000)
        self.enb.freq(1000)
        self.stop()

    def set_motors(self, left_speed, left_dir, right_speed, right_dir):
        """Sets raw hardware states for both motors."""
        # Left Motor Logic
        if left_dir == 1: # Forward
            self.in1.value(1); self.in2.value(0)
        elif left_dir == -1: # Backward
            self.in1.value(0); self.in2.value(1)
        else: # Stop
            self.in1.value(0); self.in2.value(0)
            
        # Right Motor Logic
        if right_dir == 1: # Forward
            self.in3.value(1); self.in4.value(0)
        elif right_dir == -1: # Backward
            self.in3.value(0); self.in4.value(1)
        else: # Stop
            self.in3.value(0); self.in4.value(0)
            
        self.ena.duty_u16(left_speed)
        self.enb.duty_u16(right_speed)

    def forward(self, speed=40000):
        print("Maneuver: FORWARD")
        self.set_motors(speed, 1, speed, 1)

    def backward(self, speed=40000):
        print("Maneuver: BACKWARD")
        self.set_motors(speed, -1, speed, -1)

    def spin_left(self, speed=40000):
        print("Maneuver: PIVOT LEFT")
        self.set_motors(speed, -1, speed, 1)

    def spin_right(self, speed=40000):
        print("Maneuver: PIVOT RIGHT")
        self.set_motors(speed, 1, speed, -1)

    def stop(self):
        print("Maneuver: STOP")
        self.set_motors(0, 0, 0, 0)

# --- EXECUTION ---
bot = Robot()

try:
    print("--- STARTING NAVIGATION TEST ---")
    
    bot.forward(45000)
    sleep(2)
    
    bot.stop()
    sleep(1)
    
    bot.spin_right(45000) # Turn 90 degrees (approx)
    sleep(0.8)
    
    bot.forward(45000)
    sleep(2)
    
    bot.stop()
    print("Test Complete. Bot Securing.")

except KeyboardInterrupt:
    bot.stop()
    print("\nSafety Stop Triggered.")
