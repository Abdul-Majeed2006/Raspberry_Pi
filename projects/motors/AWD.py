# ==========================================================
# MOTOR PROJECT: AWD LIBRARY (REFINED)
# Goal: Reusable Class for 4-Wheel Drive control.
# Mapping: Front (15, 14, 13) | Back (12, 11, 10)
# ==========================================================

from machine import Pin
import time

class AWD:
    def __init__(self, f_pins, b_pins):
        """
        f_pins = (ena, in1, in2)
        b_pins = (enb, in3, in4)
        """
        # --- FRONT AXLE ---
        self.f_ena = Pin(f_pins[0], Pin.OUT)
        self.f_in1 = Pin(f_pins[1], Pin.OUT)
        self.f_in2 = Pin(f_pins[2], Pin.OUT)
        
        # --- BACK AXLE ---
        self.b_enb = Pin(b_pins[0], Pin.OUT)
        self.b_in3 = Pin(b_pins[1], Pin.OUT)
        self.b_in4 = Pin(b_pins[2], Pin.OUT)
        
        self.stop() # Safe start

    def drive_forward(self):
        # Front Move
        self.f_ena.value(1)
        self.f_in1.value(1); self.f_in2.value(0)
        
        # Back Move
        self.b_enb.value(1)
        self.b_in3.value(0); self.b_in4.value(1) # Inverted per test
        print("AWD: Moving Forward")

    def drive_backward(self):
        # Front Move
        self.f_ena.value(1)
        self.f_in1.value(0); self.f_in2.value(1)
        
        # Back Move
        self.b_enb.value(1)
        self.b_in3.value(1); self.b_in4.value(0)
        print("AWD: Moving Backward")

    def stop(self):
        self.f_ena.value(0); self.f_in1.value(0); self.f_in2.value(0)
        self.b_enb.value(0); self.b_in3.value(0); self.b_in4.value(0)
        print("AWD: Stopped")

# --- TEST CODE ---
if __name__ == "__main__":
    # Latest User Map: Front (15, 14, 13) | Back (12, 11, 10)
    truck = AWD(f_pins=(15, 14, 13), b_pins=(10, 11, 12))
    
    try:
        truck.drive_forward()
        time.sleep(2)
        
        truck.drive_backward()
        time.sleep(2)
        
        truck.stop()
        
    except KeyboardInterrupt:
        truck.stop()