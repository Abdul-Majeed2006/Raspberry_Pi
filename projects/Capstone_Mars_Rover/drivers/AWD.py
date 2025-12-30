# ==========================================================
# DRIVER: 4-Wheel Drive (AWD) Chassis
# ==========================================================
# Wraps the L298N H-Bridge logic into a simple "Truck" object.
# ==========================================================

from machine import Pin
import time

class HardwareConfig:
    # Front Axle (H-Bridge A)
    PIN_F_ENA = 15; PIN_F_IN1 = 14; PIN_F_IN2 = 13
    # Back Axle (H-Bridge B)
    PIN_B_ENB = 10; PIN_B_IN3 = 11; PIN_B_IN4 = 12

class AWD:
    def __init__(self):
        # Setup Front
        self.f_ena = Pin(HardwareConfig.PIN_F_ENA, Pin.OUT)
        self.f_in1 = Pin(HardwareConfig.PIN_F_IN1, Pin.OUT)
        self.f_in2 = Pin(HardwareConfig.PIN_F_IN2, Pin.OUT)
        
        # Setup Back
        self.b_enb = Pin(HardwareConfig.PIN_B_ENB, Pin.OUT)
        self.b_in3 = Pin(HardwareConfig.PIN_B_IN3, Pin.OUT)
        self.b_in4 = Pin(HardwareConfig.PIN_B_IN4, Pin.OUT)
        self.stop() 

    def forward(self):
        # Front: Forward
        self.f_ena.value(1)
        self.f_in1.value(1); self.f_in2.value(0)
        # Back: Forward
        self.b_enb.value(1)
        self.b_in3.value(0); self.b_in4.value(1)

    def backward(self):
        # Front: Reverse
        self.f_ena.value(1)
        self.f_in1.value(0); self.f_in2.value(1)
        # Back: Reverse
        self.b_enb.value(1)
        self.b_in3.value(1); self.b_in4.value(0)
        
    def turn_left(self):
        self.b_enb.value(0) # Drag rear
        self.f_ena.value(1)
        self.f_in1.value(1); self.f_in2.value(0)

    def turn_right(self):
        self.b_enb.value(0) # Drag rear
        self.f_ena.value(1)
        self.f_in1.value(0); self.f_in2.value(1)

    def stop(self):
        self.f_ena.value(0); self.f_in1.value(0); self.f_in2.value(0)
        self.b_enb.value(0); self.b_in3.value(0); self.b_in4.value(0)
