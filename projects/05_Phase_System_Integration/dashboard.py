# ==========================================================
# PHASE 05: SYSTEM INTEGRATION (DASHBOARD CONTROLLER)
# Goal: Run Motors and OLED Screen simultaneously.
# ==========================================================

from machine import Pin, I2C
import time
import random

# Import our custom drivers (Phase 03 and Phase 04)
from AWD import AWD
from ssd1306 import SSD1306_I2C

# --- CONFIGURATION ---
# I2C Pins (Screen)
I2C_ID = 0
SDA_PIN = 16
SCL_PIN = 17

# Motor Pins (Front: 15,14,13 | Back: 10,11,12)
FRONT_PINS = (15, 14, 13)
BACK_PINS = (10, 11, 12)

class Dashboard:
    def __init__(self):
        # 1. Wake up the Screen
        print("Initializing Dashboard...")
        self.i2c = I2C(I2C_ID, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN))
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        
        # 2. Wake up the Truck
        print("Initializing AWD Chassis...")
        self.truck = AWD(FRONT_PINS, BACK_PINS)
        
        # 3. Boot Animation
        self.show_boot_screen()
        
    def show_boot_screen(self):
        self.oled.fill(0)
        self.oled.fill_rect(0, 0, 128, 15, 1) # Header Bar
        self.oled.text("AWD TRUCK PRO", 10, 4, 0)
        self.oled.text("System Ready...", 5, 25, 1)
        self.oled.show()
        time.sleep(2)

    def update_display(self, speed, direction, status_text):
        """
        Draws the main dashboard UI.
        """
        self.oled.fill(0)
        
        # --- HEADER ---
        self.oled.fill_rect(0, 0, 128, 12, 1)
        self.oled.text("AWD DASHBOARD", 10, 2, 0)
        
        # --- MAIN STATUS (Big Text) ---
        # Note: Standard font is small, so we use caps and spacing
        self.oled.text(f"DIR: {direction}", 5, 20, 1)
        self.oled.text(f"PWR: {speed}%", 5, 32, 1)
        
        # --- VISUALIZER ---
        # Draw a little truck box
        self.oled.rect(90, 20, 30, 40, 1) # Chassis
        
        # Draw Wheels based on motion
        if direction == "FWD":
            self.oled.fill_rect(88, 22, 4, 8, 1) # Front Left moving
            self.oled.fill_rect(118, 22, 4, 8, 1) # Front Right moving
        elif direction == "REV":
            self.oled.fill_rect(88, 50, 4, 8, 1) # Back Left moving
            self.oled.fill_rect(118, 50, 4, 8, 1) # Back Right moving
            
        # --- FOOTER ---
        self.oled.hline(0, 52, 128, 1)
        self.oled.text(status_text, 5, 55, 1)
        
        self.oled.show()

    def run_demo(self):
        """
        Main Loop: Cycles through driving modes.
        """
        print("Starting Demo Loop...")
        try:
            while True:
                # 1. Drive Forward (2 Seconds)
                self.truck.drive_forward()
                self.update_display(100, "FWD", "Status: CRUISE")
                time.sleep(2)
                
                # 2. Stop (1 Second)
                self.truck.stop()
                self.update_display(0, "STOP", "Status: IDLE")
                time.sleep(1)
                
                # 3. Drive Backward (2 Seconds)
                self.truck.drive_backward()
                self.update_display(100, "REV", "Status: BACKING")
                time.sleep(2)
                
                # 4. Stop (1 Second)
                self.truck.stop()
                self.update_display(0, "STOP", "Status: IDLE")
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.truck.stop()
            self.oled.fill(0)
            self.oled.text("SYSTEM HALTED", 10, 30, 1)
            self.oled.show()
            print("Dashboard Shutdown.")

# --- ENTRY POINT ---
if __name__ == "__main__":
    dash = Dashboard()
    dash.run_demo()
